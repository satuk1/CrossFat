# dodaj_dane.py
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crosfit.settings')

django.setup()


from crosfat.models import cwiczenie_utrata_wagi, cwiczenie_budowa_masy_miesniowej, cwiecznie_poprawa_wytrzymalosc
def dodaj_dane():
    # Przykładowe dodawanie danych
    i = 50
    for i in range(100):
        if i < 25:
            cwiczenie_budowa_masy_miesniowej.objects.create(nazwa=f'cwiczenie {i} ', partia='Nogi', ilosc_pow='8')
            cwiecznie_poprawa_wytrzymalosc.objects.create(nazwa=f'cwiczenie {i} ', partia='Nogi', ilosc_pow='8')
            cwiczenie_utrata_wagi.objects.create(nazwa=f'cwiczenie {i} ',partia='Nogi',ilosc_pow='8')
        elif i >= 25 and i < 50:
            cwiczenie_budowa_masy_miesniowej.objects.create(nazwa=f'cwiczenie {i} ', partia='Ramiona', ilosc_pow='12')
            cwiecznie_poprawa_wytrzymalosc.objects.create(nazwa=f'cwiczenie {i} ', partia='Ramiona', ilosc_pow='12')
            cwiczenie_utrata_wagi.objects.create(nazwa=f'cwiczenie {i} ',partia='Ramiona',ilosc_pow='12')
        elif i >= 50 and i < 75:
            cwiczenie_budowa_masy_miesniowej.objects.create(nazwa=f'cwiczenie {i} ', partia='Brzuch', ilosc_pow='15')
            cwiecznie_poprawa_wytrzymalosc.objects.create(nazwa=f'cwiczenie {i} ', partia='Brzuch', ilosc_pow='15')
            cwiczenie_utrata_wagi.objects.create(nazwa=f'cwiczenie {i} ',partia='Brzuch',ilosc_pow='15')
        elif i >= 75 and i < 100:
            cwiczenie_budowa_masy_miesniowej.objects.create(nazwa=f'cwiczenie {i} ', partia='Plecy', ilosc_pow='10')
            cwiecznie_poprawa_wytrzymalosc.objects.create(nazwa=f'cwiczenie {i} ', partia='Plecy', ilosc_pow='10')
            cwiczenie_utrata_wagi.objects.create(nazwa=f'cwiczenie {i} ', partia='Plecy',ilosc_pow='10')
if __name__ == '__main__':
    dodaj_dane()
