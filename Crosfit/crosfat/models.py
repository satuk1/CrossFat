from django.db import models
from django.conf import settings
from datetime import datetime

class cwiczenie(models.Model):
    nazwa = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class PlanTreningowy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    waga = models.DecimalField(max_digits=5, decimal_places=2)
    wzrost = models.IntegerField()
    cel = models.CharField(max_length=100)
    wiek = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    PLEC_CHOICES = (
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
    )
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES)
    kcal = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.waga > 0 and self.wzrost > 0:
            wzrost_m = self.wzrost / 100
            self.bmi = self.waga / (wzrost_m * wzrost_m)
        super().save(*args, **kwargs)

    def zapotrzebowanie_kaloryczne(self):
        # Obliczanie zapotrzebowania kalorycznego w zależności od płci, wzrostu, wagi i wieku
        if self.plec == 'M':
            if self.cel == 'utrata-wagi':
                return int((10 * self.waga + 6.25 * self.wzrost - 5 * int(self.wiek) + 5) * 0.85)  # 85% zapotrzebowania dla utraty wagi
            elif self.cel == 'budowa-masy-miesniowej':
                return int((12 * self.waga + 6.25 * self.wzrost - 5 * int(self.wiek) + 500) * 1.2)  # 120% zapotrzebowania dla budowy masy mięśniowej
            elif self.cel == 'poprawa-wytrzymalosci':
                return int((10 * self.waga + 6.25 * self.wzrost - 5 * int(self.wiek) + 5) * 1.1)  # 110% zapotrzebowania dla poprawy wytrzymałości
            else:
                return 0  # Dla innych celów, można ustawić na 0 lub obsłużyć inaczej
        elif self.plec == 'K':
            if self.cel == 'utrata-wagi':
                return int((10 * self.waga + 6.25 * self.wzrost - 5 * int(self.wiek) - 161) * 0.85)  # 85% zapotrzebowania dla utraty wagi
            elif self.cel == 'budowa-masy-miesniowej':
                return int((12 * self.waga + 6.25 * self.wzrost - 5 * int(self.wiek) + 300) * 1.2)  # 120% zapotrzebowania dla budowy masy mięśniowej
            elif self.cel == 'poprawa-wytrzymalosci':
                return int((10 * self.waga + 6.25 * self.wzrost - 5 * int(self.wiek) - 161) * 1.1)  # 110% zapotrzebowania dla poprawy wytrzymałości
            else:
                return 0  # Dla innych celów, można ustawić na 0 lub obsłużyć inaczej

    def oblicz_kcal(self):
        # Obliczanie zapotrzebowania kalorycznego i zapisanie wyniku w polu kcal
        zapotrzebowanie = self.zapotrzebowanie_kaloryczne()
        print(zapotrzebowanie)
        self.kcal = zapotrzebowanie

        return zapotrzebowanie

    def __str__(self):
        return f"Plan treningowy dla wagi: {self.waga} i wzrostu: {self.wzrost}"
