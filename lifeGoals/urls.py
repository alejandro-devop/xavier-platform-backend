from django.urls import path
from .views import GoalApiList, GoalDetailApi
urlpatterns = [
    path('', GoalApiList.as_view()),
    path('/<int:item_id>', GoalDetailApi.as_view())
]