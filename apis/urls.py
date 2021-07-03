from django.urls import path
from apis import views

urlpatterns = [
    path('', views.ListView.as_view(), name='tasks'),
    path('create/', views.TodoList.as_view(), name='tasks'),
    path('list/<int:pk>/', views.DetailTodo.as_view()),
]