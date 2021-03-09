from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task310.logic import solution

def handle_task_310(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    if not sentence:
        web_result = ""
        web_result_coins = ""
    else:
        result, result_coins = solution(sentence)
        web_result = ""
        for key, value in result.items():
            web_result += f"<h2><p>купюра {key}:{value}</p></h2>"
        web_result_coins = ""
        for key, value in result_coins.items():
            web_result_coins += f"<h2><p>монета {key}:{value}</p></h2>"

    context = {
        "sentence": sentence,
        "text_mone": web_result,
        "text_coins": web_result_coins,

    }
    response = render(request, "task310/index.html", context)

    return response