from django.shortcuts import render


def root(request):
    return render(request, 'root/index.html', {'Name': 'AlexanderGaganov', 'tasks5': range(1, 11), 'tasks7': range(1, 11)})