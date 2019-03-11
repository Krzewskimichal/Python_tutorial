from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from sandbox.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        error = 'Login Failed'
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user1 = authenticate(username=username, password=password)
            user2 = authenticate(email=username, password=password)
            if user1 is not None:
                if user1.is_active:
                    login(request, user1)
                    return render(request, 'mainsite.html')
            elif user2 is not None:
                if user2.is_active:
                    login(request, user2)
                    return render(request, 'mainsite.html')
            return render(request, 'login.html', {'error': error})


class MainSiteView(View):

    def get(self, request):
        return render(request, 'mainsite.html')

    def post(self, request):
        pass