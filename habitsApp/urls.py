from django.urls import path
from .views import HabitCategoryApiList, HabitCategoryApiDetail, HabitApiList, HabitApiDetail, HabitFollowUpApi

urlpatterns = [
    path('categories/', HabitCategoryApiList.as_view()),
    path('categories/<int:item_id>', HabitCategoryApiDetail.as_view()),
    path('follow-up/<int:habit_id>', HabitFollowUpApi.as_view()),
    path('', HabitApiList.as_view()),
    path('<int:item_id>', HabitApiDetail.as_view())
]
