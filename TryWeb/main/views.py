from django.shortcuts import render


def index(request):
    data = {
        'title': 'Технопарк',
        'values': ['Технопарк', '-', 'это', 'люди'],
        'peoples': {
            'staraschuk': 'Yarik',
            'voytenko': 'Ivan',
            'libchuk': 'Ilya'
        }
    }
    return render(request, 'main/index.html', data)   # отрабатывает запуск html файла


def about(request):
    return render(request, 'main/about.html')
