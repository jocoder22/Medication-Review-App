# Medication Review App
This is web application that list medication categories and medications within each category. For each medication, the app display brief information about the name, brief description, adverse effects and FDA pregnancy classification of the medication. This information will be presented to public for guidance on medication use.
## App Implementation
This is a `RESTful` web application implemented on Python framework Flask incorporating `Google` and `Facebook` third party `OAuth authentication`. Registered users can view, edit and delete medication categories and medications created by them while unregistered user can only view the medication categories and medication within each category.
Registered user are logged in using either `Google` or `Facebook` API and can view all medication categories. Registered logged in users can create new medication categories and medication list under same category but can only edit or deleted medication categories and medications created by them from the list.
Unregistered user not authenticated by either `Google` or `Facebook` cannot log in and can only view list medication categories and medication within the category. They cannot create new medication category and medication or delete or edit them.
### App Backend
The app has a `Sqlalchemy` based database consisting of the following tables:
* User
* Medication Category
* Medication
