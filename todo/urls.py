from django.urls import path

from .views import todo_lists 

app_name = 'todos'

urlpatterns = [
    path('', todo_lists),
]