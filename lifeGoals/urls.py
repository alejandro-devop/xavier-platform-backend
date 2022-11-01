from django.urls import path
from .views import GoalApiList
urlpatterns = [
    path('', GoalApiList.as_view())
]