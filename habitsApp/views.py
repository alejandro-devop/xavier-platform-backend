from rest_framework import permissions, status
from .models import HabitCategory, Habit, HabitMeasures
from .serializers import HabitCategorySerializer, HabitSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# ::::::::::::::::::::      Habit category       ::::::::::::::::::::


class HabitCategoryApiList(APIView):
    """"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """"""
        categories = HabitCategory.objects.filter(user=request.user.id)
        serializer = HabitCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """"""
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'icon': request.data.get('icon'),
            'user': request.user.id
        }
        serializer = HabitCategorySerializer(data=data)
        if HabitCategory.it_already_registered(data['name'], request.user.id):
            return Response({
                'error': True,
                'message': 'The category already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitCategoryApiDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        """"""
        instance = HabitCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        serializer = HabitCategorySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        instance = HabitCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'icon': request.data.get('icon'),
            'user': request.user.id
        }
        serializer = HabitCategorySerializer(instance=instance, data=data, partial=True)

        if HabitCategory.it_already_registered(data['name'], data['user'], instance.id):
            return Response({
                'error': True,
                'message': 'The category already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id, *arg, **kwargs):
        """"""
        instance = HabitCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})

        instance.delete()

        return Response({
            'removed': True,
        }, status=status.HTTP_200_OK)


# ::::::::::::::::::::      Habits       ::::::::::::::::::::


class HabitApiList(APIView):
    """"""
    def get(self, request, *args, **kwargs):
        habits = Habit.objects.filter(user=request.user.id)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.user.id,
            'activity': request.data.get('activity'),
            'measure': request.data.get('measure'),
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'should_avoid': request.data.get('should_avoid'),
            'should_keep': request.data.get('should_keep'),
            'is_counter': request.data.get('is_counter'),
            'is_timer': request.data.get('is_timer'),
            'days': request.data.get('days'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date')
        }

        # Check for the measure if it comes and if it  exists
        measure = HabitMeasures.get_object(data['user'], data['measure'])
        if (data['measure'] is not None) and (measure is None):
            return Response({
                'error': True,
                'message': 'The entered measure does not exists'
            })
        # Todo: Check for the activity if it comes

        # Preparing to save
        serializer = HabitSerializer(data=data)
        # Checking if the habit is not already registered
        if Habit.already_exists(data['name'], data['user']):
            return Response({
                'error': True,
                'message': "The Habit is already registered"
            })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class HabitApiDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        instance = Habit.get_object(request.user.id, item_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exists'
            })
        serializer = HabitSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, item_id, *args, **kwargs):
        instance = Habit.get_object(request.user.id, item_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exists'
            })

        data = {
            'user': request.user.id,
            'activity': request.data.get('activity'),
            'measure': request.data.get('measure'),
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'should_avoid': request.data.get('should_avoid'),
            'should_keep': request.data.get('should_keep'),
            'is_counter': request.data.get('is_counter'),
            'is_timer': request.data.get('is_timer'),
            'days': request.data.get('days'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date')
        }

        serializer = HabitSerializer(instance=instance, data=data)

        if Habit.already_exists(data['name'], data['user'], item_id):
            return Response({
                'error': True,
                'message': 'The habit is already registered'
            })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id, *args, **kwargs):
        instance = Habit.get_object(request.user.id, item_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exists'
            })
        instance.delete()
        return Response({
            'removed': True,
        }, status=status.HTTP_200_OK)