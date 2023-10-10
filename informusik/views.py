from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ik/home.html")

def artistas(request):
    return render(request, "ik/artistas.html")

def musicas(request):
    return render(request, "ik/musicas.html")

def eventos(request):
    return render(request, "ik/eventos.html")

def podcasts(request):
    return render(request, "ik/podcasts.html")

def store(request):
    return render(request, "ik/store.html")

def news(request):
    return render(request, "ik/news.html")