# Generated by Django 4.1 on 2022-12-08 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0003_alter_forum_komenpertama"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="forum",
            name="user",
        ),
        migrations.RemoveField(
            model_name="komen",
            name="user",
        ),
    ]