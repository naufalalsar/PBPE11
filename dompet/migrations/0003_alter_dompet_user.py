# Generated by Django 4.1 on 2022-10-28 02:47n

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dompet', '0002_alter_aruskas_tipe'),
    ]

    operations = [
        migrations.AlterField(
          model_name='dompet',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
