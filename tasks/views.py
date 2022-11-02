from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from activitiesApp.models import ActivityCategory
from rest_framework.response import Response
from .serializers import TaskStoreSerializer, TaskListSerializer
from .models import Task
from datetime import datetime


class TaskApiList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'user': request.user.id,
            'category': request.data.get('category'),
            'description': request.data.get('description'),
            'is_urgent': request.data.get('is_urgent'),
            'priority': request.data.get('priority')
        }
        category = ActivityCategory.get_object(data['user'], data['category'])
        if category is None:
            return Response({
                'error': True,
                'message': 'Category does not exists'
            })
        if request.data.get('deadline'):
            pass
        else:
            parsed_date = datetime.strptime(request.data.get('deadline'), '%Y-%m-%d')
            data['date_line'] = parsed_date

        serializer = TaskStoreSerializer(data=data)
        if Task.is_already_registered(data['title'], data['user']):
            return Response({
                'error': True,
                'message': "Task already registered"
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(TaskListSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)



class TaskDetailApi(APIView):
    pass



