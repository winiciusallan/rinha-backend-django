from django.urls import path
from . import views

urlpatterns = [
    path('pessoas/', views.pessoas),
#    path('pessoas/', ),
#    path('', ),
#    path('contagem-pessoas', ),
]
