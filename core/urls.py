from django.urls import path
from .views import GeradorSenhaView, PasswordView, AboutView

urlpatterns = [
    path('', GeradorSenhaView.as_view(), name='geradorSenha'),
    path('password', PasswordView.as_view(), name='password'),
    path('about', AboutView.as_view(), name='about'),
]