from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login

#Отображение домашней страницы авторизации
def home(request):
    return render(request, 'users/home.html')

#Регистрация пользователя
class Register(View):
    template_name = 'users/register.html'

    #Форма для создания нового пользователя
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    #Обработка формы, создание нового пользователя, вход в систему
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('finance_home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)