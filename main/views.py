from django.shortcuts import render, redirect

from .forms import UploadFileForm, UploadFileForm2
from django.http import HttpResponse
from .models import UploadedFile


# Create your views here.

def home(request):
    return render(request, 'home.html')

def education(request):
    return render(request, 'education.html')

def cancer_awareness(request):
    return render(request, 'cancer_awareness.html')

def blog(request):
    return render(request, 'blog.html')

def contacts(request):
    return render(request, 'contacts.html')

def book_appointment(request):
    return render(request, 'book_appointment.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm2()
    files = UploadedFile.objects.all()
    return render(request, 'home.html', {'form': form, 'files': files})

def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

