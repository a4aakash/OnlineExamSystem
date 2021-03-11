from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from home.models import Contact,AnswerPage
from datetime import datetime

# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect("/")
    return render(request,'index.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'ExamPage.html')
        else:
           return render(request,'login.html')
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")
def about(request):
    return render(request,'about.html')
def Exams(request):
    return render(request,'Exams.html')
def ExamPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        examAnswer = AnswerPage(name=name,roll=roll, phone=phone, desc=desc, date=datetime.today())
        examAnswer.save()
        messages.success(request, 'Your data is uploaded! You may LOGOUT.')
    return render(request, 'ExamPage.html')
def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        registration = request.POST.get('registration')
        branch = request.POST.get('branch')
        roll = request.POST.get('roll')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # desc = request.POST.get('desc')
        examAnswer=Contact(name=name,registration=registration,branch=branch,roll=roll,email=email,phone=phone,date=datetime.today())
        examAnswer.save()
        messages.success(request, 'Registration Successful! Now you can proceed to Exam. BEST OF LUCK!')
    return render(request, 'contact.html')