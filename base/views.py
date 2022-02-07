from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .models import Task

# # Create your views here.
# def taskList(request):
#     # return HttpResponse('To do List')

class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields  = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['tasks'] = context ['tasks'].filter(user = self.request.user)
        context ['count'] = context ['tasks'].filter(complete = False).count()

        return context
    
    
class TaskDetail(DetailView):
    model = Task
    
    
class TaskCreate(CreateView):
    model = Task
    # fields = ['title', 'description', 'complete', 'created']
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
    
class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
