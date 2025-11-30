from django.urls import path
from .views import (
    PatientListCreate, PatientUpdate,
    ProcedureListCreate, ProcedureUpdate,
    ProfessionalListCreate, ProfessionalUpdate,
    ScheduleListCreate, ScheduleUpdate,
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

    # schedules
    path('schedules/', ScheduleListCreate.as_view()),
    path('schedules/<int:pk>/', ScheduleUpdate.as_view()),

    # Budget
    path('budgets/', BudgetListCreate.as_view()),
    path('budgets/<int:pk>/', BudgetUpdate.as_view()),
]
