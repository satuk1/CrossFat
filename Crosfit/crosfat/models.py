from django.db import models

# Create your models here.
class plan_cwiczen(models.Model):
    typ = models.CharField(max_length=100)


class cwizcenie(models.Model):
    nazwa = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


