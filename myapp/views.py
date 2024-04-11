from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная")


def about(request):
    return HttpResponse("Привет! Меня зовут [ваше имя] и я начинающий веб-разработчик. Я увлекаюсь созданием веб-сайтов и разработкой приложений. Сейчас я изучаю Django и очень рад поделиться с вами результатами своего обучения.")
# Create your views here.