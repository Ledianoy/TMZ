from django.urls import path

from .views import handle_task_507

urlpatterns = [
    path("", handle_task_507),
]