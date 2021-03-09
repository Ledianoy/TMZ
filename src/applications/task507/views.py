from random import randrange
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import requires_csrf_token
from applications.task507.logic import check_value
from project.util import post_in_dict

@requires_csrf_token
def handle_task_507(request: HttpRequest) -> HttpResponse:
    result = ""
    froms = int(request.GET.get('input_number_from', "0"))
    before = int(request.GET.get('input_number_before', "0"))
    attempt = int(request.GET.get('input_number_attempt', "0"))
    repeat = int(request.GET.get('repeat', "0"))
    request.session["task507_attempt"] = 0
    request.session["task402_list"] = ""
    value = ""
    if int(request.session["task507_attempt"]) == -1:
        request.session["task507_attempt"] = attempt
    if repeat == 1:
        request.session["task507_attempt"] = -1
        request.session["task402_list"] = ''
    if len(request.session["task402_list"]) <= 1:
        difference = before - froms
        i = 1
        lists = ''
        while i <= difference:
            number = randrange(froms, before)
            lists = request.session["task402_list"] = f"{lists} {number} "
            i += 1
    if request.method.lower() == "post":
        data = post_in_dict(request)
        if len(data) >= 1:
            value = int(data.get('input_number_value', "-1"))
            request.session["task507_froms"] = froms
            request.session["task507_before"] = before
            request.session["task507_value"] = value
            if value >= 0:
                result = check_value(request.session, value)

    attempt = request.session["task507_attempt"]
    context = {
        "froms": froms,
        "before": before,
        "attempt": attempt,
        "value": value,
        "result": result,
    }
    response = render(request, "task507/index.html", context)

    return response
