from django.shortcuts import render
from rest_framework import generics
from todo import models
from apis import serializers

from django.views.decorators.csrf import csrf_exempt


# class TodoListView(generics.ListAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializer

class ListView(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class TodoList(generics.CreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
