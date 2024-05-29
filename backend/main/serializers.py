from rest_framework import serializers
from .models import *


class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorias
        fields = '__all__'
        many = True

class LivrosSerializer(serializers.ModelSerializer):
    categoriaFK = CategoriasSerializer(read_only=True)
    class Meta:
        model = livros
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = emprestimo
        fields = '__all__'
        many = True

class EmprestimoLivroSerializer(serializers.ModelSerializer):
    livroFK = LivrosSerializer
    
    class Meta:
        model = emprestimoLivros
        fields = '__all__'
        many = True

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = autores
        fields = '__all__'
        many = True