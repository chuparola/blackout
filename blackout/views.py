from django.shortcuts import render

def index(request):
    return render(
        request,
        'pages/index.html'    
    )

def hacking(request):
    return render(
        request,
        'pages/comprar/hacking.html'    
    )

def verificacao_hacking(request):
    return render(
        request,
        'pages/comprar/verificacao/verificacao_hacking.html'    
    )

def obrigado_hacking(request):
    return render(
        request,
        'pages/comprar/verificacao/obrigado/obrigado_hacking.html'    
    )

def termux(request):
    return render(
        request,
        'pages/comprar/termux.html'    
    )

def verificacao_termux(request):
    return render(
        request,
        'pages/comprar/verificacao/verificacao_termux.html'    
    )

def obrigado_termux(request):
    return render(
        request,
        'pages/comprar/verificacao/obrigado/obrigado_termux.html'    
    )

def ferramentas(request):
    return render(
        request,
        'pages/comprar/ferramentas.html'    
    )

def verificacao_ferramentas(request):
    return render(
        request,
        'pages/comprar/verificacao/verificacao_ferramentas.html'    
    )

def obrigado_ferramentas(request):
    return render(
        request,
        'pages/comprar/verificacao/obrigado/obrigado_ferramentas.html'    
    )

def sobre(request):
    return render(
        request,
        'pages/sobre.html'    
    )

def contato(request):
    return render(
        request,
        'pages/contato.html'    
    )

