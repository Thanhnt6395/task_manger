# Generated by Django 4.1.6 on 2023-03-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.TextField(default=None, verbose_name='username'),
        ),
    ]
