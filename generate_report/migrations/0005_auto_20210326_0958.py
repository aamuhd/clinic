# Generated by Django 3.1.4 on 2021-03-26 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generate_report', '0004_auto_20210326_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodglucose',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bloods', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='liverfunctiontest',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='livers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='renalfunctiontest',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='renals', to=settings.AUTH_USER_MODEL),
        ),
    ]
