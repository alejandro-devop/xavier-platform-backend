from rest_framework import permissions, status
from .models import HabitCategory
from .serializers import HabitCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class HabitCategoryApiList(APIView):
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
        if HabitCategory.it_already_registered(data['name']):
            return Response({
                'error': True,
                'message': 'The category already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        elif not HabitCategory.it_already_registered(data['name']):
            return Response({"content": "Totally new"})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
