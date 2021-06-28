from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import default_home_view, Layer1AuthView, Layer2AuthView

app_name = 'core'

urlpatterns = [
    path('', default_home_view, name='home'),
    path('layer1/', Layer1AuthView.as_view(), name='layer1'),
    path('layer2/', Layer2AuthView.as_view(), name='layer2'),
    path('logout/', LoginView.as_view(), name='logout')
]