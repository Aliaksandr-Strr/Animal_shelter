from rest_framework import serializers

from .models import Dog


class AnimalSerializer(serializers.Serializer):
    # class Meta:
    #     model = Dog
    #     fields = {'name', 'egs', 'breed', 'entry_date'}
    name = serializers.CharField(max_length=50)
    egs = serializers.FloatField()
    breed = serializers.CharField(max_length=50)
    entry_date = serializers.DateField()

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.egs = validated_data.get('egs', instance.egs)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.entry_date = validated_data.get('entry_date', instance.entry_date)
        instance.save()
        return instance

