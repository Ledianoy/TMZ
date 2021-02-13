import random

from main.costom_type import RequestT, ResponseT
from main.util import read_template


def handle_task_405(request: RequestT) -> ResponseT:
    template = read_template('task405.html')

    result = random_number()

    response = ResponseT(
        payload=template.format(result=result),
        content_type="text/html",
    )
    return response

def random_number () ->str:
    number = 0
    result = ""
    while number != 7:
        number = random.randint(1,10)
        result += f"{number} "
    return result