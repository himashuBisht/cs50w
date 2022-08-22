from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

# tasks = ["foo", "baar", "baz"]


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {"tasks": request.session["tasks"]})


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# to add tasks
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"] += [task]
            # return HttpResponseRedirect('/tasks/')
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})

    return render(request, "tasks/add.html", {"form": NewTaskForm()})
