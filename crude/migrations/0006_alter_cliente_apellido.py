# Generated by Django 4.2 on 2024-10-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crude', '0005_alter_cliente_descripcion_alter_cliente_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
    ]