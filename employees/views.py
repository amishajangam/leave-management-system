from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Employee
from .models import Branch
from .forms import BranchForm, EmployeeForm
from leaves.models import Leave
from attendance.models import Attendance
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html') 

def profile(request):

    emp = Employee.objects.filter(
        user=request.user
    ).first()

    if not emp:
        return redirect('/admin/')

    leaves = Leave.objects.filter(employee=emp)

    total = emp.total_leaves
    used = emp.used_leaves
    balance = total - used

    return render(
        request,
        'profile.html',
        {
            'emp': emp,
            'leaves': leaves,
            'total': total,
            'used': used,
            'balance': balance
        }
    )
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')

    return render(request, 'login.html')


def dashboard(request):

    emp = Employee.objects.filter(
        user=request.user
    ).first()

    if not emp:
        return redirect('/admin/')

    if emp.role == 'Admin':

        employees = Employee.objects.all()
        leaves = Leave.objects.all()

        q = request.GET.get('q')
        if q:
            employees = employees.filter(
                user__username__icontains=q
            )

        branch = request.GET.get('branch')
        if branch:
            employees = employees.filter(
                branch__name=branch
            )

        approved = Leave.objects.filter(
            status='Approved'
        ).count()

        rejected = Leave.objects.filter(
            status='Rejected'
        ).count()

        pending = Leave.objects.filter(
            status='Pending'
        ).count()

        present_count = Attendance.objects.filter(
            status='Present'
        ).count()

        absent_count = Attendance.objects.filter(
            status='Absent'
        ).count()

        return render(
            request,
            'dashboard_admin.html',
            {
                'employees': employees,
                'leaves': leaves,
                'approved': approved,
                'rejected': rejected,
                'pending_count': pending,
                'approved_chart': approved,
                'rejected_chart': rejected,
                'pending_chart': pending,
                'present_count': present_count,
                'absent_count': absent_count,
            }
        )

    else:

        leaves = Leave.objects.filter(
            employee=emp
        )

        return render(
            request,
            'dashboard_employee.html',
            {
                'emp': emp,
                'leaves': leaves
            }
        )
        
def employee_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

    return render(request, 'login.html')


def admin_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

    return render(request, 'login.html')   
        
def branch_list(request):

    branches = Branch.objects.all()

    return render(
        request,
        'branch_list.html',
        {
            'branches': branches
        }
    )
# Add Branch
def add_branch(request):

    if request.method == "POST":
        form = BranchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('branch_list')

    else:
        form = BranchForm()

    return render(request, 'branch_form.html', {'form': form})


# Edit Branch
def edit_branch(request, id):

    branch = Branch.objects.get(id=id)

    if request.method == "POST":

        form = BranchForm(request.POST, instance=branch)

        if form.is_valid():
            form.save()
            return redirect('branch_list')

    else:
        form = BranchForm(instance=branch)

    return render(request, 'branch_form.html', {'form': form})


# Delete Branch
def delete_branch(request, id):

    branch = Branch.objects.get(id=id)
    branch.delete()

    return redirect('branch_list')    
# Employee List
def employee_list(request):

    employees = Employee.objects.all()

    search = request.GET.get('search')

    if search:
        employees = employees.filter(
            user__username__icontains=search
        )

    return render(
        request,
        'employee_list.html',
        {
            'employees': employees
        }
    )

# Add Employee
def add_employee(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(
        request,
        'employee_form.html',
        {
            'form': form
        }
    ) 
    
# Edit Employee
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employee_form.html',
        {
            'form': form
        }
    )   
# Delete Employee
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('employee_list')     

def user_logout(request):
    logout(request)
    return redirect('/')        