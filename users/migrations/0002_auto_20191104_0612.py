# Generated by Django 2.2.6 on 2019-11-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]