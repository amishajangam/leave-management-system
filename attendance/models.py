from django.db import models
from employees.models import Employee

class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    STATUS = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    in_time = models.TimeField(
        null=True,
        blank=True
    )

    out_time = models.TimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.employee.user.username} - {self.date}"