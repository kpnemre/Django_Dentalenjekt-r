# Generated by Django 3.1.6 on 2021-03-18 09:01

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20210318_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Hakkımızda Başlık')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Hakkımızda Resim')),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=250, verbose_name=' Hakkımızda içerik')),
            ],
            options={
                'verbose_name': 'Hakkımızda Bilgi',
                'verbose_name_plural': 'Hakkımızda Bilgiler',
            },
        ),
        migrations.CreateModel(
            name='ProductContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Hakkımızda Başlık')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Hakkımızda Resim')),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=250, verbose_name=' Hakkımızda içerik')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aboutcontent', to='pages.producttitle')),
            ],
            options={
                'verbose_name': 'Hakkımızda Bilgi',
                'verbose_name_plural': 'Hakkımızda Bilgiler',
            },
        ),
    ]