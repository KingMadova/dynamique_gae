# Generated by Django 5.1.5 on 2025-03-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="My Freakin' Awesome Blog !", max_length=255),
        ),
    ]
