# Generated by Django 5.0.5 on 2024-05-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='avaliacao',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
