# Generated by Django 3.0.3 on 2020-02-23 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_remove_customers_ward'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customers',
        ),
    ]
