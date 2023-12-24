from django.urls import path
from . import views

urlpatterns = [
    path('pessoas/', views.pessoas),
    path('hello', views.hello),
#    path('pessoas/', ),
#    path('', ),
#    path('contagem-pessoas', ),
]
