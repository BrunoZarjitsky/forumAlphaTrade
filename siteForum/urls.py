from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path("", views.Index, name = "Index"),
    path("enquetes/", views.Enquetes, name = "Enquetes"),
    path("enquetes/<id>", views.EnqueteDetalhe, name = "EnqueteDetalhe"),
    path('accounts/sign_up/',views.sign_up, name="sign-up"),
    path('minhasEnquetes/', views.minhasEnquetes, name = "MinhasEnquetes"),
    path('minhasRespostas/', views.minhasRespostas, name = "MinhasRespostas"),
    path('novaEnquete/', views.novaEnquete, name = "novaEnquete"),
    path('preencherPerfil/', views.preencherPerfil, name = "preencherPerfil"),
]