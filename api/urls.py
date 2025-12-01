from django.urls import path
from .views import (
    PatientListCreate, PatientDetail,
    ProcedureListCreate, ProcedureDetail,
    ProfessionalListCreate, ProfessionalDetail,
    ScheduleListCreate, ScheduleDetail,
    BudgetListCreate, BudgetDetail,
)

urlpatterns = [
    # Patients
    path('patients/', PatientListCreate.as_view(), name='patients-list'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patients-detail'),

    # Procedures
    path('procedures/', ProcedureListCreate.as_view(), name='procedures-list'),
    path('procedures/<int:pk>/', ProcedureDetail.as_view(), name='procedures-detail'),

    # Professionals
    path('professionals/', ProfessionalListCreate.as_view(), name='professionals-list'),
    path('professionals/<int:pk>/', ProfessionalDetail.as_view(), name='professionals-detail'),

    # Schedules
    path('schedules/', ScheduleListCreate.as_view(), name='schedules-list'),
    path('schedules/<int:pk>/', ScheduleDetail.as_view(), name='schedules-detail'),

    # Budgets
    path('budgets/', BudgetListCreate.as_view(), name='budgets-list'),
    path('budgets/<int:pk>/', BudgetDetail.as_view(), name='budgets-detail'),
]
