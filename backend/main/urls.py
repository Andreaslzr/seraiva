from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'usuarios',UsuarioCustomizadoView)
router.register(r'categorias',CategoriasView)
router.register(r'livros',LivrosView)
router.register(r'autores',AutoresView)
router.register(r'emprestimo',EmprestimoView)
router.register(r'emprestimo-livros',EmprestimoLivroView)

urlpatterns = router.urls