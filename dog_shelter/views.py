from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from . import forms
from . import models


def animal(request):
    dogs = models.Dog.objects.all()
    return render(request, 'dog_shelter/dog.html', {'dogs': dogs})


# def add_animal(request):
#     dog_form = forms.DogForm
#     if request.method == 'POST':
#         form = forms.DogForm(request.POST)
#         if form.is_valid():
#             print(2)
#             dogs = models.Dog()
#             dogs.name = request.POST.get('name')
#             dogs.egs = request.POST.get('egs')
#             dogs.breed = request.POST.get('breed')
#             dogs.entry_date = request.POST.get('entry_date')
#             dogs.save()
#             return HttpResponseRedirect("/")
#     return render(request, 'dog_shelter/add_dog.html', {"dog_form": dog_form, })


class AnimalCreate(SuccessMessageMixin, CreateView):
    model = models.Dog
    fields = ['name', 'egs', 'breed', 'entry_date']
    template_name = 'dog_shelter/create.html'
    success_url = reverse_lazy('dog:home')
    success_message = 'Животное успешно добавлено'


class AnimalUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Dog
    fields = ['name', 'egs', 'breed', 'entry_date']
    template_name = 'dog_shelter/update.html'
    success_url = reverse_lazy('dog:home')
    success_message = 'Данные успешно изменены'


class AnimalDeleteView(SuccessMessageMixin, DeleteView):
    model = models.Dog
    template_name = 'dog_shelter/delete.html'
    success_url = reverse_lazy('dog:home')
    success_message = 'Данные успешно удалены'
