# Generated by Django 2.2.7 on 2019-11-24 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'default_permissions': ('add', 'delete'), 'permissions': (('give_refund', 'Can refund customers'), ('can_hire', 'Can hire employees'))},
        ),
    ]