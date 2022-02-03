from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task

# # Create your views here.
# def taskList(request):
#     # return HttpResponse('To do List')
    
class TaskList(ListView):
    model = Task