# dodaj_dane.py
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crosfit.settings')

django.setup()


from crosfat.models import user
def dodaj_dane():
    # Przykładowe dodawanie danych
    user.objects.create(imie='Jan', nazwisko='dipa')

if __name__ == '__main__':
    dodaj_dane()
