from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import input_validators
from .models import Patient, Medic, Disease
from .decorators import medics_only, patients_only, logged_out
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='/login')
def home(request):
    diseases = Disease.objects.all()

    p = Patient.objects.filter(registered=True)
    m = Medic.objects.all()
    d = Disease.objects.all()

    context = {
        "diseases": diseases,
        "no_patients":  len(p),
        "no_medics":  len(m),
        "no_diseases":  len(d),
    }

    user = request.user
    groups = user.groups.all()
    groups = [group.name for group in groups]

    if "Patient" in groups:
        p = Patient.objects.get(user=user)
        if not p.registered:
            messages.error(request, f"Hey {request.user} you have not not entered you medical data, please click on 'Input Data'"
                                    " on the navigation bar to begin. Entering your medical data will "
                                    "help support eHealth4real")

    return render(request, 'home.html', context)


@logged_out
def login_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')

        else:
            messages.error(request, "LOGIN FAILED - check details and try again")
    context = {}
    return render(request, 'login.html', context)


@logged_out
def register(request):
    context = {}
    return render(request, 'register.html', context)


@logged_out
def patient_register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        val = input_validators.validate_all(username, password, firstname, lastname)

        if val != True:
            for error in val:
                messages.error(request, error)
            return render(request, 'register_patient.html', context)

        u = User(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
        u.set_password(password)
        g = Group.objects.get(name='Patient')
        try:
            u.save()
            u.groups.add(g)
            p = Patient(user=u)
            p.save()
            messages.info(request, "Registration Successful - Enter your details to login and begin ")
            return redirect('Login')
        except:
            messages.error(request, "Registration failed")

    return render(request, 'register_patient.html', context)


@logged_out
def medic_register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        institute = request.POST['institute']

        val = input_validators.validate_all(username, password, firstname, lastname)

        if val != True:
            for error in val:
                messages.error(request, error)
            return render(request, 'register_medic.html', context)

        u = User(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
        u.set_password(password)
        g = Group.objects.get(name='Medic')
        try:
            u.save()
            u.groups.add(g)
            m = Medic(user=u, institute=institute)
            m.save()
            messages.info(request, "Registration Successful - Enter your details to login and begin ")
            return redirect('Login')

        except:
            messages.error(request, "Registration failed")
    return render(request, 'register_medic.html', context)


@login_required(login_url='/login')
def logout_page(request):

    logout(request)
    messages.info(request, "You have logged out successfully")
    return redirect('Login')


@login_required(login_url='/login')
@patients_only
def add_patient_details(request):
    p = Patient.objects.get(user=request.user)

    dis = Disease.objects.all()
    context = {
        "diseases": dis,
        "patient": p,
    }
    if request.method == "POST":

        if int(request.POST["age"]) > 0:
            p.age = int(request.POST["age"])
        else:
            p.age = 0

        p.gender = request.POST["gender"]
        p.phone_number = request.POST["phone"]
        p.address = request.POST["address"]
        p.occupation = request.POST["occupation"]
        p.emergency_contact_name = request.POST["emergency_contact_name"]
        p.emergency_contact_phone = request.POST["emergency_contact_phone"]
        p.relationship_to_patient = request.POST["relationship"]
        p.previous_surgery = request.POST["surgery"]
        p.previous_hospitalized = request.POST["hospitalized"]

        for disease in dis:
            if request.POST.get(disease.name, False):
                p.diseases.add(disease)

        if request.POST.get("on_med", False):
            p.on_medication = True

        if request.POST.get("on_imp", False):
            p.medical_implants = True

        p.registered = True
        p.save()
        messages.info(request, "Patient details have successfully been entered. Thank you for supporting eHealth4real.")

        return redirect("Home")

    return render(request, 'add_patient_details.html', context)


@login_required(login_url='/login')
@medics_only
def records(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, 'records.html', context)


@login_required(login_url='/login')
@medics_only
def patient_details(request, patient_pk):

    patient = Patient.objects.get(pk=patient_pk)
    context = {
        "patient": patient
    }
    return render(request, 'patient_details.html', context)
