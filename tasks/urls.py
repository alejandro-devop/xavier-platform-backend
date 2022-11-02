from django.urls import path
from .views import TaskApiList, TaskDetailApi
urlpatterns = [
    path('', TaskApiList.as_view()),
    path('<int:item_id>', TaskDetailApi.as_view()),
]
