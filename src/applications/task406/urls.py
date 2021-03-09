from django.urls import path

from .views import handle_task_406

urlpatterns = [
    path("", handle_task_406),
]