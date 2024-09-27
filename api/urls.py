from django.urls import path, include

from rest_framework import routers

from .viewsets import GeneroViewset, JuegoViewset, PlataformaViewset

router = routers.DefaultRouter()

router.register(r'generos', GeneroViewset)
router.register(r'juegos', JuegoViewset)
router.register(r'plataformas', PlataformaViewset)

urlpatterns = [
    path('', include(router.urls)),
]