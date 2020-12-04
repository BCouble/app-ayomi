from django.conf.urls import url
from django.urls import path

from ayomi.apps.register.views import LoginView, LogoutView, UserCreateView, ProfileDetailView, EmailUpdateView

app_name = 'register'

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='register-form'),
    #path('accounts/login/', auth_views.LoginView.as_view(template_name='register/login.html')),
    url(r'^$', LogoutView.as_view()),
    path('user-add/', UserCreateView.as_view(), name='register-add'),
    path('p/', ProfileDetailView.as_view(), name='mp-list'),
    path('upmail/<int:pk>', EmailUpdateView.as_view(), name='up-email'),
    path('profile/', EmailUpdateView.as_view(), name='m_profile'),
]