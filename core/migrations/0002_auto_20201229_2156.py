# Generated by Django 3.1.4 on 2020-12-29 21:56

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='extra_info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='img',
            field=models.ImageField(blank=True, help_text='Image size should be 922x731 px', null=True, upload_to='images', verbose_name='Main Image'),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='file',
            field=models.ImageField(default=django.utils.timezone.now, help_text='Image size is 1900px width and 1267px height', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
