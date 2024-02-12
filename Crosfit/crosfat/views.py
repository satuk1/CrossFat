from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm
from .models import PlanTreningowy
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
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
    bmi_list = []
    for plan in plans:
        wzrost_m = float(plan.wzrost) / 100
        bmi = float(plan.waga) / (wzrost_m * wzrost_m)
        bmi_list.append(bmi)
    return render(request, "plan_details.html", {'plans': plans, 'bmi_list': bmi_list})



@login_required
def edit_user(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Aktualizuje hash sesji
            messages.success(request, 'Your password was successfully updated!')
            return redirect('crosfat:user')
    else:
            messages.error(request, 'Please correct the error below.')
            form = PasswordChangeForm(request.user)
    return render(request, 'Edit.html', {'form': form})


# views.py


def abc_view(request):
    return 0;




def submit_training_plan(request):
    if request.method == 'POST':
        waga = float(request.POST.get('waga'))
        wzrost = float(request.POST.get('wzrost'))
        cel = request.POST.get('cel')
        plec = request.POST.get('PLEC')
        wiek = request.POST.get('wiek')
        plan = PlanTreningowy(user=request.user, waga=waga, wzrost=wzrost, cel=cel,
                              plec=plec, wiek=wiek)
        plan.kcal = plan.oblicz_kcal()
        plan.save()
        messages.success(request, 'Twój plan treningowy został zapisany.')

        return redirect('crosfat:plan_details', pk=plan.pk)
    else:
        return render(request, 'create.html')


def lista_planow(request):
    plany = PlanTreningowy.objects.filter(user=request.user)
    return render(request, 'lista_planow.html', {'plany': plany})

# views.py
# views.py
from django.views.generic import DetailView


class PlanDetails(DetailView):
    model = PlanTreningowy
    template_name = 'plan_details.html'  # Twój szablon HTML dla szczegółów planu treningowego
    context_object_name = 'plan'






