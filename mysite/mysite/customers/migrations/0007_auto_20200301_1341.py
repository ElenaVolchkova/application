# Generated by Django 3.0.3 on 2020-03-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20200301_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='day_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='day_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='day_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='day_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='day_5',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='day_6',
            field=models.BooleanField(default=False),
        ),
    ]