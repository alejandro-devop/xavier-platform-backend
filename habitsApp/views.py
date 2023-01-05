from rest_framework import permissions, status
from .models import HabitCategory, Habit, HabitMeasures
from .serializers import HabitCategorySerializer, HabitSerializer, HabitListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# ::::::::::::::::::::      Habit category       ::::::::::::::::::::


class HabitCategoryApiList(APIView):
    """
    API to list habit categories and create new ones
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Method to list categories
        """
        categories = HabitCategory.objects.filter(user=request.user.id)
        serializer = HabitCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Method to create a category
        """
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
    """
    API to view, update and remove Habit categories
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        """
        Method to get information for a single habit category
        """
        instance = HabitCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        serializer = HabitCategorySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        """
        Method to update a single category
        """
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
        """
        Method to remove a single habit category
        """
        instance = HabitCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})

        instance.delete()

        return Response({
            'removed': True,
        }, status=status.HTTP_200_OK)


# ::::::::::::::::::::      Habits       ::::::::::::::::::::


class HabitApiList(APIView):
    """API to list habits and create habits"""
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        """
        Method to list habits
        """
        habits = Habit.objects.filter(user=request.user.id)
        serializer = HabitListSerializer(habits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Method to create a habit
        """
        data = {
            'user': request.user.id,
            'activity': request.data.get('activity'),
            'measure': request.data.get('measure'),
            'category': request.data.get('category'),
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'should_avoid': request.data.get('should_avoid'),
            'should_keep': request.data.get('should_keep'),
            'is_counter': request.data.get('is_counter'),
            'is_timer': request.data.get('is_timer'),
            'days': request.data.get('days'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'timer_goal': request.data.get('timer_goal'),
            'times_goal': request.data.get('times_goal'),
        }

        # Check for the measure if it comes and if it  exists
        measure = HabitMeasures.get_object(data['user'], data['measure'])

        if data['measure'] is not None and measure is None:
            print('Its here')
            return Response({
                'error': True,
                'message': 'The entered measure does not exists'
            })
        # Check for the measure if it comes and if it  exists
        category_instance = HabitCategory.get_object(data['user'], data['category'])

        if (data['category'] is not None) and (category_instance is None):
            return Response({
                'error': True,
                'message': 'The entered Category does not exists'
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
            data_serializer = HabitListSerializer(instance=serializer.instance)
            return Response(data_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitApiDetail(APIView):
    """
    Api to view, update and delete habits
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        """
        Method to view habit
        """
        instance = Habit.get_object(request.user.id, item_id)
        if not instance:
            return Response({
                'error': True,
                'message': 'The object does not exists'
            })
        serializer = HabitSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, item_id, *args, **kwargs):
        """
        Method to update habit
        """
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
            'end_date': request.data.get('end_date'),
            'timer_goal': request.data.get('timer_goal'),
            'times_goal': request.data.get('times_goal'),
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
        """
        Method to remove habits
        """
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