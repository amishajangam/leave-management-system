from django.shortcuts import render, redirect
from .models import Leave
from employees.models import Employee
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

def review_leave(request, id):

    leave = Leave.objects.get(id=id)
    employee = leave.employee

    remaining_leaves = employee.total_leaves - employee.used_leaves

    previous_leaves = Leave.objects.filter(
        employee=employee
    ).order_by('-start_date')

    context = {
        'leave': leave,
        'employee': employee,
        'remaining_leaves': remaining_leaves,
        'previous_leaves': previous_leaves,
    }

    return render(request, 'review_leave.html', context)


def apply_leave(request):

    if request.method == 'POST':

        emp = Employee.objects.filter(
            user=request.user
        ).first()

        if not emp:
            return redirect('/admin/')

        leave = Leave(
            employee=emp,
            leave_type=request.POST['leave_type'],
            start_date=request.POST['start'],
            end_date=request.POST['end'],
            reason=request.POST['reason']
        )

        try:
            leave.full_clean()
            leave.save()

            send_mail(
                'New Leave Request',
                f'''
Employee: {emp.user.username}

Leave Type: {leave.leave_type}

Start Date: {leave.start_date}

End Date: {leave.end_date}

Reason: {leave.reason}
''',
                None,
                ['jangamamisha9@gmail.com'],
                fail_silently=True,
            )

            return redirect('/dashboard/')

        except ValidationError as e:

            return render(
                request,
                'apply.html',
                {
                    'error': str(e)
                }
            )

    return render(request, 'apply.html')


def approve_leave(request, id):

    leave = Leave.objects.get(id=id)

    leave.status = 'Approved'
    leave.save()

    leave.employee.used_leaves += 1
    leave.employee.save()

    send_mail(
        'Leave Approved',
        f'Your leave from {leave.start_date} to {leave.end_date} has been approved.',
        None,
        [leave.employee.user.email],
        fail_silently=True,
    )

    return redirect('/dashboard/')


def reject_leave(request, id):

    leave = Leave.objects.get(id=id)

    leave.status = 'Rejected'
    leave.save()

    send_mail(
        'Leave Rejected',
        f'Your leave from {leave.start_date} to {leave.end_date} has been rejected.',
        None,
        [leave.employee.user.email],
        fail_silently=True,
    )

    return redirect('/dashboard/')

def employee_login(request):
    return render(request, 'login.html', {
        'title': 'Employee Login'
    })


def admin_login(request):
    return render(request, 'login.html', {
        'title': 'Admin Login'
    })
    
def my_leaves(request):

    emp = Employee.objects.filter(
        user=request.user
    ).first()

    if not emp:
        return redirect('/')

    leaves = Leave.objects.filter(
        employee=emp
    ).order_by('-start_date')

    search = request.GET.get('search')

    if search:
        leaves = leaves.filter(
            leave_type__icontains=search
        )

    status = request.GET.get('status')

    if status:
        leaves = leaves.filter(
            status=status
        )

    return render(
        request,
        'my_leaves.html',
        {
            'employee': emp,
            'leaves': leaves
        }
    )