from main.costom_type import HandlerT, RequestT
from main.henders.henders_lesson3 import handle_task_303, handle_task_310, handle_task_311
from main.henders.henders_system import handle_error, handle_404
from main.util import index_page, environ_page
from tasks.Lesson4.task402.task402 import handle_task_402

HANDLERS = {
    "/": index_page,
    "/e/": handle_error,
    "/environ/": environ_page,
    "/tasks/lesson3/task303/": handle_task_303,
    "/tasks/lesson3/task310/": handle_task_310,
    "/tasks/lesson3/task311/": handle_task_311,
    "/tasks/lesson4/task402/": handle_task_402,
}


def get_handler(request: RequestT) -> HandlerT:

    handler = HANDLERS.get(request.path, handle_404)

    return handler

