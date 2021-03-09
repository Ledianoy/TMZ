from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task311.logic import solution

def handle_task_311(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    if not sentence:
        result = ""
    else:
        result = solution(sentence)
        result_prov = int(result)
        if result_prov == 1:
            result = "DOMAIN NAME is not supported"
        else:
            result = sentence

    context = {
        'sentence': sentence,
        'text': result,
    }
    response = render(request, "task311/index.html", context)

    return response


