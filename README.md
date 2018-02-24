# Medication Review App
## Introduction
This is a web application that list medication categories and medications within each category. For each medication, the app display information about the name, brief description, adverse effects and FDA pregnancy category of the medication. This information will be presented to public for guidance on medication use. 

## App Implementation
This is a `RESTful` web application implemented on Python framework Flask incorporating `Google` and `Facebook` third party `OAuth authentication`. Registered users can view, edit and delete medication categories and medications created by them while unregistered user can only view the medication categories and medication within each category.

* **Required Libraries and dependencies** 
  - `Python 2.7` 
    - `Flask`
    - `SQLAlchemy`

* **Registered user**
  - Registered users are logged in using either `Google` or `Facebook` API and can view all medication categories. Registered logged in users can create new medication categories and medication list under same category but can only edit or deleted medication categories and medications created by them from the list.
* **Unregistered**
  - Unregistered user not authenticated by either `Google` or `Facebook` cannot log in and can only view list medication categories and medication within the category. They cannot create new medication category and medication or delete or edit them. Unregistered user can register and log in using either `Google` or `Facebook` for 'OAuth` authentication and authorization system.
### App Backend
The app has a `Sqlalchemy` based database consisting of the following tables:
* **User table** contains:
  - User Id
  - User Name
  - User Email
  - User Picture

* **Medication Category table** contains:
   - Category Id
   - Category Name
   
* **Medication table** contains:
  - Medication Id
  - Medication Name
  - Description
  - FDA Pregnancy Category
  - Adverse Effect
   
These three tables are related to each other through a `Relationship` links using `ForeignKey`
   
### JSON endpoint
The app also provide `JSON`endpoints for medication categories and medications listed on the database.
 - use http://www.jocoder22.com/medication/all/JSON  to request JSON data of all medications.
 - use http://www/jocoder22.com/medication/category/JSON to request JSON data of medication category

## Installation
* **Google OAuth2** 
   - Visit [google developer page](https://console.developers.google.com/apis) and create OAuth client ID and client secret that will enable communication with google API libraries and the web application. The `project.py` and `login.html` implements the login and callback function for google OAuth2 authentication and authorization process. [Google documentation](https://developers.google.com/identity/protocols/OAuth2) for more information
 * **Operating Instruction**
    - On the web browser run http://www.jocoder22.com/medication 
    - sign in with google email account

