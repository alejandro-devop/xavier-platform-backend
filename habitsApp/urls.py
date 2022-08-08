from django.urls import path
from .views import HabitCategoryApiList, HabitCategoryApiDetail

urlpatterns = [
    path('categories/', HabitCategoryApiList.as_view()),
    path('categories/<int:item_id>', HabitCategoryApiDetail.as_view())
]
