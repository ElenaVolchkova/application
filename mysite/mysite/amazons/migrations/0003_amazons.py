# Generated by Django 3.0.3 on 2020-02-23 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ward', '0002_ward_ward'),
        ('amazons', '0002_delete_amazons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amazons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ward.Ward')),
            ],
        ),
    ]
