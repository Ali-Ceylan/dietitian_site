# Generated by Django 4.1.7 on 2024-01-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yemekler', '0003_kategori_program_katagori'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
