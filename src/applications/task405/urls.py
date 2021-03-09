from django.urls import path

from .views import handle_task_405

urlpatterns = [
    path("", handle_task_405),
]