# Generated by Django 4.2 on 2024-10-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crude', '0003_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='apellido',
            field=models.TextField(blank=True, null=True),
        ),
    ]
