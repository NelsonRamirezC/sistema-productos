# Generated by Django 5.1.2 on 2024-10-18 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(default='Sin categoría', max_length=50),
        ),
    ]
