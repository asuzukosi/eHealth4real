from django.urls import path
from . import views

# Set urls for different paths in the program
urlpatterns = [
    path("", views.home, name="Home"),
    path("register", views.register, name="Register"),
    path("register/patient", views.patient_register, name="Register Patient"),
    path("register/medic", views.medic_register, name="Register Medic"),
    path("login", views.login_page, name="Login"),
    path("logout", views.logout_page, name="Logout"),
    path("records", views.records, name="Records"),
    path("records/details/<int:patient_pk>", views.patient_details, name="Patient Details"),
    path("add_patient_details", views.add_patient_details, name="Add Patient Details")
]
