from django.urls import path

from .views import handle_task_402

urlpatterns = [
    path("", handle_task_402),
]