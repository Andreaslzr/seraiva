from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class UsuarioCustomizadoView(ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = UsuarioCustomizado.objects.filter(id=user.id)        
        return queryset
    
class CategoriasView(ModelViewSet):
    queryset = categorias.objects.all()
    serializer_class = CategoriasSerializer
    permission_classes = (IsAuthenticated,)

class LivrosView(ModelViewSet):
    queryset = livros.objects.all()
    serializer_class = LivrosSerializer

class EmprestimoView(ModelViewSet):
    queryset = emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoLivroView(ModelViewSet):
    queryset = emprestimoLivros.objects.all()
    serializer_class = EmprestimoLivroSerializer

class AutoresView(ModelViewSet):
    queryset = autores.objects.all()
    serializer_class = AutoresSerializer
