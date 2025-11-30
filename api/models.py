from django.db import models

# Patient
class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
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
    email = models.EmailField()
    cro = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    yearsExperience = models.PositiveIntegerField()
    
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("VACATION", "Vacation"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")

    def __str__(self):
        return self.name


# Appointment
class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)

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
        ("PENDING", "Pending"),
        ("DONE", "Done"),
        ("CANCELLED", "Cancelled"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")

    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
