from django.urls import path
from . import views

app_name = 'dog'
urlpatterns = [
    path('', views.animal, name='home'),
    # path('add/', views.add_animal),
    path('create/', views.AnimalCreate.as_view(), name='create'),
    path('update/<int:pk>', views.AnimalUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.AnimalDeleteView.as_view(), name='delete'),
    path('api', views.AnimalView.as_view()),
    path('api/<int:pk>', views.AnimalView.as_view())
]
