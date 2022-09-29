from django.urls import path
from todos.models import todos
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('change/<int:pk>',views.change, name='change'),
    path('edit/<int:pk>',views.edit, name='edit'),
    path('update/<int:pk>', views.update, name='update'),
]