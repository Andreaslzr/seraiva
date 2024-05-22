from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'categorias',CategoriasView)
router.register(r'livros',LivrosView)
router.register(r'emprestimo',EmprestimoView)

urlpatterns = router.urls