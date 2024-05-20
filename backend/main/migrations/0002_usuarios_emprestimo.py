# Generated by Django 5.0.5 on 2024-05-20 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEmprestimo', models.DateField(auto_now_add=True)),
                ('prazo', models.DateField()),
                ('dataDevolucao', models.DateField()),
                ('livroFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimoLivros', to='main.livros')),
                ('usuarioFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimoUsuario', to='main.usuarios')),
            ],
        ),
    ]
