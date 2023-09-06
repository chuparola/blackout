from django.urls import path
from blackout.views import index, hacking, verificacao_hacking, obrigado_hacking, termux, verificacao_termux, obrigado_termux, ferramentas, verificacao_ferramentas, obrigado_ferramentas, sobre, contato

urlpatterns = [
    path('', index, name='index'),
    path('sobre-nós/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('comprar/hacking', hacking, name='hacking'),
    path('comprar/hacking/verificacao', verificacao_hacking, name='verificacao_hacking'),
    path('comprar/hacking/verificacao/obrigado', obrigado_hacking, name='obrigado_hacking'),
    path('comprar/termux', termux, name='termux'),
    path('comprar/termux/verificacao', verificacao_termux, name='verificacao_termux'),
    path('comprar/termux/verificacao/obrigado', obrigado_termux, name='obrigado_termux'),
    path('comprar/ferramentas', ferramentas, name='ferramentas'),
    path('comprar/ferramentas/verificacao', verificacao_ferramentas, name='verificacao_ferramentas'),
    path('comprar/ferramentas/verificacao/obrigado', obrigado_ferramentas, name='obrigado_ferramentas'),
]
