# this is the project file

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, and_ , or_
from sqlalchemy.orm import sessionmaker
from data_setup import MedCategory, Base, MedList

app = Flask(__name__)

# app.config['JSON_SORT_KEYS'] = False


#Imports for session token
from flask import session as login_session
import random, string


engine = create_engine('sqlite:///medication.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Create state session to prevent forgery login_session
@app.route("/login")
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return 'The current session state is %s' % login_session['state']



def queryData():
    allCategory = session.query(MedCategory).all()
    allCatergoryMeds = session.query(MedList).all()
    return allCategory, allCatergoryMeds

def questFilter(category, med):
    oneCategory = session.query(MedCategory).filter_by(category=medcat).one()
    oneMed = session.query(MedList).filter_by(name=med).one()
    return oneCategory, oneMed



def add_entry(query):
    session.add(query)
    session.commit()


def delete_entry(query):
    session.delete(query)
    session.commit()


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
@app.route('/medication/<string:meds>/JSON')
def categoryMedsJSON(medcat):
    medcategory = session.query(MedCategory).filter_by(category=medcat).one()
    medss = session.query(MedList).filter_by(medcategory_id=medcategory.id).all()
    return jsonify(medictions=[i.serialize for i in medss], message="Medication list created successfully", Message='This is the list for %s medications' % meds)

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
    medicationclass = session.query(MedCategory).all()
    return render_template('Home.html', medicationclass=medicationclass)



@app.route('/medication/<string:medcat>/')
def medsCatList(medcat):
    medicationlist = session.query(MedCategory).all()
    categoryM = session.query(MedCategory).filter_by(category=medcat).first()
    medsdisplay = session.query(MedList).filter_by(medcategory_id=categoryM.id).all()
    return render_template('category.html', categoryM=categoryM, medsdisplay=medsdisplay, medicationlist=medicationlist)
    ##return render_template('categoryPublic.html', categoryM=categoryM, medsdisplay=medsdisplay, medicationlist=medicationlist)


@app.route('/medication/<string:medcat>/<string:med>/')
def medList(medcat, med):
    caMed = session.query(MedCategory).filter_by(category=medcat).one()
    categoryM = session.query(MedList).filter_by(medcategory_id=caMed.id).all()
    medsdisplay = session.query(MedList).filter_by(name=med).one()
    return render_template('catMeds.html', categoryM=categoryM, medsdisplay=medsdisplay, caMed=caMed)
    ##return render_template('catMedsPublic.html', categoryM=categoryM, medsdisplay=medsdisplay, caMed=caMed)








# Creating, editing and deleting medication category
@app.route('/medication/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        if request.form['category']:
            category1 = MedCategory(category=request.form['category'])
            add_entry(category1)
            flash("%s category created!" % request.form['category'])
            return redirect(url_for('medsCatList',medcat=request.form['category']))
        else:
            return render_template('newCategory.html')
    else:
        return render_template('newCategory.html')




@app.route('/medication/<string:medcat>/Edit/', methods=['GET', 'POST'])
def editCategory(medcat):
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
    catTodel = session.query(MedCategory).filter_by(category=medcat).first()
    catTodel2 = session.query(MedCategory).filter_by(id='1').first()
    name = catTodel.category
    if request.method == 'POST':
        delete_entry(catTodel)
        flash("%s deleted from category!" % name)
        ##return redirect(url_for('medicationlist'))
        return redirect(url_for('medsCatList',medcat=catTodel2.category))

    else:
        return render_template('deleteCategory.html',medcat=medcat)









# creating, editing and deleting medication



@app.route('/medication/<string:medcat>/New/', methods=['GET', 'POST'])
def createMedication(medcat):
    caMed = session.query(MedCategory).filter_by(category=medcat).one()
    if request.method == 'POST':
        if request.form['name']:
            newMed= MedList(name = request.form['name'], description = request.form['description'], adverseEffect = request.form['adverseEffect'], pregnancyCategory = request.form['pregnancyCategory'], medcategory_id=caMed.id)
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
    medTodel = session.query(MedList).filter_by(name=med).first()
    medTodel2 = session.query(MedList).filter_by(id='1').first()
    deletecat = session.query(MedCategory).filter_by(category=medcat).one()

    if request.method == 'POST':
        delete_entry(medTodel)
        flash("%s deleted from %s category!" % (med, medcat))
        #return redirect(url_for('medicationlist',medcat=deletecat.category))
        return redirect(url_for('medList', medcat=deletecat.category, med=medTodel2.name))

    else:
        return render_template('deleteMedication.html',medcat=medcat, med=med, deletecat=deletecat, medTodel=medTodel)




if __name__ == '__main__':

    app.secret_key = 'Super_Secret_Key'
    app.debug = True
    app.run(host='0.0.0.0', port=9080)
