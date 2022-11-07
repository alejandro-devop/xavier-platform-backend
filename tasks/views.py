from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from activitiesApp.models import ActivityCategory
from rest_framework.response import Response
from .serializers import TaskStoreSerializer, TaskListSerializer
from .models import Task
from datetime import datetime


class TaskToggleFlagsApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, item_id, *args, **kwargs):
        instance = Task.get_object(request.user.id, item_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The task does not exists'
            })
        data = {
            'is_canceled': request.data.get('is_canceled'),
            'is_completed': request.data.get('is_completed')
        }
        serializer = TaskStoreSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                TaskListSerializer(serializer.instance).data,
                status=status.HTTP_200_OK
            )

        return serializer.errors()






class TaskApiList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user.id)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
            parsed_date = datetime.strptime(request.data.get('deadline'), '%Y-%m-%d')
            data['date_line'] = parsed_date.date()
        else:
            pass

        serializer = TaskStoreSerializer(data=data)
        if Task.is_already_registered(data['title'], data['user']):
            return Response({
                'error': True,
                'message': "Task already registered"
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(TaskListSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        instance = Task.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        serializer = TaskListSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        instance = Task.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        data = {
            'title': request.data.get('title'),
            'user': request.user.id,
            'category': request.data.get('category'),
            'description': request.data.get('description'),
            'is_urgent': request.data.get('is_urgent'),
            'is_completed': request.data.get('is_completed'),
            'is_canceled': request.data.get('is_canceled'),
            'priority': request.data.get('priority')
        }

        if request.data.get('deadline'):
            parsed_date = datetime.strptime(request.data.get('deadline'), '%Y-%m-%d')
            data['date_line'] = parsed_date.date()
        else:
            data['date_line'] = None

        serializer = TaskStoreSerializer(instance=instance, data=data, partial=True)

        if Task.is_already_registered(data['title'], request.user.id, instance.id):
            # print('Some: ', data['title'], request.user.id, instance.id)
            return Response({
                'error': True,
                'message': 'Object already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(
                TaskListSerializer(serializer.instance).data,
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id, *args, **kwargs):
        instance = Task.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        instance.delete()

        return Response({'removed': True}, status=status.HTTP_200_OK)



