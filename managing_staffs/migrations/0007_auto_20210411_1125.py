# Generated by Django 3.1.7 on 2021-04-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing_staffs', '0006_doctor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='others',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]