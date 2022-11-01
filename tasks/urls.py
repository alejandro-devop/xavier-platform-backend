from django.urls import path
from .views import TaskCategoryApiList, TaskCategoryDetailApi, TaskApiList, TaskDetailApi
urlpatterns = [
    path('categories/', TaskCategoryApiList.as_view()),
    path('categories/<int:item_id>', TaskCategoryDetailApi.as_view()),
    path('', TaskApiList.as_view()),
    path('<int:item_id>', TaskDetailApi.as_view()),
]
