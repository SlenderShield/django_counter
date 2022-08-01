from django.shortcuts import render

# Create your views here.


def helloworld(request):
    info = {'name': "Muralidhara", 'age': 22}
    return render(request, 'helloworld/helloworld.html', info)


def increment(request):
    return
