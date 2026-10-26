from django.contrib import admin
from .models import Patient, TestSession, SensorData, TestResult, MedicationLog

admin.site.register(Patient)
admin.site.register(TestSession)
admin.site.register(SensorData)
admin.site.register(TestResult)
admin.site.register(MedicationLog)