from rest_framework import permissions, status
from .models import ActivityCategory, Activity, ActivityFollowUp
from .serializers import ActivityCategorySerializer, ActivitySerializer, ActivityListSerializer, ActivityFollowUpListSerializer, ActivityFollowUpSaveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta


class ActivityListApi(APIView):
    """
    API To list, and create a new Activity
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Method to list the activities
        """
        activities = Activity.objects.filter(user=request.user.id)
        serializer = ActivityListSerializer(activities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'color': request.data.get('color'),
            'description': request.data.get('description'),
            'category':  request.data.get('category'),
            'user': request.user.id
        }
        # Check for the measure if it comes and if it  exists
        category = ActivityCategory.get_object(data['user'], data['category'])
        if category is None:
            return Response({
                'error': True,
                'message': 'The entered measure does not exists'
            })

        serializer = ActivitySerializer(data=data)
        if Activity.it_already_registered(data['name'], request.user.id):
            return Response({
                'error': True,
                'message': 'The activity already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            dataSerializer = ActivityListSerializer(serializer.instance)
            return Response(dataSerializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityDetailApi(APIView):
    """
    API to View, Update and Delete activities
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        """
        Method to View a single activity
        """
        instance = Activity.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        serializer = ActivityListSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        """
        Method to update a single activity
        """
        instance = Activity.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})

        data = {
            'name': request.data.get('name'),
            'color': request.data.get('color'),
            'description': request.data.get('description'),
            'category': request.data.get('category'),
            'user': request.user.id
        }

        serializer = ActivitySerializer(instance=instance, data=data, partial=True)
        if Activity.it_already_registered(data['name'], request.user.id, instance.id):
            return Response({
                'error': True,
                'message': 'The item already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            serialized_data = ActivityListSerializer(serializer.instance)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id, *arg, **kwargs):
        """
        Method to remove an activity
        """
        instance = Activity.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})

        instance.delete()

        return Response({
            'removed': True,
        }, status=status.HTTP_200_OK)


class ActivityCategoryApiList(APIView):
    """
    API to list and create Activity categories
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        method to list the categories
        """
        categories = ActivityCategory.objects.filter(user=request.user.id)
        serializer = ActivityCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Method to create a category
        """
        data = {
            'name': request.data.get('name'),
            'color': request.data.get('color'),
            'description': request.data.get('description'),
            'icon':  request.data.get('icon'),
            'is_rest': request.data.get('is_rest'),
            'is_work': request.data.get('is_work'),
            'is_learning': request.data.get('is_learning'),
            'is_self_care': request.data.get('is_self_care'),
            'is_exercise': request.data.get('is_exercise'),
            'is_planning': request.data.get('is_planning'),
            'is_feeding': request.data.get('is_feeding'),
            'is_loving': request.data.get('is_loving'),
            'is_idle': request.data.get('is_idle'),
            'is_driving': request.data.get('is_driving'),
            'is_playing': request.data.get('is_playing'),
            'is_entertainment': request.data.get('is_entertainment'),
            'user': request.user.id
        }
        serializer = ActivityCategorySerializer(data=data)
        if ActivityCategory.it_already_registered(data['name'], request.user.id):
            return Response({
                'error': True,
                'message': 'The category already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityCategoryDetailAPI(APIView):
    """
    API To view, update and delete categories
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        """
        Method to view a category
        """
        instance = ActivityCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        serializer = ActivityCategorySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        """
        Method to update a category
        """
        instance = ActivityCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})

        data = {
            'name': request.data.get('name'),
            'color': request.data.get('color'),
            'description': request.data.get('description'),
            'icon':  request.data.get('icon'),
            'is_rest': request.data.get('is_rest'),
            'is_work': request.data.get('is_work'),
            'is_learning': request.data.get('is_learning'),
            'is_self_care': request.data.get('is_self_care'),
            'is_exercise': request.data.get('is_exercise'),
            'is_planning': request.data.get('is_planning'),
            'is_feeding': request.data.get('is_feeding'),
            'is_loving': request.data.get('is_loving'),
            'is_idle': request.data.get('is_idle'),
            'is_driving': request.data.get('is_driving'),
            'is_playing': request.data.get('is_playing'),
            'is_entertainment': request.data.get('is_entertainment'),
        }

        serializer = ActivityCategorySerializer(instance=instance, data=data, partial=True)
        if ActivityCategory.it_already_registered(data['name'], request.user.id, instance.id):
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
        Method to delete a category
        """
        instance = ActivityCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})

        instance.delete()

        return Response({
            'removed': True,
        }, status=status.HTTP_200_OK)


class FollowUpDayApi(APIView):
    """
    API to get Follow ups between dates
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, day_to_get, *args, **kwargs):
        """
        Method to get the followups between dates
        """
        parsed_date = datetime.strptime(day_to_get, '%Y-%m-%d')
        print(parsed_date.year, parsed_date.month, parsed_date.day)
        follow_ups = ActivityFollowUp.objects.filter(
            user=request.user.id,
            date=datetime(
                parsed_date.year,
                parsed_date.month,
                parsed_date.day
            )
        )
        serializer = ActivityFollowUpListSerializer(follow_ups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddFollowUpApi(APIView):
    """
    API to get A particular Activity's follow ups and to add
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, activity_id, *args, **kwargs):
        """
        Method to add follow ups
        """
        follow_ups = ActivityFollowUp.objects.filter(activity_id=activity_id)
        serializer = ActivityFollowUpListSerializer(follow_ups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, activity_id, *args, **kwargs):
        """
        Method to add new follow up
        """
        data = {
            'date': request.data.get('date'),
            'description': request.data.get('description'),
            'time_spent': request.data.get('time_spent'),
            'user': request.user.id
        }
        activity = Activity.get_object(request.user.id, activity_id)
        if not activity:
            return Response({
                'error': True,
                'message': 'Invalid activity'
            }, status=status.HTTP_400_BAD_REQUEST)
        # Let's update the activity spent time
        activity_data = {}
        # First the global time
        if not activity.spent_time:
            activity_data['spent_time'] = data['time_spent']
        else:
            activity_data['spent_time'] = activity.spent_time + int(data['time_spent'])

        activity_serializer = ActivitySerializer(instance=activity, data=activity_data, partial=True)

        data['activity'] = activity_id
        if request.data.get('started_at'):
            parsed_date = datetime.strptime(request.data.get('started_at'), '%Y-%m-%d %H:%M:%S')
            data['started_date'] = parsed_date
        else:
            data['started_date'] = datetime.today() - timedelta(minutes=int(data['time_spent']))
            print(datetime.today())

        serializer = ActivityFollowUpSaveSerializer(data=data)

        if serializer.is_valid() and activity_serializer.is_valid():
            serializer.save()
            activity_serializer.save()
            data_serializer = ActivityFollowUpListSerializer(serializer.instance)
            return Response(data_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)