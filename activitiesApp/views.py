from django.shortcuts import render
from models import ActivityCategory
def view_some(request):
    q = ActivityCategory()
