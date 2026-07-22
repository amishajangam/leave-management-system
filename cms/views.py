from django.shortcuts import render, redirect
from .models import Notice
from .forms import NoticeForm


# Notice List
def notice_list(request):

    notices = Notice.objects.all().order_by('-created_at')

    return render(
        request,
        'notice_list.html',
        {
            'notices': notices
        }
    )


# Add Notice
def add_notice(request):

    if request.method == "POST":

        form = NoticeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('notice_list')

    else:
        form = NoticeForm()

    return render(
        request,
        'notice_form.html',
        {
            'form': form
        }
    )
    
# Edit Notice
def edit_notice(request, id):

    notice = Notice.objects.get(id=id)

    if request.method == "POST":

        form = NoticeForm(
            request.POST,
            request.FILES,
            instance=notice
        )

        if form.is_valid():

            form.save()

            return redirect('notice_list')

    else:

        form = NoticeForm(instance=notice)

    return render(
        request,
        'notice_form.html',
        {
            'form': form
        }
    )


# Delete Notice
def delete_notice(request, id):

    notice = Notice.objects.get(id=id)

    notice.delete()

    return redirect('notice_list')    
