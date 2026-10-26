from rest_framework import serializers
from .models import TestSession, SensorData, TestResult, MedicationLog

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

class TestSessionSerializer(serializers.ModelSerializer):
    sensor_data = SensorDataSerializer(many=True, read_only=True)
    test_result = TestResultSerializer(read_only=True)

    class Meta:
        model = TestSession
        fields = ['id', 'patient', 'session_date', 'status', 'notes', 'sensor_data', 'test_result']

class MedicationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationLog
        fields = ['id', 'patient', 'medication_name', 'dosage', 'taken_at', 'notes']