from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm
from .models import PlanTreningowy
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
def home(request):
    return render(request, "home.html")

def wyloguj(request):
    logout(request)
    return redirect('crosfat:home')
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Użytkownik zalogowany, przekieruj go do widoku 'user'
                return redirect('crosfat:user')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def sign_in_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            return redirect('crosfat:login')
    else:
        form = UserCreationForm()
    return render(request, 'sign_in.html', {'form': form})


def user_view(request):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    return render(request, 'user.html',{'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})
def create(request):
    return render(request, "create.html")
def Plans(request):
    plans = PlanTreningowy.objects.filter(user=request.user)
    return render(request, "Plans.html", {'plans': plans})


def edit_user(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            return redirect('change_user_data')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'edit.html', {'form': form})


# views.py
def user_list(request):
    users = user.objects.all()
    return render(request, 'user_list.html', {'users': users})

def abc_view(request):
    return 0;




def submit_training_plan(request):
    if request.method == 'POST':
        waga = request.POST.get('waga')
        wzrost = request.POST.get('wzrost')
        cel = request.POST.get('cel')
        plan = PlanTreningowy(user=request.user, waga=waga, wzrost=wzrost, cel=cel)
        plan.save()
        messages.success(request, 'Twój plan treningowy został zapisany.')
        return redirect('crosfat:Plans')
    else:
        return render(request, 'create.html')


