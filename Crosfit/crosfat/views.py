from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import user
from .forms import UserLoginForm
from django.shortcuts import render
from .forms import EditProfileForm
def home(request):
    return render(request, "home.html")

def wyloguj(request):
    logout(request)
    return redirect('home')
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Użytkownik zalogowany, przekieruj go gdzieś np. do strony głównej
                return redirect('user')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def sign_in_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')
    else:
        form = UserCreationForm()
    return render(request, 'sign_in.html', {'form': form})


def user_view(request):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    return render(request, 'User.html',{'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})
def create(request):
    return render(request, "create.html")
def Plans(request):
    return render(request, "Plans.html")
def Edit(request):
      if request.method == 'POST':
          form = EditProfileForm(request.POST, instance=request.user)
          if form.is_valid():
            form.save()
            return redirect('user.html')
      else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'Edit.html', {'form': form})
# views.py
def user_list(request):
    users = user.objects.all()
    return render(request, 'user_list.html', {'users': users})

def abc_view(request):
    return 0;