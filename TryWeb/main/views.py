from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')   # отрабатывает запуск html файла


def about(request):
    return render(request, 'main/about.html')
