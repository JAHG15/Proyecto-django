# Generated by Django 4.2 on 2024-10-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crude', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
