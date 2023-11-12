from django.urls import path
from .views import GeradorSenhaView, PasswordView

urlpatterns = [
    path('', GeradorSenhaView.as_view(), name='geradorSenha'),
    path('password', PasswordView.as_view(), name='password'),
]