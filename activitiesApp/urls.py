from django.urls import path
from .views import ActivityCategoryApiList

urlpatterns = [
    path('categories/', ActivityCategoryApiList.as_view())
]