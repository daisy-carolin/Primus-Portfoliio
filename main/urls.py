from . import views
from django.urls import path

urlpatterns = [
   path('',views.home,name='home'),
   path('education',views.education,name='education'),
   path('cancer_awareness',views.cancer_awareness,name='cancer_awareness'),
   path('blog',views.blog,name='blog'),
   path('contacts',views.contacts,name='contacts'),
   path('book_appointment',views.book_appointment,name='book_appointment'),
    path('download/<int:file_id>/', views.download_file, name='home'),




]
