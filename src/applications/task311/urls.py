from django.urls import path

from .views import handle_task_311

urlpatterns = [
    path("", handle_task_311),
]