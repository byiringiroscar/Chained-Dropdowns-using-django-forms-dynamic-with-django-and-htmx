from django.shortcuts import render
from .models import Course, Module
from .forms import UniverstiyForm

# Create your views here.


def courses(request):
    form = UniverstiyForm()
    context = {
        'form': form
    }
    return render(request, 'university.html', context)


def modules(request):
    course = request.GET.get('course')
    modules = Module.objects.filter(course=course)

    context  = {
        'modules': modules
    }

    return render(request, 'partials/modules.html', context)
