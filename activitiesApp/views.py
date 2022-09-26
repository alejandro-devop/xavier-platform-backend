from rest_framework import permissions, status
from .models import ActivityCategory, Activity
from .serializers import ActivityCategorySerializer, ActivitySerializer, ActivityListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ActivityListApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
        print('The category: ', category)
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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        instance = Activity.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        serializer = ActivityListSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
class ActivityCategoryApiList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categories = ActivityCategory.objects.filter(user=request.user.id)
        serializer = ActivityCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id, *args, **kwargs):
        instance = ActivityCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})
        serializer = ActivityCategorySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
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
        """"""
        instance = ActivityCategory.get_object(request.user.id, item_id)
        if not instance:
            return Response({'error': True, 'message': 'The object does not exists'})

        instance.delete()

        return Response({
            'removed': True,
        }, status=status.HTTP_200_OK)