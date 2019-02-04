from django.urls import path

from .views import LibroListCBV, AutoreDetailCBV

urlpatterns = [
    path('', LibroListCBV.as_view(), name = 'lista_libri'),
    path('autore/<int:pk>/', AutoreDetailCBV.as_view(), name = 'autore'),
]
