from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AdminUsuarioCustomizado(UserAdmin):
    model=UsuarioCustomizado
    list_display = ['id', 'email', 'cpf']
    list_display_links = ('id', 'email', 'cpf',)
    fieldsets = (
        (None,{'fields': ('email','password')}),
        ('Permissions', {'fields': ('is_staff','is_active','groups','user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf','telefone','endereco',)}),
    )
    filter_horizontal = ('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2', 'is_staff','is_active','groups','user_permissions',)
        }),
    )    
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(UsuarioCustomizado,AdminUsuarioCustomizado)

class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(categorias,AdminCategoria)

class AdminLivros(admin.ModelAdmin):
    list_display = ['id', 'titulo']
    list_display_links = ('id', 'titulo',)
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(livros,AdminLivros)

class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['id', 'livroFK','usuarioFK']
    list_display_links = ('id', 'livroFK','usuarioFK')
    search_fields = ('livroFK','usuarioFK')
    list_per_page = 10

admin.site.register(emprestimo,AdminEmprestimo)

