# Generated by Django 5.1.2 on 2024-10-22 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_alter_producto_precio_alter_producto_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('crear_productos', 'Puede crear nuevos productos'),)},
        ),
    ]
