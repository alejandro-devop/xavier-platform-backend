from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from activitiesApp.models import Activity
from .serializer import RoutineStoreSerializer, RoutineSingleSerializer
from .models import Routine


class MyScheduleRoutineDetailApi(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, routine_id, *args, **kwargs):
        instance = Routine.get_object(request.user.id, routine_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exist'
            })
        serializer = RoutineSingleSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, routine_id, *args, **kwargs):
        instance = Routine.get_object(request.user.id, routine_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exist'
            })
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'initial_time': request.data.get('initial_time'),
            'interval': request.data.get('interval'),
            'is_monday': request.data.get('is_monday'),
            'is_tuesday': request.data.get('is_tuesday'),
            'is_wednesday': request.data.get('is_wednesday'),
            'is_thursday': request.data.get('is_thursday'),
            'is_friday': request.data.get('is_friday'),
            'is_saturday': request.data.get('is_saturday'),
            'is_sunday': request.data.get('is_sunday'),
        }
        serializer = RoutineStoreSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                RoutineSingleSerializer(serializer.instance).data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, routine_id, *args, **kwargs):
        instance = Routine.get_object(request.user.id, routine_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exist'
            })
        instance.delete()
        return Response({'removed': True}, status=status.HTTP_200_OK)


class MyScheduleRoutineListApi(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        data = {
            'user': request.user.id,
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'initial_time': request.data.get('initial_time'),
            'interval': request.data.get('interval'),
            'is_monday': request.data.get('is_monday'),
            'is_tuesday': request.data.get('is_tuesday'),
            'is_wednesday': request.data.get('is_wednesday'),
            'is_thursday': request.data.get('is_thursday'),
            'is_friday': request.data.get('is_friday'),
            'is_saturday': request.data.get('is_saturday'),
            'is_sunday': request.data.get('is_sunday'),
        }

        serializer = RoutineStoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                RoutineSingleSerializer(serializer.instance).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
