# Generated by Django 3.0.3 on 2020-03-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazons', '0004_auto_20200301_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazons',
            name='month_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='amazons',
            name='month_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='amazons',
            name='month_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='amazons',
            name='month_4',
            field=models.BooleanField(default=False),
        ),
    ]
