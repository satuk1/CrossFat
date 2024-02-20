
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, get_object_or_404
from .models import PlanTreningowy, PlanCwiczen, cwiczenie_utrata_wagi, cwiczenie_budowa_masy_miesniowej, cwiecznie_poprawa_wytrzymalosc
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

        return redirect('crosfat:Gen_pl', plan_id=plan.pk)
    else:
        return render(request, 'create.html')

def gen_pl(request, plan_id):
    plan = get_object_or_404(PlanTreningowy, pk=plan_id)
    if plan.cel == 'utrata-wagi':
        lista_cwiczen_dzien1 = cwiczenie_utrata_wagi.objects.filter(partia='Nogi')
        lista_cwiczen_dzien2 = cwiczenie_utrata_wagi.objects.filter(partia='Ramiona')
        lista_cwiczen_dzien3 = cwiczenie_utrata_wagi.objects.filter(partia__in=['Brzuch', 'Plecy'])
    elif plan.cel == 'budowa-masy-miesniowej':
        lista_cwiczen_dzien1 = cwiczenie_budowa_masy_miesniowej.objects.filter(partia='Nogi')
        lista_cwiczen_dzien2 = cwiczenie_budowa_masy_miesniowej.objects.filter(partia='Ramiona')
        lista_cwiczen_dzien3 = cwiczenie_budowa_masy_miesniowej.objects.filter(partia__in=['Brzuch', 'Plecy'])
    elif plan.cel == 'poprawa-wytrzymalosci':
        lista_cwiczen_dzien1 = cwiecznie_poprawa_wytrzymalosc.objects.filter(partia='Nogi')
        lista_cwiczen_dzien2 = cwiecznie_poprawa_wytrzymalosc.objects.filter(partia='Ramiona')
        lista_cwiczen_dzien3 = cwiecznie_poprawa_wytrzymalosc.objects.filter(partia__in=['Brzuch', 'Plecy'])
    else:
        lista_cwiczen_dzien1 = []
        lista_cwiczen_dzien2 = []
        lista_cwiczen_dzien3 = []

    return render(request, 'gen_pl.html', {'plan': plan, 'lista_cwiczen_dzien1': lista_cwiczen_dzien1,
        'lista_cwiczen_dzien2': lista_cwiczen_dzien2,
        'lista_cwiczen_dzien3': lista_cwiczen_dzien3,})


def lista_planow(request):
    plany = PlanTreningowy.objects.filter(user=request.user)
    return render(request, 'lista_planow.html', {'plany': plany})

# views.py
# views.py
from django.views.generic import DetailView


class PlanDetails(DetailView):
    model = PlanTreningowy
    template_name = 'plan_details.html'
    context_object_name = 'plan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plan_treningowy = self.object
        cwiczenia_po_dniach = {}
        for dzien in range(1, 4):
            cwiczenia_w_dniu = PlanCwiczen.objects.filter(plan_treningowy=plan_treningowy, dzien=dzien)
            cwiczenia_po_dniach[dzien] = cwiczenia_w_dniu
        context['cwiczenia_po_dniach'] = cwiczenia_po_dniach
        return context

def zapisz_cwiczenia_do_planu(request, plan_id):
    plan = get_object_or_404(PlanTreningowy, pk=plan_id)

    if request.method == 'POST':
        PlanCwiczen.objects.filter(plan_treningowy=plan).delete()

        for dzien in range(1, 4):
            cwiczenia_ids = request.POST.getlist(f'cwiczeniaDzien{dzien}')
            if not cwiczenia_ids:
                continue
            for cwiczenie_id in cwiczenia_ids:
                if not cwiczenie_id:
                    continue  # Pomijamy puste ID

                # Tworzymy obiekt PlanCwiczen dla każdego wybranego ćwiczenia
                if plan.cel == 'utrata-wagi':
                    cwiczenie = get_object_or_404(cwiczenie_utrata_wagi, pk=cwiczenie_id)
                    PlanCwiczen.objects.create(plan_treningowy=plan, cwiczenie_utrata_wagi=cwiczenie, dzien=dzien)
                elif plan.cel == 'budowa-masy-miesniowej':
                    cwiczenie = get_object_or_404(cwiczenie_budowa_masy_miesniowej, pk=cwiczenie_id)
                    PlanCwiczen.objects.create(plan_treningowy=plan, cwiczenie_budowa_masy_miesniowej=cwiczenie, dzien=dzien)
                elif plan.cel == 'poprawa-wytrzymalosci':
                    cwiczenie = get_object_or_404(cwiecznie_poprawa_wytrzymalosc, pk=cwiczenie_id)
                    PlanCwiczen.objects.create(plan_treningowy=plan, cwiczenie_poprawa_wytrzymalosci=cwiczenie, dzien=dzien)

        messages.success(request, 'Ćwiczenia zostały zapisane.')
        return redirect('crosfat:plan_details', pk=plan_id)

    return redirect('crosfat:gen_pl', plan_id=plan_id)





