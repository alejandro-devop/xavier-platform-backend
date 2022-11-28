from rest_framework import permissions, status
from .models import HabitMeasures
from .serializers import MeasuresSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class HabitMeasureApiList(APIView):
    """
    Api to list and create habit measures
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        """
        Method to list all habit measures list
        """
        measures = HabitMeasures.objects.filter(user=request.user.id)
        serializer = MeasuresSerializer(measures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Method to create a new habit measurement
        """
        data = {
            'user': request.user.id,
            'name': request.data.get('name'),
            'abbreviation': request.data.get('abbreviation')
        }
        serializer = MeasuresSerializer(data=data)
        if HabitMeasures.already_registered(data['name'], data['user']):
            return Response({
                'error': True,
                'message': 'The measure already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitMeasureDetail(APIView):
    """
    Api to view, update and remove habit measurements
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        """
        Method to View habit measurement
        """
        instance = HabitMeasures.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object doest not exists'})

        serializer = MeasuresSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        """
        Method to update a habit measurement
        """
        instance = HabitMeasures.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object doest not exists'})

        data = {
            'user': request.user.id,
            'name': request.data.get('name'),
            'abbreviation': request.data.get('abbreviation')
        }
        serializer = MeasuresSerializer(instance=instance, data=data, partial=True)

        if HabitMeasures.already_registered(data['name'], data['user'], item_id):
            return Response({
                'error': True,
                'message': 'The measure is already registered'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id, *args, **kwargs):
        """
        Method to update a habit measurement
        """
        instance = HabitMeasures.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object doest not exists'})

        instance.delete()
        return Response({
            'removed': True,
        }, status=status.HTTP_200_OK)
