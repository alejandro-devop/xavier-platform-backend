from rest_framework import permissions, status
from .models import ActivityCategory
from .serializers import ActivityCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response


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