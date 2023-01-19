from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo

def index(request):
    items = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': items})

def add(request):
    todo = request.POST['myplan']
    Todo(plan = todo).save()
    return HttpResponseRedirect(reverse("home"))

def done(request,id):
    myplan = Todo.objects.get(id=id)
    myplan.status = True
    myplan.save()
    return HttpResponseRedirect(reverse("home"))

def delete(request,id):
    myplan = Todo.objects.get(id=id)
    myplan.delete()
    return HttpResponseRedirect(reverse("home"))

def cancel(request,id):
    myplan = Todo.objects.get(id=id)
    myplan.status = False
    myplan.save()
    return HttpResponseRedirect(reverse("home"))    