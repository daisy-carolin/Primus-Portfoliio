from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import UploadFileForm, UploadFileForm2
from django.http import HttpResponse
from .models import UploadedFile
import os

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

def download_cv(request):
    cv_file_path = 'static/PRIMUS-OCHIENG-CV.pdf'
    response = FileResponse(open(cv_file_path, 'rb'))
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(cv_file_path)}"'
    return response