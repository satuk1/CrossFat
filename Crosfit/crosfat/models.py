from django.db import models
from django.conf import settings

# Create your models here.


class cwizcenie(models.Model):
    nazwa = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class user(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    haslo = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class PlanTreningowy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    waga = models.DecimalField(max_digits=5, decimal_places=2)
    wzrost = models.IntegerField()
    cel = models.CharField(max_length=100)

    def __str__(self):
        return f"Plan treningowy dla wagi: {self.waga} i wzrostu: {self.wzrost}"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"