from django.urls import path
from .views import MyScheduleRoutineDetailApi, MyScheduleRoutineListApi

urlpatterns = [
    path('routine', MyScheduleRoutineListApi.as_view()),
    path('routine/<int:routine_id>', MyScheduleRoutineDetailApi.as_view()),
    path('routine/<int:routine_id>/add-activity')
]
