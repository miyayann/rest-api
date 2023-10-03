from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Task, Post
# Create your views here.


class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = (AllowAny,)
  
  # モデル内のオブジェクトのリストを返すのが主な目的
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    
    #特定のオブジェクトを詳細情報
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    
    # モデル内のオブジェクトのリストを返すのが主な目的
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

    #特定のオブジェクトを詳細情報
class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)
    
# モデルベースのAPIビューを作成するための便利なクラスで、CRUD操作ができる
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer