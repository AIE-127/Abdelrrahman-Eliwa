from django.urls import path
from .views import index, detailed_task, tasks_by_status, tasks_by_todo , Createtodo , createCategory , update_task , delete_task

urlpatterns = [
    path('', index, name='home'),
    path('detailed/<int:id>/', detailed_task, name='detail'),
    path('todos/status/<str:status>/', tasks_by_status, name='tasks_by_status'),
    path('todo/<int:todo_id>/', tasks_by_todo, name='todo_tasks'),
    path('todo/create' , Createtodo , name="createtodo"),
    path('categopry/create' , createCategory , name='createcategory' ) ,
    path('todo/update/<int:id>' , update_task , name ="update-task"),
    path('todo/delete/<int:id>' , delete_task , name ="delete-task"),
]
