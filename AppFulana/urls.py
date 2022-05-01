from django.urls import path
from AppFulana import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('blog', views.blog, name= "Blog"),
    path('lenguajes', views.lenguajes, name= "Lenguajes"),
    path('institutos', views.instituto, name= "Institutos"),  
    path('acerca', views.acerca, name= "Acerca"),    
    path('buscar/', views.buscar),
]
