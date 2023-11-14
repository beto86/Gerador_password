from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from django.shortcuts import redirect
from .forms import PasswordParameters
import random

# Create your views here.
class GeradorSenhaView(FormView):
    template_name = 'geradorSenha.html'
    form_class = PasswordParameters
    success_url = 'password'

    def form_valid(self, form):
        length = form.cleaned_data['length']
        uppercase = form.cleaned_data['uppercase']
        number = form.cleaned_data['number']
        special = form.cleaned_data['special']
        redirect_url = reverse('password')
        redirect_url += f'?length={length}&uppercase={uppercase}&number={number}&special={special}'
        #return super().form_valid(form)
        return redirect(redirect_url)

class PasswordView(TemplateView):
    template_name = 'password.html'

    def get_context_data(self, **kwargs):
        context = super(PasswordView, self).get_context_data(**kwargs)
        # Obtenha os parâmetros da URL
        length = self.request.GET.get('length', 12) 
        uppercase = self.request.GET.get('uppercase', False)
        number = self.request.GET.get('number', False)
        special = self.request.GET.get('special', False)
        # Converta os parâmetros para os tipos necessários
        length = int(length)
        uppercase = uppercase.lower() == 'true'
        number = number.lower() == 'true'
        special = special.lower() == 'true'
        # Sua lógica de geração de senha aqui com base nos parâmetros
        characters = list('abcdefghigklmnopqrstuwxyz')
        if uppercase  == True:
            characters.extend('ABCDEFGHIJKLMNOPQRSTUWXYZ')
        if number == True:
            characters.extend('0123456789')
        if special == True:
            characters.extend('/*-.-_!@#$%&:;')
        password = ''
        for x in range(length):
            password += random.choice(characters)
        context['password'] = password
        return context
    

class AboutView(TemplateView):
    template_name = 'about.html'