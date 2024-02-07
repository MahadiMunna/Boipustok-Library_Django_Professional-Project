from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.contrib.auth import login,logout
from django.urls import reverse_lazy


# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'form.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Registration'
        return context

class UserLoginView(LoginView):
    template_name = 'form.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'User Information is incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class Profile(TemplateView):
    template_name = 'profile.html'
    def get(self, request):
        return render(request, self.template_name, None)
    
class UserAccountUpdateView(View):
    template_name = 'form.html'

    def get(self, request):
        form = forms.EditProfile(instance=request.user)
        return render(request, self.template_name, {'form': form, 'type':'Edit Profile'})

    def post(self, request):
        form = forms.EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    

