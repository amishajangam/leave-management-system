from django.shortcuts import render
from .models import Attendance

from django.shortcuts import render, redirect
from .forms import AttendanceForm

def attendance_report(request):

    records = Attendance.objects.all()

    return render(
        request,
        'attendance_report.html',
        {
            'records': records
        }
    )
    
# Attendance List
def attendance_list(request):

    records = Attendance.objects.all().order_by('-date')

    search = request.GET.get('search')

    if search:
        records = records.filter(
            employee__user__username__icontains=search
        )

    return render(
        request,
        'attendance_list.html',
        {
            'records': records
        }
    )


# Add Attendance
def add_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm()

    return render(
        request,
        'attendance_form.html',
        {
            'form': form
        }
    )   
    
# Edit Attendance
def edit_attendance(request, id):

    record = Attendance.objects.get(id=id)

    if request.method == "POST":

        form = AttendanceForm(
            request.POST,
            instance=record
        )

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm(instance=record)

    return render(
        request,
        'attendance_form.html',
        {
            'form': form
        }
    )
    
# Delete Attendance
def delete_attendance(request, id):

    record = Attendance.objects.get(id=id)

    record.delete()

    return redirect('attendance_list')         
