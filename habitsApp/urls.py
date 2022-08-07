from django.urls import path
from .views import HabitCategoryApiList

urlpatterns = [
    path('categories/', HabitCategoryApiList.as_view()),
]
