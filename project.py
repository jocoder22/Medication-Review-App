# this is the project file

from flask import (Flask, 
                   render_template, 
                   request, 
                   redirect, 
                   url_for, 
                   flash, 
                   jsonify,
                   make_response,
                   session as login_session)

from sqlalchemy import create_engine, and_ , or_, asc
from sqlalchemy.orm import sessionmaker
from database_setup import MedCategory, Base, MedList, User


#Imports to handle result sent by signInCallback function on the login.html
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json, random, string
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Medication Review App"

# connect to the database and create database session
engine = create_engine('sqlite:///medication.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def queryData():
    allCategory = session.query(MedCategory).order_by(asc(MedCategory.category))
    allCatergoryMeds = session.query(MedList).order_by(asc(MedList.name))
    return allCategory, allCatergoryMeds


def add_entry(query):
    session.add(query)
    session.commit()


def delete_entry(query):
    session.delete(query)
    session.commit()

#Create state session to prevent forgery login_session
@app.route("/login")
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    #return 'The current session state is %s' % login_session['user_id']
    return render_template('login.html', STATE=state)


@app.route("/loginstate")
def showLoginState():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return 'The current session state is %s' % login_session['state']
    #return render_template('login.html', STATE=state)



# connect the user and initial the OAuth process
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id


    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    add_entry(newUser)
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None



@app.route('/users/JSON')
def showUserJSON():
    users = session.query(User).order_by(asc(User.name))
    return jsonify(allUsers=[i.serialize for i in users], message="All users list created successfully")


# Create a JSON file of all medication on the database.
@app.route('/medication/all/JSON')
def showAllMedsJSON():
    a,b = queryData()
    return jsonify(AllMEDS=[i.serialize for i in b], message="All medication list created successfully")

# Create a JSON file of the all medication categories.
@app.route('/medication/category/JSON')
def allCategoryJSON():
    a,b = queryData()
    return jsonify(Category=[i.serialize for i in a], message="Medication list created successfully")

# Create a JSON file of the all medications within a category.
@app.route('/medication/<string:medcat>/JSON')
def categoryMedsJSON(medcat):
    medcategory = session.query(MedCategory).filter_by(category=medcat).one()
    medss = session.query(MedList).order_by(asc(MedList.name)).filter_by(medcategory_id=medcategory.id).all()
    return jsonify(medictions=[i.serialize for i in medss], message="Medication list created successfully", Message='This is the list for %s medications' % medcat)

# Create a JSON file of the a particular medication.
@app.route('/medication/<string:category>/<string:meds>/JSON')
def oneMedicationJSON(category, med):
    try:
        medication = session.query(MedCategory).filter_by(category=category).one()
        onemedication = session.query(MedList).filter_by(name=med, medcategory_id=medication.id).one()
        return jsonify(medication=[onemedication.serialize], message="Medication list created successfully", Message='This is for %s' % meds)
    except:

        return jsonify(message="Please ensure that your are searching in the right medication category and the medication exist in the database", Message=" .... Sorry we can't find your medication in our database under the %s category" % category)






@app.route('/')
@app.route('/medication/')
def medicationlist():
    ##medicationclass = session.query(MedCategory).all()
    medicationclass = session.query(MedCategory).order_by(asc(MedCategory.category))
    return render_template('Home.html', medicationclass=medicationclass)



@app.route('/medication/<string:medcat>/')
def medsCatList(medcat):
    medicationlist = session.query(MedCategory).order_by(asc(MedCategory.category))
    categoryM = session.query(MedCategory).filter_by(category=medcat).first()
    medsdisplay = session.query(MedList).filter_by(medcategory_id=categoryM.id).order_by(asc(MedList.name)).all()
    if 'username' in login_session:
        return render_template('category.html', categoryM=categoryM, medsdisplay=medsdisplay, medicationlist=medicationlist)
    else:
        return render_template('categoryPublic.html', categoryM=categoryM, medsdisplay=medsdisplay, medicationlist=medicationlist)


@app.route('/medication/<string:medcat>/<string:med>/')
def medList(medcat, med):
    caMed = session.query(MedCategory).filter_by(category=medcat).one()
    categoryM = session.query(MedList).order_by(asc(MedList.name)).filter_by(medcategory_id=caMed.id).all()
    medsdisplay = session.query(MedList).filter_by(name=med).one()
    if 'username' in login_session:
        return render_template('catMeds.html', categoryM=categoryM, medsdisplay=medsdisplay, caMed=caMed)
    else:
        return render_template('catMedsPublic.html', categoryM=categoryM, medsdisplay=medsdisplay, caMed=caMed)








# Creating, editing and deleting medication category
@app.route('/medication/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    user1 = getUserInfo()
    user1 = session.query(User).filter_by(name=login_session['username']).first()
    if request.method == 'POST':
        if request.form['category']:
            category1 = MedCategory(category=request.form['category'], user=user1)
            add_entry(category1)
            flash("%s category created!" % request.form['category'])
            return redirect(url_for('medsCatList',medcat=request.form['category']))
        else:
            return render_template('newCategory.html')
    else:
        return render_template('newCategory.html')




@app.route('/medication/<string:medcat>/Edit/', methods=['GET', 'POST'])
def editCategory(medcat):
    if 'username' not in login_session:
        return redirect('/login')
    catToEdit = session.query(MedCategory).filter_by(category=medcat).first()
    if request.method == 'POST':
        if request.form['category']:
            catToEdit.category = request.form['category']
            add_entry(catToEdit)
            flash("%s category edited!" % request.form['category'])
            return redirect(url_for('medsCatList',medcat=catToEdit.category))
        else:
            return render_template('editCategory.html',medcat=medcat,catToEdit=catToEdit)
    else:
        return render_template('editCategory.html',medcat=medcat, catToEdit=catToEdit)




@app.route('/medication/<string:medcat>/Delete/', methods=['GET', 'POST'])
def deleteCategory(medcat):
    if 'username' not in login_session:
        return redirect('/login')
    catTodel = session.query(MedCategory).filter_by(category=medcat).first()
    #catTodel2 = session.query(MedCategory).filter_by(id='1').first()
    name = catTodel.category
    if request.method == 'POST':
        delete_entry(catTodel)
        flash("%s deleted from category!" % name)
        ##return redirect(url_for('medicationlist'))
        catTodel2 = session.query(MedCategory).order_by(asc(MedCategory.category)).first()
        return redirect(url_for('medsCatList',medcat=catTodel2.category))

    else:
        return render_template('deleteCategory.html',medcat=medcat)









# creating, editing and deleting medication
@app.route('/medication/<string:medcat>/New/', methods=['GET', 'POST'])
def createMedication(medcat):
    if 'username' not in login_session:
            return redirect('/login')
    caMed = session.query(MedCategory).filter_by(category=medcat).one()
    if request.method == 'POST':
        if request.form['name']:
            newMed= MedList(name = request.form['name'], description = request.form['description'], adverseEffect = request.form['adverseEffect'], pregnancyCategory = request.form['pregnancyCategory'], medcategory_id=caMed.id, user_id=caMed.user_id)
            add_entry(newMed)
        #flash('New Medication added successfully!!')
            flash("%s created in %s category!" % (request.form['name'], medcat))
            return redirect(url_for('medsCatList', medcat=medcat))

        else:
            return render_template('newMedication.html', medcat=medcat)
            #flash('New Medication added successfully!!')
    else:
        return render_template('newMedication.html', medcat=medcat)



@app.route('/medication/<string:medcat>/<string:med>/Edit', methods=['GET', 'POST'])
def editMedication(medcat, med):
    if 'username' not in login_session:
        return redirect('/login')
    medToEdit = session.query(MedList).filter_by(name=med).one()
    editcat = session.query(MedCategory).filter_by(category=medcat).one()
    if request.method == 'POST':
        if request.form['name']:
            medToEdit.name = request.form['name']
            medToEdit.description = request.form['description']
            medToEdit.adverseEffect = request.form['adverseEffect']
            medToEdit.pregnancyCategory = request.form['pregnancyCategory']
            medToEdit.medcategory_id = request.form['medcategory_id']
            add_entry(medToEdit)
            flash("%s updated in %s category!" % (request.form['name'], medcat))
            return redirect(url_for('medList', medcat=editcat.category, med=medToEdit.name))
        else:
            return render_template('editMedication.html',medcat=medcat,med=med, medToEdit=medToEdit, editcat=editcat)

    else:
        return render_template('editMedication.html',medcat=medcat,med=med, medToEdit=medToEdit, editcat=editcat)


@app.route('/medication/<string:medcat>/<string:med>/Delete/', methods=['GET', 'POST'])
def deleteMedication(medcat, med):
    if 'username' not in login_session:
        return redirect('/login')
    medTodel = session.query(MedList).filter_by(name=med).first()
    deletecat = session.query(MedCategory).filter_by(category=medcat).one()

    if request.method == 'POST':
        delete_entry(medTodel)
        flash("%s deleted from %s category!" % (med, medcat))
        medTodel2 = session.query(MedList).filter_by(medcategory_id= deletecat.id).order_by(asc(MedList.name)).first()
        return redirect(url_for('medList', medcat=deletecat.category, med=medTodel2.name))

    else:
        return render_template('deleteMedication.html',medcat=medcat, med=med, deletecat=deletecat, medTodel=medTodel)




if __name__ == '__main__':

    app.secret_key = 'Super_Secret_Key'
    app.debug = True
    app.run(host='0.0.0.0', port=9080)
