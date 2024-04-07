from django.shortcuts import render
from .models import UFrm,UserForm
from django.views.generic import CreateView,FormView,UpdateView,DeleteView,ListView
# Create your views here.
def home(request):
    return render(request,'home.html')

class frm(FormView):
    form_class=UserForm
    template_name='home.html'


class Add(CreateView):
    model=UFrm
    fields='__all__'
    success_url='/'

class List(ListView):
    model=UFrm
    template_name='home.html'

class Update(UpdateView):
    model=UFrm
    fields='__all__'
    template_name='up.html'
    success_url='/'

class Delete(DeleteView):
    model=UFrm
    template_name='del.html'
    success_url='/'