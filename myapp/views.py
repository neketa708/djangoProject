from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)
def index(request):
    return HttpResponse("Добро пожаловать на мой первый Django-сайт")


def about(request):
    return HttpResponse("Привет! Я начинающий веб-разработчик. Я увлекаюсь созданием веб-сайтов и разработкой приложений. Сейчас я изучаю Django и очень рад поделиться с вами результатами своего обучения.")
# Create your views here.