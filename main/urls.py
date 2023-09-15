from . import views
from django.urls import path
from .views import *

urlpatterns = [
   path('',views.home,name='home'),
   path('education',views.education,name='education'),
   path('cancer_awareness',views.cancer_awareness,name='cancer_awareness'),
   path('contacts',views.contacts,name='contacts'),
   path('book_appointment',views.book_appointment,name='book_appointment'),
   path('download-cv/', views.download_cv, name='download_cv'),
   path('blog', views.PostList.as_view(), name='blog'),
   path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

   

  

]
