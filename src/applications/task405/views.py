from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task405.logic import random_number


def handle_task_405(request: HttpRequest) -> HttpResponse:

    result = random_number()


    context = {
         "result": result,
    }

    response = render(request, "task405/index.html", context)

    return response



