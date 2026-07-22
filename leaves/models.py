from django.db import models
from employees.models import Employee
from django.core.exceptions import ValidationError


class Leave(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Cancelled', 'Cancelled'),
    )
    
    LEAVE_TYPES = (
        ('Casual', 'Casual'),
        ('Sick', 'Sick'),
        ('WFH', 'Work From Home'),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    
    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPES,
        default='Casual'
    )

    start_date = models.DateField()

    end_date = models.DateField()
    
    
    reason = models.TextField(
    blank=True,
    null=True
)


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    
    admin_remark = models.TextField(
    blank=True,
    null=True
)
    
    def clean(self):

        if self.end_date < self.start_date:

            raise ValidationError(
                "End date cannot be before Start date"
            )

    def __str__(self):
        return self.employee.user.username
