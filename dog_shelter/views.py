from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Dog


# @permission_required('dog_shelter.add_dog')
def animal(request):
    dogs = Dog.objects.all()
    return render(request, 'dog_shelter/dog.html', {'dogs': dogs})


class AnimalCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'dog_shelter.add_dog'
    model = Dog
    fields = ['name', 'egs', 'breed', 'entry_date']
    template_name = 'dog_shelter/create.html'
    success_url = reverse_lazy('dog:home')
    success_message = 'Животное успешно добавлено'


class AnimalUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'dog_shelter.add_dog'
    model = Dog
    fields = ['name', 'egs', 'breed', 'entry_date']
    template_name = 'dog_shelter/update.html'
    success_url = reverse_lazy('dog:home')
    success_message = 'Данные успешно изменены'


class AnimalDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'dog_shelter.add_dog'
    model = Dog
    template_name = 'dog_shelter/delete.html'
    success_url = reverse_lazy('dog:home')
    success_message = 'Данные успешно удалены'
