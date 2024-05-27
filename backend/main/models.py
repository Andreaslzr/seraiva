from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

class UsuarioCustomizado(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
     
    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email   
    
class autores(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.CharField(max_length=1000)
    biografia = models.CharField(max_length=100)

class categorias(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

FORMATO_LIVRO = [
    ("E","E-BOOK"),
    ("F","FISICO"),
]  

class livros(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.CharField(max_length=1000)
    paginas = models.IntegerField()
    descricao = models.CharField(max_length=1000)
    formato = models.CharField(max_length=30, choices=FORMATO_LIVRO)
    n_edicao = models.IntegerField()
    autor = models.CharField(max_length=50)
    ano_pub = models.IntegerField()
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoriaFK = models.ForeignKey(categorias, related_name='livrosCategorias', on_delete=models.CASCADE)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.titulo
    
class emprestimo(models.Model):
    usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='emprestimoUsuario', on_delete=models.CASCADE)
    dataEmprestimo = models.DateField(auto_now_add=True)
    prazo = models.DateField(null=True, blank=True)
    dataDevolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.livroFK.titulo
    
class emprestimoLivros(models.Model):
     livroFK = models.ForeignKey(livros, related_name='emprestimoLivros', on_delete=models.CASCADE)
     quantidade = models.IntegerField()
     emprestimoFK = models.ForeignKey(livros, related_name='emprestimoFK', on_delete=models.CASCADE)

     def __str__(self):
            return self.livroFK.titulo





