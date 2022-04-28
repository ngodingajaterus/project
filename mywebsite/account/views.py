# this views motherfucker
from django.shortcuts import redirect, render
# form import
from .forms import formLogin,formRegister
# django messages
from django.contrib import messages

from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
# fucking decorator login required decorator bitch
from django.utils.decorators import method_decorator


# make the fucking login view
class loginView(LoginView):
    template_name = 'account/login.html'
    next_page = '/admin/'
    redirect_authenticated_user = True
  

# this logoutVIew 
class logoutView(LoginRequiredMixin, LogoutView):
    login_url = '/account/login/'
    template_name = 'account/logout.html'
    next_page = '/'

# this registerVIew 
class registerView(CreateView):
    form_class = formRegister
    template_name = 'account/register.html'
    success_url='/account/login/'
    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully')
        return super().form_valid(form)