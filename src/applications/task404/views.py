from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task404.logic import sum_cube


def handle_task_404(request: HttpRequest) -> HttpResponse:

    client_input = request.GET.get("input_number","")
    if client_input == "":
        result = ""
    else:
        result = sum_cube(client_input)

    context = {
        "input_number": client_input,
        "result": result,
    }

    response = render(request, "task404/index.html", context)

    return response



