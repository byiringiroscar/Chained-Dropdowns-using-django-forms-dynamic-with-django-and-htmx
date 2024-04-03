from django.shortcuts import render
from .models import Course, Module
from .forms import UniversityForm
from django.http.response import HttpResponse

# Create your views here.


def courses(request):
    form = UniversityForm()
    context = {
        'form': form
    }
    return render(request, 'university.html', context)


def modules(request):
    form = UniversityForm(request.GET)

    return HttpResponse(form['modules'])
