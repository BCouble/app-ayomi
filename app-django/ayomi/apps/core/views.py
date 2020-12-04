# ayomi/core/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.models import User
from bootstrap_modal_forms.generic import BSModalUpdateView
from ayomi.apps.core.forms import EmailModelForm
from django.http import JsonResponse

@login_required(login_url='register/', redirect_field_name='')
def index(request):
    return render(request, 'core/index.html')


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(ListView):
    template_name = 'core/profile_list.html'
    model = User

    def get_context_data(self, **kwargs):
        """ Select user information """
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.filter(id=self.request.user.id)
        return context


class EmailUpdateView(BSModalUpdateView):
    model = User
    template_name = 'core/profile_update_email.html'
    form_class = EmailModelForm
    success_message = 'Succès: Email à été modifié.'
    success_url = reverse_lazy('core:mp-list')


def email(request):
    data = dict()
    if request.method == 'GET':
        profile_ajax = User.objects.filter(id=request.user.id)
        data['email'] = render_to_string(
            'core/_profile_up.html',
            {'email': email},
            request=request
        )
        return JsonResponse(data)