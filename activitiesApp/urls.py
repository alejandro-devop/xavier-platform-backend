from django.urls import path
from .views import ActivityCategoryApiList, ActivityCategoryDetailAPI

urlpatterns = [
    path('categories/', ActivityCategoryApiList.as_view()),
    path('categories/<int:item_id>', ActivityCategoryDetailAPI.as_view())
]