from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, 'Invalid email or password')
            return redirect('login')

    else:

        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['Username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=name, email=email, password=password1)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password did not match')
            return redirect(signup)
    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return render(request, '/')


def profile(request):
    return render(request, 'profile.html')
