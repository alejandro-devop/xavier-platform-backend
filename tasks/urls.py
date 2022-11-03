from django.urls import path
from .views import TaskApiList, TaskDetailApi, TaskToggleFlagsApi
urlpatterns = [
    path('', TaskApiList.as_view()),
    path('<int:item_id>', TaskDetailApi.as_view()),
    path('toggle-flags/<int:item_id>', TaskToggleFlagsApi.as_view())
]
