from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

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
