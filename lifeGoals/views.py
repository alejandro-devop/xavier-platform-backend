from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from activitiesApp.models import ActivityCategory
from rest_framework.response import Response
from datetime import datetime
from .serializers import GoalStoreSerializer, GoalListSerializer
from .models import Goal


class GoalApiList(APIView):
    permission_classes = [permissions.IsAuthenticated]

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
    pass



