# Generated by Django 4.1.7 on 2024-01-06 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yemekler', '0007_prokategori_program_katego'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='katego',
        ),
        migrations.DeleteModel(
            name='prokategori',
        ),
    ]
