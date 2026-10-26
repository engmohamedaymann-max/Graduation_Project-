from django.urls import path
from .views import (
    TestSessionListCreateView,
    TestSessionDetailView,
    MedicationLogListCreateView
)

urlpatterns = [
    path('sessions/', TestSessionListCreateView.as_view(), name='session-list-create'),
    path('sessions/<int:pk>/', TestSessionDetailView.as_view(), name='session-detail'),
    path('medications/', MedicationLogListCreateView.as_view(), name='medication-list-create'),
]