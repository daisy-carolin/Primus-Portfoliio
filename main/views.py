from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import UploadFileForm, UploadFileForm2
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic
import os

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def education(request):
    return render(request, 'education.html')

def cancer_awareness(request):
    return render(request, 'cancer_awareness.html')

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


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog_details.html'