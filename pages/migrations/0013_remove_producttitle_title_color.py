# Generated by Django 3.1.6 on 2021-03-23 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_producttitle_title_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttitle',
            name='title_color',
        ),
    ]