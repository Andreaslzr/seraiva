# Generated by Django 5.0.5 on 2024-05-27 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_emprestimolivros'),
    ]

    operations = [
        migrations.CreateModel(
            name='emprestimoLivros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('emprestimoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimoFK', to='main.livros')),
                ('livroFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimoLivros', to='main.livros')),
            ],
        ),
    ]
