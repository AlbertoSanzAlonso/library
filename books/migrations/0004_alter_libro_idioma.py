# Generated by Django 5.0.7 on 2025-03-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_biografía_autor_biografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='idioma',
            field=models.CharField(choices=[('ES', 'Español'), ('EN', 'Ingles')], default='ES', max_length=2),
        ),
    ]
