from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from main.util import index_page
from tasks.Lesson4.task402 import handle_task_402
from tasks.Lesson4.task402cookies import handle_task_402_cookies
from tasks.Lesson4.task404 import handle_task_404
from tasks.Lesson4.task405 import handle_task_405
from tasks.Lesson4.task406 import handle_task_406
from tasks.Lesson4.task407 import handle_task_407
from tasks.Lesson5.task502 import handle_task_502
from tasks.Lesson5.task507 import handle_task_507
from tasks.lesson3.task303 import handle_task_303
from tasks.lesson3.task310 import handle_task_310
from tasks.lesson3.task311 import handle_task_311

#
# def xxx(req):
#     number = req.GET.get ("number")
#     if number:
#         req.session["number"] = number
#     else:
#         number = req.session.get ("number")
#
#     return HttpResponse(
#         f" Hello World! metthod: {number}"
#     )
#
#     pass
#


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_page),
    # path("e/", handle_error),
    path("tasks/lesson3/task303/", handle_task_303),
    path("tasks/lesson3/task310/", handle_task_310),
    path("tasks/lesson3/task311/", handle_task_311),
    path("tasks/lesson4/task402/", csrf_exempt(handle_task_402)),
    path("tasks/lesson4/task402cookies/", csrf_exempt(handle_task_402_cookies)),
    path("tasks/lesson4/task404/", handle_task_404),
    path("tasks/lesson4/task405/", handle_task_405),
    path("tasks/lesson4/task406/", handle_task_406),
    path("tasks/lesson4/task407/", handle_task_407),
    path("tasks/lesson5/task502/", handle_task_502),
    path("tasks/lesson5/task507/", csrf_exempt(handle_task_507)),
]
