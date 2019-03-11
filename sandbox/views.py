from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from sandbox.forms import LoginForm, RegisterForm, AddDataForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from sandbox.models import BuiltInFunction


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
                    hello = "hello"
                    return render(request, 'mainsite.html', {'hello': hello})
            elif user2 is not None:
                if user2.is_active:
                    login(request, user2)
                    return render(request, 'mainsite.html')
            return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    bye = 'Logout'
    return render(request, 'mainsite.html', {'bye': bye})


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if password1 == password2:
                User.objects.create(username=username, password=password1, email=email)
                return render(request, 'mainsite.html')
            else:
                error = "Passwords are not the same!"
                return render(request, 'register.html', {'error': error})


class MainSiteView(View):

    def get(self, request):
        return render(request, 'mainsite.html')


class BuiltInFunctionView(View):

    def get(self, request):
        data = BuiltInFunction.objects.all()
        return render(request, 'built-in-function.html', {'data': data})


#  -------------------Admin Site--------------------------------
class AddDataView(View):

    def get(self, request):
        data = AddDataForm()
        return render(request, 'adddata.html', {'data': data})

    def post(self, request):
        data = AddDataForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'adddata.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'adddata.html', {'message': message})
