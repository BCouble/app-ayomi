from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView
from ayomi.apps.core.views import ProfileDetailView, EmailUpdateView
from ayomi.apps.core import views

app_name = 'core'

urlpatterns = [
    url(r'^frontend/$', login_required(TemplateView.as_view(template_name='frontend/index.html'))),
    path('', views.index, name='index'),
    path('p/', ProfileDetailView.as_view(), name='mp-list'),
    path('upmail/<int:pk>', EmailUpdateView.as_view(), name='up-email'),
    path('profile/', EmailUpdateView.as_view(), name='m_profile'),
    path('p/email/', views.email, name='email'),
]
