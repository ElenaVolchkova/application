# Generated by Django 3.0.3 on 2020-02-22 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200222_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='ward',
        ),
    ]
