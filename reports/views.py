from django.shortcuts import render
from leaves.models import Leave
import pandas as pd
from django.http import HttpResponse
from employees.models import Branch, Employee

def report_view(request):

    branch = request.GET.get('branch')
    department = request.GET.get('department')

    leaves = Leave.objects.all()

    branches = Branch.objects.all()

    departments = Employee.objects.values_list(
        'department',
        flat=True
    ).distinct()

    if branch:
        leaves = leaves.filter(
            employee__branch__name=branch
        )

    if department:
        leaves = leaves.filter(
            employee__department=department
        )

    total = leaves.count()

    approved = leaves.filter(
        status='Approved'
    ).count()

    pending = leaves.filter(
        status='Pending'
    ).count()

    rejected = leaves.filter(
        status='Rejected'
    ).count()

    return render(
        request,
        'report.html',
        {
            'leaves': leaves,
            'branches': branches,
            'departments': departments,
            'total': total,
            'approved': approved,
            'pending': pending,
            'rejected': rejected,
        }
    )
    
    total = leaves.count()



def export_excel(request):

    data = Leave.objects.all().values(
    'employee__user__username',
    'employee__branch__name',
    'leave_type',
    'start_date',
    'end_date',
    'status'
)

    data = list(data)

    df = pd.DataFrame(data)

    response = HttpResponse(
        content_type='application/ms-excel'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename=report.xlsx'

    df.to_excel(response, index=False)

    return response
