# Generated by Django 3.1.6 on 2021-03-17 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_home_navmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['order'], 'verbose_name': 'AnaSayfa Ana İçerikler ', 'verbose_name_plural': 'AnaSayfa Ana İçerik '},
        ),
    ]
