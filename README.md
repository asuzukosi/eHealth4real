Design Document for eHealth4real, a parody of eHealth4everyone.

This application is an assessment for eHealth4everyone job application.

Requirements:
1.	Sign-up page for users
2.	A page where users can fill in their medical information with relevant questions depending on the developer's discretion.
3.	A sign-up page for medical practitioners
4.	A page that displays the statistical details of the medical records gotten from the users (all users can view this page) e.g. A chart that shows the count for users with Ebola.
5.	A table that displays all users and their relevant medical records (only users registered as medical practitioners can view this page).
6.	A drop-down filter to show users with specified medical records of your own discretion e.g show only users with Malaria.


Design:

   •This application uses the Flora UI kit and Bootstrap for its user interface components

**Models**

Patient: 
1)	User - This is a one to one relationship with Django’s inbuilt user model
	
2)  Age – This is the age of the patient 
3)  Gender – This is the gender of the patient
4)	Phone number – This is the phone number of the patient 
5)	Diseases - This is a many to many relationship with the disease model, this show the diseases that the patient has
6)	On medication – This identifies if the patient is on any medication
7)	Occupation – This is the occupation of the patient
8)	Address – This is the address of the patient 
9)	Emergency Contact Name – This is the name of the emergency contact of the     patient
10)	Emergency Contact Number – This is the number of the emergency contact of the patient
11)	Relationship with patient – This is the relationship of the emergency contact with the patient
12)	Medical Implant – This is to know if the patient has any medical implant
13)	Date added – This is the day that the patient registered on eHealth4real
14)	Previous Surgery – This is information on any previous surgery done by the patient
15)	Patient Hospitalized – This is information on whether patient has previously been hospitalized
17)	Registered – This is used to validate if patient has entered in valid medical details

**Groups**

Users are divided into 2 groups Patients and Medics, so that each group has its unique permissions. User can only belong to one group, unless manually set from admin.

1)	Patient: Group for patients
2)	Medic:	Group for medics	

**Views**
1)	Home – This is the view that has all the data analytics, this view is accessible to all users, user must be logged in to access this view
2)	Login Page – This is the page to log users in, user must be logged out in order to access this page
3)	Register Page – This is the base register page, this is where the user decides if they want to register as a patient or as a medical practitioner, a user must be logged out in order to access this page
4)	Patient Register – This is the registration page for patients, a user must be logged out in order to access this page
5)	Medical Practitioner Register – This is the registration page for medical practitioners, a user must be logged out in order to access this page
6)	Logout Page – This is the page to log out users, a user must be logged in in order to access this page

7)	Add patient details – This is the page for patients to add their medical details and become registered, this page is only accessible for logged in patients
8)	Records – This is the page that shows all the medical details of the patients, this page uses get request to pass in filters for more customized search if the user is a medical practitioners. If the user is a patient it shows the patient’s medical details
9)	Patient Details – This page is only accessible for medical practitioners to view, a specific patients medical details






