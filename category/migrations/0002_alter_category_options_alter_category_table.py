# Generated by Django 5.1.6 on 2025-02-06 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
