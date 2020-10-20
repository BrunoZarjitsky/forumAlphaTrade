from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path("", views.Index, name = "Index"),
    path("enquetes/", views.Enquetes, name = "Enquetes"),
    path("enquetes/<id>", views.EnqueteDetalhe, name = "EnqueteDetalhe")
]