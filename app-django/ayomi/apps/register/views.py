from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import *
from django.conf import settings
from django.views.generic import TemplateView, ListView, FormView
from ayomi.apps.register.forms import CustomUserCreationForm, EmailModelForm
from django.utils.decorators import method_decorator
from bootstrap_modal_forms.generic import BSModalUpdateView


class LoginView(TemplateView):
    template_name = 'register/register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'register/register.html'

    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)


class UserCreateView(FormView):
    template_name = 'register/register_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register:register-form')

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(ListView):
    template_name = 'register/profile_list.html'
    model = User

    def get_context_data(self, **kwargs):
        """ Select user information """
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.filter(id=self.request.user.id)
        return context


class EmailUpdateView(BSModalUpdateView):
    model = User
    template_name = 'register/profile_update_email.html'
    form_class = EmailModelForm
    success_message = 'Succès: Email à été modifié.'
    success_url = reverse_lazy('register:mp-list')


def email(request):
    data = dict()
    if request.method == 'GET':
        books = Book.objects.all()
        data['table'] = render_to_string(
            '_email_table.html',
            {'email': email},
            request=request
        )
        return JsonResponse(data)