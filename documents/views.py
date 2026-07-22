import pandas as pd
from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm

def view_excel(request, id):

    file = Document.objects.get(id=id)

    df = pd.read_excel(file.file.path)

    table = df.to_html(
        classes='table table-bordered',
        index=False
    )

    return render(
        request,
        'excel_view.html',
        {
            'table': table,
            'file': file
        }
    )


def documents_page(request):

    if request.method == 'POST':

        form = DocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('/documents/')

    else:
        form = DocumentForm()

    files = Document.objects.all().order_by('-id')

    return render(
        request,
        'documents.html',
        {
            'form': form,
            'files': files
        }
    )
