from django.shortcuts import render


def root(request):
    return render(request, 'root/index.html', {'Name': 'AlexanderGaganov'})

def ex1_12(request):
    return render(request, 'task-3/ex1.1-12.html')

def ex13(request):
    return render(request, 'task-3/ex1.13.html')

def ex14(request):
    return render(request, 'task-3/ex1.14.html')

def ex15(request):
    return render(request, 'task-3/ex1.15.html')