# Generated by Django 3.0.3 on 2020-04-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ward', '0003_auto_20200405_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
