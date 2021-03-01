from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("applications.index.urls")),
    path("tasks/lesson3/task303/", include("applications.task303.urls")),
    path("tasks/lesson3/task310/", include("applications.task310.urls")),
    path("tasks/lesson3/task311/", include("applications.task311.urls")),
    path("tasks/lesson4/task402/", include("applications.task402.urls")),
    path("tasks/lesson4/task404/", include("applications.task404.urls")),
    path("tasks/lesson4/task405/", include("applications.task405.urls")),
    path("tasks/lesson4/task406/", include("applications.task406.urls")),
    path("tasks/lesson4/task407/", include("applications.task407.urls")),
    path("tasks/lesson5/task502/", include("applications.task502.urls")),
    path("tasks/lesson5/task507/", include("applications.task507.urls")),
]
