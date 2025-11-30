from rest_framework import generics
from .models import Patient, Procedure, Professional, Schedule, Budget
from .serializers import (
    PatientSerializer, ProcedureSerializer, ProfessionalSerializer,
    ScheduleSerializer, BudgetSerializer
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


# Schedule
class ScheduleListCreate(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleUpdate(generics.RetrieveUpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


# Budget
class BudgetListCreate(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
