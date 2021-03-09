from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task407.logic import whole_numbers_sum


def handle_task_407(request: HttpRequest) -> HttpResponse:
    client_input_a = request.GET.get("input_number_a","")
    client_input_b = request.GET.get("input_number_b","")
    if client_input_a == "":
        result = ""
    elif client_input_b == "":
        result = ""
    else:
        result = whole_numbers_sum(client_input_a, client_input_b)

    context = {
        "result_a": client_input_a,
        "result_b": client_input_b,
        "result": result,
    }

    response = render(request, "task407/index.html", context)

    return response



