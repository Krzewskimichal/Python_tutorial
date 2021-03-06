from django import forms
from django.forms import ModelForm, TextInput
from sandbox.models import BuiltInFunction, Exams, StringMethods, ListMethods, DictionaryMethods, TupleMethods, \
    Keywords, SetMethods, Messenger


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=128)
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Login', max_length=128)
    password1 = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', max_length=128, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=256)


#  -------------------add data--------------------------------
class AddBuiltInFunctionForm(ModelForm):
    class Meta:
        model = BuiltInFunction
        fields = ['name', 'definition']


class AddStringMethodsForm(ModelForm):
    class Meta:
        model = StringMethods
        fields = ['name', 'definition']


class AddListMethodsForm(ModelForm):
    class Meta:
        model = ListMethods
        fields = ['name', 'definition']


class AddDictionaryMethodsForm(ModelForm):
    class Meta:
        model = DictionaryMethods
        fields = ['name', 'definition']


class AddTupleMethodsForm(ModelForm):
    class Meta:
        model = TupleMethods
        fields = ['name', 'definition']


class AddSetMethodsForm(ModelForm):
    class Meta:
        model = SetMethods
        fields = ['name', 'definition']


class AddKeywordsForm(ModelForm):
    class Meta:
        model = Keywords
        fields = ['name', 'definition']


class AddExamForm(ModelForm):
    class Meta:
        model = Exams
        fields = ['task', 'answer', 'lesson']


class DeleteDataForm(forms.Form):
    databases = (('BuiltInFunction', BuiltInFunction.__name__),
                 ('DictionaryMethods', DictionaryMethods.__name__),
                 ('ListMethods', ListMethods.__name__),
                 ('Keywords', Keywords.__name__),
                 ('SetMethods', SetMethods.__name__),
                 ('StringMethods', StringMethods.__name__),
                 ('TupleMethods', TupleMethods.__name__))

    database = forms.ChoiceField(choices=databases)


class UserWriteMessageForm(ModelForm):
    class Meta:
        model = Messenger
        fields = ['to_user', 'message_title', 'message']
