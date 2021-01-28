from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


# Create your models here.
class Medic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute = models.CharField(max_length=200)
    date_created = models.DateField(default=timezone.now())

    def __str__(self):
        return self.user.username


class Disease(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name

    def num_patients(self):
        p = Patient.objects.all()
        pd = Patient.objects.filter(diseases=self)

        return [len(pd), len(p)-len(pd)]  # Returns number of positive and number of negative patients of that disease


class Patient(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=30, default="")
    phone_number = PhoneNumberField(default="")
    diseases = models.ManyToManyField(Disease)
    on_medication = models.BooleanField(default=False)
    occupation = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = PhoneNumberField(default="")
    relationship_to_patient = models.CharField(max_length=200, default="")
    medical_implants = models.BooleanField(default=False)

    date_added = models.DateField(default=timezone.now())
    previous_surgery = models.TextField(default="")
    previous_hospitalized = models.TextField(default="")
    registered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def not_registered(self):
        return not self.registered


