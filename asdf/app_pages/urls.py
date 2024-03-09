from django.urls import path


from django.http import HttpResponse


from .views import first,second,third,fourth,fifth,main

urlpatterns = [
    path('page=1/',first,name = 'first'),
    path('page=2/',second,name = 'second'),
    path('page=3/',third,name = 'third'),
    path('page=4/',fourth,name = 'fourth'),
    path('page=5/',fifth,name = 'fifth'),
    path('', main,name = 'main')

]