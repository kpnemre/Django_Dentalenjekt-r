# Generated by Django 3.1.6 on 2021-03-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210321_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='description_contact',
            field=models.CharField(default=1, max_length=150, verbose_name="İletişim Sayfası için Google'da çıkacak olan yazı"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='keywords_contact',
            field=models.CharField(default=1, max_length=150, verbose_name=" İletişim Sayfası için Google'da aramalarda çıkabilmek için gerekli anahtar kelimler"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.CharField(max_length=150, verbose_name="Google'da çıkacak olan yazı"),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keywords',
            field=models.CharField(max_length=150, verbose_name="Google'da aramalarda çıkabilmek için gerekli anahtar kelimler"),
        ),
    ]
