# Generated by Django 4.2.7 on 2024-02-20 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosfat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plancwiczen',
            name='ilosc_pow',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plancwiczen',
            name='nazwa',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
