# Generated by Django 3.1.2 on 2021-02-19 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_answerpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
    ]
