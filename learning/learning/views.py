from django.shortcuts import render


def root(request):
    return render(request, 'root/index.html', 
                  {'Name': 'AlexanderGaganov',
                   'tasks5': range(1, 11),
                   'tasks7': range(1, 11),
                   'tasks8': range(1, 9),
                   'tasks9': range(1, 5),
                   })

def task8(request, ex_num):
        return render(request, f'task-8/ex{ex_num}.html')
    