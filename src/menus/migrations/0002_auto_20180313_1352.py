# Generated by Django 2.0 on 2018-03-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='contents',
            field=models.TextField(help_text='Seperate each item by comma'),
        ),
        migrations.AlterField(
            model_name='item',
            name='excludes',
            field=models.TextField(blank=True, help_text='Seperate each item by comma', null=True),
        ),
    ]
