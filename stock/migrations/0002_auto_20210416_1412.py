# Generated by Django 3.1.7 on 2021-04-16 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Karya',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='medicinegiven',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='medicinegiven',
            name='date_updated',
        ),
    ]
