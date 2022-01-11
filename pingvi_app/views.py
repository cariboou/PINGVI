from django.shortcuts import redirect, render
from .models import Specialist, Approach, Therapy_session, Client
from .forms import UserLoginForm, UserRegisterForm, ClientForm, TherapySessionForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.mail import message, send_mail

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вход в личный кабинет успешно выполнен')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка входа в личный кабинет')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

def home(request):
    return render(request, 'home.html')

def how_to_start(request):
    return render(request, 'how_to_start.html')

def specialists(request):
    specialists = Specialist.objects.order_by('last_name')
    approachs = Approach.objects.all()
    context = {
        'specialists':specialists,
        'approachs': approachs
    }
    return render(request, 'specialists.html', context=context)

def get_approach(request, approach_id):
    specialists = Specialist.objects.filter(approach_id=approach_id)
    approachs = Approach.objects.all()
    context = {
        'specialists':specialists,
        'approachs': approachs,
    }
    return render(request, 'specialists.html', context=context)

def load_datetimes(request):
    specialist_id = request.GET.get('specialist')
    datetimes = Therapy_session.objects.filter(specialist_id=specialist_id).filter(is_taken=False)
    return render(request, 'load_datetimes.html', {'datetimes': datetimes})

def appointment(request):
    if request.method == 'POST':
        form1 = ClientForm(request.POST)
        form2 = TherapySessionForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            specialist = form2.cleaned_data.get('specialist')
            datetime = form2.cleaned_data.get('datetime')
            therapy_session = Therapy_session.objects.get(specialist_id=specialist, datetime=str(datetime))
            therapy_session.is_taken = True
            if not Client.objects.get(email=request.user.email):
                new_client = Client.objects.create(fist_name=form1.cleaned_data.get('fist_name'), second_name=form1.cleaned_data.get('second_name'), email=request.user.email, number_phone=form1.cleaned_data.get('number_phone'))
                new_client.save()
                therapy_session.client = new_client
            else:
                client = Client.objects.get(email=request.user.email)
                therapy_session.client = client
            therapy_session.save()
            # message = f"Добрый день, {form1.cleaned_data.get('fist_name')}! Вы записаны к {form2.cleaned_data.get('specialist')} на {form2.cleaned_data.get('datetime')}"
            # mail = send_mail(subject='Подтверждение записи от PINGVI', message = message, from_email='olia_9303@mail.ru', recipient_list=[request.user.email], fail_silently=False)
            # if mail:
            messages.success(request, 'Запись на сеанс прошла успешно')
            return redirect('my_appointments')
        else:
            messages.error(request, 'Ошибка отправки формы. Перепроверьте правильность заполнения полей')
    else:
        form1 = ClientForm()
        form2 = TherapySessionForm()
    return render(request, 'appointment.html', {'form1':form1, 'form2':form2})


def my_appointments(request):
    client = Client.objects.filter(email=request.user.email)
    context = {
            'specialists' : [],
            'datetimes' : []
        }
    if len(client) != 0:
        therapy_sessions = Therapy_session.objects.filter(client_id=client[0].id)
        for item in therapy_sessions:
            context['specialists'].append(item.specialist)
            context['datetimes'].append(item.datetime)
    return render(request, 'my_appointments.html', context=context)


