from django import forms


class DogForm(forms.Form):
    name = forms.CharField(label='Имя')
    egs = forms.FloatField(min_value=1, label='Возраст')
    breed = forms.CharField(label='Порода')
    entry_date = forms.DateField(label='Дата поступления')
