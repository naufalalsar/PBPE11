# Generated by Django 4.1 on 2022-10-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='komenPertama',
            field=models.TextField(blank=True, null=True),
        ),
    ]
