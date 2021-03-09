from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task502.logic import matrix


def handle_task_502(request: HttpRequest) -> HttpResponse:
    client_input = request.GET.get("input_number", "")
    if client_input == "":
        result = ""
        result_sum = ""
    else:
        result, result_sum = matrix(client_input)

    context = {
        "result_sum": result_sum,
        "result": result,
    }

    response = render(request, "task502/index.html", context)

    return response



