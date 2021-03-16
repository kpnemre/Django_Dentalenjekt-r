# Generated by Django 3.1.6 on 2021-03-16 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_about_aboutcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcontent',
            name='about',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='aboutcontent', to='pages.about'),
            preserve_default=False,
        ),
    ]