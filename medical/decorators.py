from django.shortcuts import redirect, render
from .models import Patient
from django.contrib import messages

def medics_only(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        groups = user.groups.all()
        groups = [group.name for group in groups]

        if "Medic" in groups:
            return func(request, *args, **kwargs)
        else:
            context = {
                "allowed": "eHealth4real registered Medical Practitioners",
                "not_allowed": "Patient"
            }
            return render(request, "access_denied.html", context)

    return wrapper


def medics_only_records(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        groups = user.groups.all()
        groups = [group.name for group in groups]

        if "Medic" in groups:
            return func(request, *args, **kwargs)
        else:
            patient = Patient.objects.get(user=user)
            context = {
                "patient": patient
            }
            return render(request, 'patient_details.html', context)

    return wrapper


def patients_only(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        groups = user.groups.all()
        groups = [group.name for group in groups]

        if "Patient" in groups:
            return func(request, *args, **kwargs)
        else:
            messages.error(request, " That page is only accessible to patients ")
            return redirect('Home')

    return wrapper


def logged_out(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Home')

        return func(request, *args, **kwargs)

    return wrapper
