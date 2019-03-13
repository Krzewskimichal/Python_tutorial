from django.shortcuts import render
from django.views import View
from sandbox.forms import LoginForm, RegisterForm, AddBuiltInFunctionForm, AddStringMethodsForm, AddExamForm,\
    AddListMethodsForm, AddDictionaryMethodsForm, AddKeywordsForm, AddSetMethodsForm, AddTupleMethodsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from sandbox.models import BuiltInFunction, UserFeature


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
            hello = 'hello'
            if user1 is not None:
                if user1.is_active:
                    login(request, user1)
                    return render(request, 'mainsite.html', {'hello': hello})
            elif user2 is not None:
                if user2.is_active:
                    login(request, user2)
                    return render(request, 'mainsite.html', {'hello': hello})
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
                Lol = User.objects.create_user(username=username, password=password1, email=email)
                UserFeature.objects.create(user_id=Lol.id)
                return render(request, 'mainsite.html')
            else:
                error = "Passwords are not the same!"
                return render(request, 'register.html', {'error': error})


class MainSiteView(View):

    def get(self, request):
        return render(request, 'mainsite.html')


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class BuiltInFunctionView(View):

    def get(self, request):
        data = BuiltInFunction.objects.all()
        return render(request, 'built-in-function.html', {'data': data})


class LessonView(View):

    def get(self, request, lesson_number):
        lesson_number = str(lesson_number)
        return render(request, 'lessons/lesson{}.html'.format(lesson_number))


class ExamView(View):

    def get(self, request, exam_number):
        exam_number = str(exam_number)
        return render(request, 'exams/exam{}.html'.format(exam_number))


#  -------------------Admin Site--------------------------------
class AdminToolsView(View):

    def get(self, request):
        return render(request, 'adddata.html')


class AddBuiltInFunctionView(View):

    def get(self, request):
        form = AddBuiltInFunctionForm()
        return render(request, 'add_data/builtinfunction.html', {'form': form})

    def post(self, request):
        data = AddBuiltInFunctionForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'add_data/builtinfunction.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'add_data/builtinfunction.html', {'message': message})


class AddStringMethodsView(View):

    def get(self, request):
        form = AddStringMethodsForm()
        return render(request, 'add_data/stringmethods.html', {'form': form})

    def post(self, request):
        data = AddStringMethodsForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'add_data/stringmethods.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'add_data/stringmethods.html', {'message': message})


class AddListMethodsView(View):

    def get(self, request):
        form = AddListMethodsForm()
        return render(request, 'add_data/listmethods.html', {'form': form})

    def post(self, request):
        data = AddListMethodsForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'add_data/listmethods.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'add_data/listmethods.html', {'message': message})


class AddDictionaryMethodsView(View):

    def get(self, request):
        form = AddDictionaryMethodsForm()
        return render(request, 'add_data/dictionarymethods.html', {'form': form})

    def post(self, request):
        data = AddDictionaryMethodsForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'add_data/dictionarymethods.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'add_data/dictionarymethods.html', {'message': message})


class AddTupleMethodsView(View):

    def get(self, request):
        form = AddTupleMethodsForm()
        return render(request, 'add_data/tuplemethods.html', {'form': form})

    def post(self, request):
        data = AddTupleMethodsForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'add_data/tuplemethods.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'add_data/tuplemethods.html', {'message': message})


class AddSetMethodsView(View):

    def get(self, request):
        form = AddSetMethodsForm()
        return render(request, 'add_data/setmethods.html', {'form': form})

    def post(self, request):
        data = AddSetMethodsForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'add_data/setmethods.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'add_data/setmethods.html', {'message': message})


class AddKeywordsView(View):

    def get(self, request):
        form = AddKeywordsForm()
        return render(request, 'add_data/keywords.html', {'form': form})

    def post(self, request):
        data = AddKeywordsForm(request.POST)
        if data.is_valid():
            data.save()
            message = "Data has been added."
            return render(request, 'add_data/keywords.html', {'message': message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'add_data/keywords.html', {'message': message})


class AddExamView(View):

    def get(self, request):
        form = AddExamForm()
        return render(request, 'addexam.html', {'form': form})

    def post(self, request):
        form = AddExamForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Task has been added."
            return render(request, 'addexam.html', {"message": message})
        else:
            message = "Ups! Something gone wrong! Try again."
            return render(request, 'addexam.html', {'message': message})

