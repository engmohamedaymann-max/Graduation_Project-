from rest_framework import generics
from .models import TestSession, MedicationLog
from .serializers import TestSessionSerializer, MedicationLogSerializer

# APIs الـ Test Sessions
class TestSessionListCreateView(generics.ListCreateAPIView):
    queryset = TestSession.objects.all()
    serializer_class = TestSessionSerializer

class TestSessionDetailView(generics.RetrieveAPIView):
    queryset = TestSession.objects.all()
    serializer_class = TestSessionSerializer

# APIs الـ Medication Logs
class MedicationLogListCreateView(generics.ListCreateAPIView):
    queryset = MedicationLog.objects.all()
    serializer_class = MedicationLogSerializer