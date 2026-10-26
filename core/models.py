from django.db import models
from django.contrib.auth.models import User

# جدول المريض (المرجع الأساسي لربط البيانات)
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Patient {self.id} - {self.user.username}"


# 1. جدول الجلسات (TestSessions)
class TestSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='test_sessions')
    session_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='completed')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Session {self.id} for Patient {self.patient.id}"


# 2. جدول قراءات الحساسات (SensorData)
class SensorData(models.Model):
    session = models.ForeignKey(TestSession, on_delete=models.CASCADE, related_name='sensor_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    accelerometer_x = models.FloatField()
    accelerometer_y = models.FloatField()
    accelerometer_z = models.FloatField()
    gyroscope_x = models.FloatField(blank=True, null=True)
    gyroscope_y = models.FloatField(blank=True, null=True)
    gyroscope_z = models.FloatField(blank=True, null=True)


# 3. جدول نتيجة الاختبار (TestResults)
class TestResult(models.Model):
    session = models.OneToOneField(TestSession, on_delete=models.CASCADE, related_name='test_result')
    tremor_score = models.FloatField()
    bradykinesia_score = models.FloatField(blank=True, null=True)
    overall_severity = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


# 4. جدول سجل الأدوية (MedicationLogs)
class MedicationLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medication_logs')
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    taken_at = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.medication_name} - Patient {self.patient.id}"