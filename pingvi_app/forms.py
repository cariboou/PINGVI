from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from .models import Client, Therapy_session, Specialist


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('fist_name', 'last_name', 'number_phone')
        widgets = {
            'fist_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'number_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TherapySessionForm(forms.Form):
    specialist = forms.ModelChoiceField(empty_label ='Не выбрано',queryset=Specialist.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    datetime = forms.ModelChoiceField(empty_label='Не выбрано',queryset=Therapy_session.objects.filter(is_taken=False), widget=forms.Select(attrs={'class': 'form-control'}))
    # class Meta:
    #     model = Therapy_session
    #     fields = ('specialist', 'datetime')
    #     widgets = {
    #         'specialist': forms.Select(attrs={'class': 'form-control'}),
    #         'datetime': forms.Select(attrs={'class': 'form-control'}),
    #     }

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))