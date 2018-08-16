from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from .forms import LoginForm, CreateForm

User = get_user_model()

# Create your views here.
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class Top(LoginRequiredMixin, generic.ListView):
    template_name = 'myapp/top.html'
    context_object_name = 'group_list'
    
    def get_queryset(self):
#        user = self.request.user
        return Group.objects.all()#filter(user=user.pk)
        
class Login(LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'
    
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    model = Group
    form_class = CreateForm
    template_name = 'myapp/create.html'
    success_url = reverse_lazy('myapp:top')
    
    def form_valid(self, form):
        messages.success(self.request, "Saved successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Failed to save")
        return super().form_invalid(form)

class DetailGroup(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'myapp/detail.html'
    context_object_name = 'user_list'
    
    def get_queryset(self):
        group = self.request.build_absolute_uri().split('/')[-2]
        return User.objects.filter(groups__name=str(group))
    
def logged_out(request):
    logout(request)
    return redirect('myapp:login')
