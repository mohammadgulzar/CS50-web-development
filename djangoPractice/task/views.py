from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "task/index.html",{
        "tasks":request.session["tasks"]
        #the html will use the variable name on the right
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "tasks/add.html",
            {
                "form":form
            })
    #Get the pages
    return render(request, "task/add.html", 
        {"form": NewTaskForm()})
