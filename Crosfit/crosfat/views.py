from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm


def home(request):
    return render(request, "home.html")
def Utworz(request):
    return render(request, "Utworz plan.html")
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
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'sign_in.html', {'form': form})


def user_view(request):
    return render(request, 'user.html')

def abc_view(request):
    return 0;