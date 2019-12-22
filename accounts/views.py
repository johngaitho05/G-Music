from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        username = request.POST['username']
        email = request.POST['email']
        if pass1 and pass2 and email and username:
            if pass1 == pass2:
                try:
                    user = User.objects.get(username=username)
                    return render(request,'accounts/signup.html', {'error': "Username is already taken"})
                except User.DoesNotExist:
                    current_user = User.objects.create_user(username=username, password=pass1, email=email)
                    return render(request, 'accounts/login.html',{'message':'Registration successful. Login to continue'})
            return render(request, 'accounts/signup.html', {'error': "Password do not match"})
        return render(request, 'accounts/signup.html', {'error': "Blank field(s) detected!"})
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('music:index')
            else:
                return render(request, 'accounts/login.html', {'error':'Invalid credentials'})
        return render(request, 'accounts/login.html', {'error': 'Blank field(s) detected!'})
    return render(request, 'accounts/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('music:index')


