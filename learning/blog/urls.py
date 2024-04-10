from django.urls import path
from .views import *


urlpatterns = [
    path('task3/ex1-12', ex1_12),
    path('task3/ex13', ex13),
    path('task3/ex14', ex14),
    path('task3/ex15', ex15),
    path('task4', task4),
    path('task5/ex<int:ex_num>', task5),
    path('', index),
    path('task7/ex<int:ex_num>', task7),
    path('task9/ex<int:ex_num>', task9),
]