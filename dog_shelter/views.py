from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin

from .models import Dog
from .serializers import AnimalSerializer


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


class AnimalView(APIView):

    def get(self, request):
        dogs = Dog.objects.all()
        serializer = AnimalSerializer(dogs, many=True)
        return Response({'animal': serializer.data})

    def post(self, request):
        dogs = request.data.get('animal')
        serializer = AnimalSerializer(data=dogs)
        if serializer.is_valid(raise_exception=True):
            dogs_save = serializer.save()
        return Response({'success': f'Dogs "{dogs_save.name} add successfully"'})

    def put(self, request, pk):
        saved_animal = get_object_or_404(Dog.objects.all(), pk=pk)
        data = request.data.get('animal')
        serializer = AnimalSerializer(instance=saved_animal, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()

        return Response({
            "success": f"Animal '{animal_saved.name}' updated"
        })

    def delete(self, request, pk):
        animals = get_object_or_404(Dog.objects.all(), pk=pk)
        animals.delete()
        return Response({'message': f"Animals with id {pk} has been deleted"}, status=204)
