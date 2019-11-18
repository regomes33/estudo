from django.urls import path


from . views import listarPessoas
from .views import descricao_pessoa

urlpatterns = [
    path('',listarPessoas,name='listarpessoas' ),
    path('descricao/<int:id>',descricao_pessoa, name='descricao_pessoa'),
]