from django.urls import path

from .views import todo_lists, todo_detail, todo_create, todo_update, todo_delete

app_name = 'todos'

urlpatterns = [
    path('', todo_lists),
    path('create/', todo_create),
    path('update/<id>', todo_update),
    path('delete/<id>', todo_delete),
    path('<id>/', todo_detail),
]