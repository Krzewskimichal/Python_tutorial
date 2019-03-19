from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie

from sandbox.forms import LoginForm, RegisterForm, AddBuiltInFunctionForm, AddStringMethodsForm, AddExamForm,\
    AddListMethodsForm, AddDictionaryMethodsForm, AddKeywordsForm, AddSetMethodsForm, AddTupleMethodsForm,  \
    DeleteDataForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from sandbox.models import BuiltInFunction, UserFeature, DictionaryMethods, Keywords, ListMethods, SetMethods, \
    StringMethods, TupleMethods
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.apps import apps


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'start.html', {'form': form})

    def post(self, request):
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
                    request.session['logged'] = True
                    return render(request, 'mainsite.html', {'hello': hello})
            elif user2 is not None:
                if user2.is_active:
                    login(request, user2)
                    request.session['logged'] = True
                    return render(request, 'mainsite.html', {'hello': hello})
            else:
                messages.error(request, 'username or password are not correct')
                return redirect('/start/')
            return redirect('/start/')


def logout_view(request):
    logout(request)
    request.session['logged'] = False
    return redirect('/start/')


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

                send_mail(
                    'Python tutorial',
                    'Thank you for registering',
                    'pythontutorial@gmail.com',
                    [email],
                    fail_silently=False,
                )
                user = authenticate(username=username, password=password1)
                if user.is_active:
                    login(request, user)
                    request.session['logged'] = True
                return redirect('/main/')
        else:
            error = "Passwords are not the same!"
            return render(request, 'start.html', {"error": error})


class MainSiteView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'mainsite.html')


class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'home.html')


class LibraryView(LoginRequiredMixin, View):

    def get(self, request, element):
        if element == 'builtinfunction':
            data = BuiltInFunction.objects.all()
            return render(request, 'built-in-function.html', {'data': data})
        elif element == 'stringmethods':
            data = StringMethods.objects.all()
            return render(request, 'built-in-function.html', {'data': data})
        elif element == 'keywords':
            data = Keywords.objects.all()
            return render(request, 'built-in-function.html', {'data': data})
        elif element == 'dictionarymethods':
            data = DictionaryMethods.objects.all()
            return render(request, 'built-in-function.html', {'data': data})
        elif element == 'listmethods':
            data = ListMethods.objects.all()
            return render(request, 'built-in-function.html', {'data': data})
        elif element == 'tuplemethods':
            data = TupleMethods.objects.all()
            return render(request, 'built-in-function.html', {'data': data})
        elif element == 'setmethods':
            data = SetMethods.objects.all()
            return render(request, 'built-in-function.html', {'data': data})
        else:
            error = 'Error'
            return render(request, 'error.html', {'error': error})


class LessonView(LoginRequiredMixin, View):

    def get(self, request, lesson_number):
        lesson_number = str(lesson_number)
        return render(request, 'lessons/lesson{}.html'.format(lesson_number))


class ExamView(LoginRequiredMixin, View):

    def get(self, request, exam_number):
        exam_number = str(exam_number)
        return render(request, 'exams/exam{}.html'.format(exam_number))


class SearchView(LoginRequiredMixin, View):

    def post(self, request):
        result = []
        lol = request.POST.get('lol')
        if BuiltInFunction.objects.filter(name__iexact=lol):
            result.append(BuiltInFunction.objects.filter(name__iexact=lol))
        elif DictionaryMethods.objects.filter(name__iexact=lol):
            result.append(DictionaryMethods.objects.filter(name__iexact=lol))
        elif Keywords.objects.filter(name__iexact=lol):
            result.append(Keywords.objects.filter(name__iexact=lol))
        elif ListMethods.objects.filter(name__iexact=lol):
            result.append(ListMethods.objects.filter(name__iexact=lol))
        elif SetMethods.objects.filter(name__iexact=lol):
            result.append(SetMethods.objects.filter(name__iexact=lol))
        elif StringMethods.objects.filter(name__iexact=lol):
            result.append(StringMethods.objects.filter(name__iexact=lol))
        elif TupleMethods.objects.filter(name__iexact=lol):
            result.append(TupleMethods.objects.filter(name__iexact=lol))
        else:
            return render(request, 'search.html', {'error': 'No item match your search'})
        return render(request, 'search.html', {'result': result})


class UserView(LoginRequiredMixin, View):

    def get(self, request):
        id = request.user.id
        name = request.user.username
        email = request.user.email
        date = request.user.date_joined
        level = UserFeature.objects.filter(user=id)
        return render(request, 'user.html', {'name': name,
                                             'email': email,
                                             'date': date,
                                             'level': level})


#  -------------------Admin Site--------------------------------
class AdminToolsView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

    def get(self, request):
        return render(request, 'adddata.html')


class DeleteDataView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

    def get(self, request):
        form = DeleteDataForm()
        return render(request, 'add_data/deletedata.html', {'form': form})

    def post(self, request):
        form = DeleteDataForm()
        delete = DeleteDataForm(request.POST)
        if delete.is_valid():
            lol = delete.cleaned_data['database']
            model = apps.get_model("sandbox", lol)
            data = model.objects.all()
            databasename = model.__name__
            return render(request, 'add_data/deletedata.html', {'data': data,
                                                                'form': form,
                                                                'databasename': databasename})


class DeleteRedirectView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

    def post(self, request):
        data = request.POST.get('delete')

        if data == None:
            return render(request, "error.html", {'error': data})
        databasename = request.POST.get('databasename')
        databasename = apps.get_model("sandbox", databasename)
        databasename.objects.filter(pk=data).delete()
        return redirect('/admin/delete_data/')


class AddBuiltInFunctionView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

    def is_admin(self):
        return User.groups.filter(name='Admins').exists()

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


class AddStringMethodsView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

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


class AddListMethodsView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

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


class AddDictionaryMethodsView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

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


class AddTupleMethodsView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

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


class AddSetMethodsView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

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


class AddKeywordsView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

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


class AddExamView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_add_group'

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
