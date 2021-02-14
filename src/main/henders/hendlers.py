from main.costom_type import HandlerT, RequestT
from main.henders.henders_system import handle_error, handle_404
from main.util import index_page, environ_page
from tasks.Lesson5.task502 import handle_task_502
from tasks.lesson3.task303 import handle_task_303
from tasks.lesson3.task310 import handle_task_310
from tasks.lesson3.task311 import handle_task_311
from tasks.Lesson4.task402 import handle_task_402
from tasks.Lesson4.task404 import handle_task_404
from tasks.Lesson4.task405 import handle_task_405
from tasks.Lesson4.task406 import handle_task_406
from tasks.Lesson4.task407 import handle_task_407


HANDLERS = {
    "/": index_page,
    "/e/": handle_error,
    "/environ/": environ_page,
    "/tasks/lesson3/task303/": handle_task_303,
    "/tasks/lesson3/task310/": handle_task_310,
    "/tasks/lesson3/task311/": handle_task_311,
    "/tasks/lesson4/task402/": handle_task_402,
    "/tasks/lesson4/task404/": handle_task_404,
    "/tasks/lesson4/task405/": handle_task_405,
    "/tasks/lesson4/task406/": handle_task_406,
    "/tasks/lesson4/task407/": handle_task_407,
    "/tasks/lesson5/task502/": handle_task_502,
}


def get_handler(request: RequestT) -> HandlerT:

    handler = HANDLERS.get(request.path, handle_404)

    return handler

