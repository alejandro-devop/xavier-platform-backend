from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from activitiesApp.models import ActivityCategory
from rest_framework.response import Response
from datetime import datetime
from .serializers import GoalStoreSerializer, GoalListSerializer
from .models import Goal


class GoalApiList(APIView):
    """
    Api to list and create life goals
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Api to list goals
        """
        return Response(
            GoalListSerializer(Goal.objects.filter(user=request.user.id), many=True).data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        data = {
            'category': request.data.get('category'),
            'user': request.user.id,
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'dead_line_date': request.data.get('dead_line_date')
        }
        category = ActivityCategory.get_object(data['user'], data['category'])
        if category is None:
            return Response({
                'error': True,
                'message': 'The category does not exists'
            })
        if request.data.get('dead_line_date'):
            parsed_date = datetime.strptime(request.data.get('dead_line_date'), '%Y-%m-%d')
            data['dead_line_date'] = parsed_date.date()

        serializer = GoalStoreSerializer(data=data)
        if Goal.is_already_registered(data['name'], data['user']):
            return Response({
                'error': True,
                'message': 'The Goal is already registered'
            })

        if serializer.is_valid():
            serializer.save()
            return Response(
                GoalListSerializer(serializer.instance).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoalDetailApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        instance = Goal.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        return Response(
            GoalListSerializer(instance).data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, item_id, *args, **kwargs):
        instance = Goal.get_object(request.user.id, item_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exits'
            })
        instance.delete()
        return Response({'removed': True}, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        instance = Goal.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The Object does not exists'})

        data = {
            'category': request.data.get('category'),
            'user': request.user.id,
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'dead_line_date': request.data.get('dead_line_date')
        }
        category = ActivityCategory.get_object(data['user'], data['category'])
        if category is None:
            return Response({
                'error': True,
                'message': 'The category does not exists'
            })

        if request.data.get('dead_line_date'):
            parsed_date = datetime.strptime(request.data.get('dead_line_date'), '%Y-%m-%d')
            data['dead_line_date'] = parsed_date.date()
        else:
            data['dead_line_date'] = None

        if Goal.is_already_registered(data['name'], data['user'], item_id):
            return Response({
                'error': True,
                'message': 'Object already exists',
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = GoalStoreSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                GoalListSerializer(serializer.instance).data,
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



