from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# Patient
class Patient(models.Model):
    name = models.CharField(max_length=100)

    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message="O CPF deve conter exatamente 11 dígitos numéricos."
            )
        ]
    )

    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    birthDate = models.DateField()
    address = models.CharField(max_length=200)
    medicalHistory = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Procedure
class Procedure(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    durationMinutes = models.PositiveIntegerField()
    specialty = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Professional
class Professional(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    cro = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    yearsExperience = models.PositiveIntegerField()

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("VACATION", "Vacation"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    def __str__(self):
        return self.name


# Schedule
class Schedule(models.Model):
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)

    def clean(self):
        """Validação de horário: fim deve ser após início."""
        if self.endTime <= self.startTime:
            raise ValidationError(
                "O horário de término deve ser maior que o horário de início."
            )

    def save(self, *args, **kwargs):
        # Garante execução da validação antes de salvar
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.patient.name}"


# Budget (Orçamento)
class Budget(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    totalValue = models.DecimalField(max_digits=10, decimal_places=2)
    validUntil = models.DateField()

    STATUS_CHOICES = [
        ("PROCESSING", "Processing"),
        ("PENDING", "Pending"),
        ("DONE", "Done"),
        ("CANCELLED", "Cancelled"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
