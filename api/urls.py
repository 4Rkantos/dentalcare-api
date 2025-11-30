from django.urls import path
from .views import (
    PatientListCreate, PatientUpdate,
    ProcedureListCreate, ProcedureUpdate,
    ProfessionalListCreate, ProfessionalUpdate,
    AppointmentListCreate, AppointmentUpdate,
    BudgetListCreate, BudgetUpdate,
)

urlpatterns = [
    # Patients
    path('patients/', PatientListCreate.as_view()),
    path('patients/<int:pk>/', PatientUpdate.as_view()),

    # Procedures
    path('procedures/', ProcedureListCreate.as_view()),
    path('procedures/<int:pk>/', ProcedureUpdate.as_view()),

    # Professionals
    path('professionals/', ProfessionalListCreate.as_view()),
    path('professionals/<int:pk>/', ProfessionalUpdate.as_view()),

    # Appointments
    path('appointments/', AppointmentListCreate.as_view()),
    path('appointments/<int:pk>/', AppointmentUpdate.as_view()),

    # Budget
    path('budgets/', BudgetListCreate.as_view()),
    path('budgets/<int:pk>/', BudgetUpdate.as_view()),
]
