from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import PersonForm
from django.http import JsonResponse

# Create your views here.

@never_cache
def index(request):
    return render(request,'home.html')

@never_cache
@login_required(login_url='login')
def confirm(request):
    return render(request,'confirm.html')

@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid Username or password")
                return redirect('login')
        return render(request,'Login.html')

@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            password2=request.POST.get('password2')
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request,"Username already taken!")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password)
                    messages.info(request, "User Registred Successfully!")
                    user.save()
                    return redirect('login')
            else:
                messages.error(request,"Password Not Matched")
                return redirect('register')
        return render(request,"Register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def person_id(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirm')
        else:
            messages.error(request, form.errors)
    return render(request,'Form.html', {'form': form})


def GetCourses(request):
    department = request.GET['department_id']
    courses = Course.objects.filter(department=department).values()
    return JsonResponse({'success': True,'courses':list(courses),},safe=False)








