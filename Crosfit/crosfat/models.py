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
    data = datetime.now().date()
    bmi = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.waga > 0 and self.wzrost > 0:
            wzrost_m = self.wzrost / 100
            self.bmi = self.waga / (wzrost_m * wzrost_m)
        super(PlanTreningowy, self).save(*args, **kwargs)

    def __str__(self):
        return f"Plan treningowy dla wagi: {self.waga} i wzrostu: {self.wzrost}"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
from django.contrib.auth.models import AbstractUser

