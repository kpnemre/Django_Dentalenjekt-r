# Generated by Django 3.1.6 on 2021-03-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_aboutcontent_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=50, verbose_name='Hakkımızda Video Linki'),
        ),
    ]