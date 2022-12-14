# Generated by Django 4.1 on 2022-10-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('writer', models.CharField(max_length=200, null=True)),
                ('source', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
