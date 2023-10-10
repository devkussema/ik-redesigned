from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("artistas", views.artistas, name="artistas"),
    path("musicas", views.musicas, name="musicas"),
    path("eventos", views.eventos, name="eventos"),
    path("podcasts", views.podcasts, name="podcasts"),
    path("store", views.store, name="store"),
    path("news", views.news, name="news"),
]
