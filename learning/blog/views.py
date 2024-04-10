from django.shortcuts import render


def ex1_12(request):
    return render(request, 'task-3/ex1.1-12.html')

def ex13(request):
    return render(request, 'task-3/ex1.13.html')

def ex14(request):
    return render(request, 'task-3/ex1.14.html')

def ex15(request):
    return render(request, 'task-3/ex1.15.html')

def task4(request):
    return render(request, 'task-4/ex1.1-14.html')

def task5(request, ex_num):
    return render(request, f'task-5/ex{ex_num}.html')

def index(request):
    return render(request, 'index.html')

def task7(request, ex_num):
    return render(request, f'task-7/ex{ex_num}.html', {'sizes': range(1, 4), 'color': "ff0000", 'task10': range(1, 11)})

def task9(request, ex_num):
    return render(request, f'task-9/ex{ex_num}.html')