from django.urls import path
from .views import HabitMeasureApiList, HabitMeasureDetail
urlpatterns = [
    path('habits/measures', HabitMeasureApiList.as_view()),
    path('habits/measures/<int:item_id>', HabitMeasureDetail.as_view()),
]