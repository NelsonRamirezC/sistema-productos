# Generated by Django 5.1.2 on 2024-10-22 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_alter_producto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('crear_productos', 'Puede crear nuevos productos'), ('productos_vip', 'Puede visualizar exclusivos'))},
        ),
    ]
