from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task303.logic import solution

def handle_task_303(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    result = solution(sentence) if sentence else ""

    context = {
        "sentence": sentence,
        "result": result,

    }

    response = render(request, "task303/index.html", context)

    return response
