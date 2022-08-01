
from django.shortcuts import redirect, render

from .models import Counter

# Create your views here.


def helloworld(request):
    object = Counter.objects.filter(id=1)[0]
    info = {'number': object.number}
    return render(request, 'counter.html', info)


def increment(request):
    # function to increment the number
    object = Counter.objects.filter(id=1)[0]
    object.number = int(object.number) + 1
    object.save()
    return redirect(request.META['HTTP_REFERER'])


def decrement(request):
    # function to decrement the number
    object = Counter.objects.filter(id=1)[0]
    object.number = int(object.number) - 1
    object.save()
    return redirect(request.META['HTTP_REFERER'])


def reset(request):
    # Reset the number to zero
    object = Counter.objects.filter(id=1)[0]
    object.number = 0
    object.save()
    return redirect(request.META['HTTP_REFERER'])
