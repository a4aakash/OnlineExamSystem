from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('Exams',views.Exams,name="Exams"),
    path('ExamPage',views.ExamPage,name="ExamPage"),
]