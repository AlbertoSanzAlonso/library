# Generated by Django 5.1.7 on 2025-03-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_editorial_ciudad_alter_editorial_codigo_postal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='direccion',
            field=models.CharField(default='ejemplo', max_length=300),
            preserve_default=False,
        ),
    ]
