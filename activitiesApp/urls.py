from django.urls import path
from .views import ActivityCategoryApiList, ActivityCategoryDetailAPI, ActivityListApi, ActivityDetailApi

urlpatterns = [
    path('categories/', ActivityCategoryApiList.as_view()),
    path('categories/<int:item_id>', ActivityCategoryDetailAPI.as_view()),
    path('', ActivityListApi.as_view()),
    path('<int:item_id>', ActivityDetailApi.as_view()),
]