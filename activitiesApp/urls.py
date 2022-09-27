from django.urls import path
from .views import ActivityCategoryApiList, ActivityCategoryDetailAPI, ActivityListApi, ActivityDetailApi, AddFollowUpApi

urlpatterns = [
    path('follow-up/<int:activity_id>', AddFollowUpApi.as_view()),
    path('categories/', ActivityCategoryApiList.as_view()),
    path('categories/<int:item_id>', ActivityCategoryDetailAPI.as_view()),
    path('', ActivityListApi.as_view()),
    path('<int:item_id>', ActivityDetailApi.as_view()),
]