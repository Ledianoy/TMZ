import random
from django.http import HttpRequest, HttpResponse
from main.util import render_template

TEMPLATE = "pages_html/task405.html"


def handle_task_405(_request: HttpRequest) -> HttpResponse:

    result = random_number()


    context = {
         "result": result,
    }
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    return response

def random_number () ->str:
    number = 0
    result = ""
    while number != 7:
        number = random.randint(1,10)
        result += f"{number} "
    return result