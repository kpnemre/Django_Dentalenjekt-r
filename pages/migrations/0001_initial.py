# Generated by Django 3.1.6 on 2021-02-16 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Başlık')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('content', models.TextField(blank=True, verbose_name='İçeirk')),
                ('description', models.CharField(max_length=120, verbose_name='Sayfanın search engine açıklaması')),
                ('is_navbar', models.BooleanField(default=True, verbose_name='Navbarda gösterilsin mi?')),
                ('active', models.BooleanField(default=True, verbose_name='Sitede gösterilsin mi?')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Sıralama')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Başlık')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('description', models.CharField(max_length=120, verbose_name='Sayfanın search engine açıklaması')),
                ('keywords', models.CharField(max_length=120, verbose_name='Sayfanın search engine anahtar kelimeleri')),
                ('active', models.BooleanField(default=True, verbose_name='Sitede gösterilsin mi?')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Sıralama')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='pages.header')),
            ],
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='resim')),
                ('short_description', models.CharField(max_length=75, verbose_name='Kısa açıklama')),
                ('content', models.TextField(verbose_name='Açıklama')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
            ],
        ),
    ]
