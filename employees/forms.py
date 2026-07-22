from django import forms
from .models import Branch, Employee


# ---------------- Branch Form ---------------- #

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name']


# ---------------- Employee Form ---------------- #

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = [
            'user',
            'branch',
            'role',
            'total_leaves',
            'used_leaves'
        ]