from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

import random


# Create your views here.
# def index_view(request):
#     context = {
#         'first_value': 'Це перше повідомлення',
#         'second_value': f'Ваше випадкове число: {random.randint(1, 100)}',
#         'range': range(1, 21)
#     }
#
#     return render(request, 'main/index.html', context)


class IndexView(TemplateView):
    template_name = 'main/index.html'
    predictions = [
        "Найближчим часом з’явиться новий інтерес, пов’язаний з навчанням або розвитком навичок",
        "Одна зі старих ідей отримає друге життя і почне реально працювати",
        "З’явиться можливість навчити когось тому, що раніше здавалося очевидним",
        "Рутина почне дратувати сильніше, що підштовхне до змін",
        "Буде невеликий, але помітний прогрес у фізичній формі",
        "З’явиться інструмент або технологія, яка значно спростить повсякденні задачі",
        "Одна розмова змінить погляд на знайому ситуацію",
        "Зросте впевненість у власних рішеннях без потреби постійного підтвердження",
        "З’явиться бажання структурувати хаос — списки, плани, системи",
        "Маленький успіх дасть сильніший поштовх, ніж великий результат",
        "Час почне цінуватися більше, ніж раніше",
        "Одна звичка зникне сама собою, без примусу"
    ]
    # extra_context = {}   # простий спосіб доповнення контексту

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # отримали базовий батьківський контекст

        context['prediction'] = random.choice(self.predictions)

        return context


class CustomLoginView(LoginView):
    template_name = 'main/login.html'


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    # success_url = reverse_lazy('login')
    template_name = 'main/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response
