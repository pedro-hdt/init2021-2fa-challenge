from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import Layer2AuthForm

def default_home_view(request):
    return render(request, 'default-home.html')

class Layer1AuthView(FormView):
    template_name = 'layer1.html'
    form_class = AuthenticationForm
    #success_url = reverse_lazy('core:layer2')

    def form_valid(self, form):
        # TODO send request to bot for layer 2 authentication
        username = self.request.POST['username']
        password = self.request.POST['password']
        self.user_pk = authenticate(self.request, username=username, password=password).pk
        return super().form_valid(form)

    def get_success_url(self):
        # pass user public key on to the layer 2 authentication screen
        return reverse('core:layer2') + '?pk=' + self.user_pk

class Layer2AuthView(FormView):
    template_name = 'layer2.html'
    form_class = Layer2AuthForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        # TODO authenticate the user here and associate it with the session
        return super().form_valid(form)