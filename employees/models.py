from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):

    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )
    
    department = models.CharField(
    max_length=100,
    default='IT'
)

    total_leaves = models.IntegerField(default=24)

    used_leaves = models.IntegerField(default=0)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    
    leave_balance = models.IntegerField(
    default=24
)

    def balance(self):
        return self.total_leaves - self.used_leaves

    def __str__(self):
        return self.user.username
    
