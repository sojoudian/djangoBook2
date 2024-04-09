from django.urls import path
from .views import hi_view

urlpatterns = [
    path('hi/', hi_view, name="hi_view"),
]