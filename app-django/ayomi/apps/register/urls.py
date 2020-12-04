from django.conf.urls import url

from ayomi.apps.register.views import LoginView, LogoutView

app_name = 'register'

urlpatterns = [
    url(r'^$', LoginView.as_view()),
    #path('accounts/login/', auth_views.LoginView.as_view(template_name='register/login.html')),
    url(r'^$', LogoutView.as_view()),
]
