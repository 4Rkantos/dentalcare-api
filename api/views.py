from rest_framework import generics
from .models import Patient, Procedure, Professional, Appointment, Budget
from .serializers import (
    PatientSerializer, ProcedureSerializer, ProfessionalSerializer,
    AppointmentSerializer, BudgetSerializer
)

# Patients
class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientUpdate(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# Procedure
class ProcedureListCreate(generics.ListCreateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class ProcedureUpdate(generics.RetrieveUpdateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


# Professional
class ProfessionalListCreate(generics.ListCreateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalUpdate(generics.RetrieveUpdateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


# Appointment
class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


# Budget
class BudgetListCreate(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
