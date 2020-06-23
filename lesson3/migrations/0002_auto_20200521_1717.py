# Generated by Django 3.0.4 on 2020-05-21 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='usr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usr',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usr',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usr',
            name='passport',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
