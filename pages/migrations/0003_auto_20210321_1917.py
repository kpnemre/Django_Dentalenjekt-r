# Generated by Django 3.1.6 on 2021-03-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210318_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.CharField(default=1, max_length=150, verbose_name="Google'da çıkacak olan yazı"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttitle',
            name='description',
            field=models.CharField(default=1, max_length=150, verbose_name="Google'da çıkacak olan yazı"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(default=1, max_length=150, verbose_name="Google'da çıkacak olan yazı"),
            preserve_default=False,
        ),
    ]
