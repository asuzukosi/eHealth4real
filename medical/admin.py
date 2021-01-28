from django.contrib import admin
from .models import Patient, Medic, Disease

# Register your models here.
admin.site.register(Patient)
admin.site.register(Medic)
admin.site.register(Disease)

