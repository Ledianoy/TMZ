from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task406.logic import sum_cube


def handle_task_406(request: HttpRequest) -> HttpResponse:
    client_input_n = request.GET.get("input_number_n","")
    client_input_m = request.GET.get("input_number_m","")
    if client_input_n == "":
        result = ""
    elif client_input_m == "":
        result = ""
    else:
        result = sum_cube(client_input_n,client_input_m)

    context = {
        "result_n": client_input_n,
        "result_m": client_input_m,
        "result": result,
    }

    response = render(request, "task406/index.html", context)

    return response



