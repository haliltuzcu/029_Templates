from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello World!</h1>')


def student(request):
    context = {
        'first_name':'rafe',
        'my_list': [2020, 2021, 2022],
        'book_name':'lord of the rings'
        }
    return render(request, 'home/home.html', context)

def student_detail(request):
    return render(request, 'home/student_detail.html')