from django.urls import path
from .views import MyScheduleRoutineDetailApi, MyScheduleRoutineListApi, AddBlockApi, RemoveBlockApi

urlpatterns = [
    path('routine', MyScheduleRoutineListApi.as_view()),
    path('routine/<int:routine_id>', MyScheduleRoutineDetailApi.as_view()),
    path('routine/<int:routine_id>/add-activity', AddBlockApi.as_view()),
    path('routine/<int:routine_id>/remove-block/<int:block_id>', RemoveBlockApi.as_view())
]
