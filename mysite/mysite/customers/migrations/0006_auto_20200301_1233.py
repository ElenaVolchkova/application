# Generated by Django 3.0.3 on 2020-03-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='day_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='day_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='day_3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='day_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='day_5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='day_6',
            field=models.BooleanField(default=True),
        ),
    ]
