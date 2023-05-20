from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


from .models import ToDo

from .serializer import (ToDoSerializer, ToDoCreateSerializer, ToDoUpdateSerializer)

class ToDoListView(APIView):
    def get(self, request: Request):
        query_set= ToDo.objects.all()
        serializer = ToDoSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ToDoCreateView(APIView):
    def post(self, request: Request):
        serializer = ToDoCreateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ToDoUpdateView(APIView):
    def patch(self, request: Request, pk):
        try:
            todo = ToDo.objects.get(pk=pk) # -> ToDo object
        # todo = ToDo.objects.filter(pk=pk) #QuerySet[ToDo Object1, ToDoObject 2...]
        # todo = ToDo.objects.filter(pk=pk).first #QuerySet[ToDo Object1]
        except ToDo.DoesNotExist:
            raise Http404
        serializer = ToDoUpdateSerializer(instance=todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
class ToDoDeleteView(APIView):
    def delete(self, reques:Request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404
        todo.delete()
        return Response({'message':'Deleted'}, status=status.HTTP_204_NO_CONTENT)

class ToDoDetailView(APIView):
    def get(self, request:Request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404
        serializer = ToDoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)


