from random import randrange
from typing import Dict

from django.http import HttpRequest, HttpResponse

from main.henders.henders_system import post_in_dict
from main.util import render_template

TEMPLATE = "pages_html/task507.html"


def handle_task_507(request: HttpRequest) -> HttpResponse:
    result = ""
    froms = int(request.GET.get('input_number_from', "0"))
    before = int(request.GET.get('input_number_before', "0"))
    attempt = int(request.GET.get('input_number_attempt', "0"))
    repeat = int(request.GET.get('repeat', "0"))
    value = ""
    if int(request.session["task507_attempt"]) == -1:
        request.session["task507_attempt"] = attempt
    if repeat == 1:
        request.session["task507_attempt"] = -1
        request.session["task402_list"] = ''
    if len(request.session["task402_list"])<=1:
        difference = before - froms
        i = 1
        list = ''
        while i <= difference:
            number = randrange(froms, before)
            list = request.session["task402_list"] = f"{list} {number} "
            i += 1
    if request.method.lower() == "post":
        data = post_in_dict(request)
        if len(data) >=1:
            value = int(data.get('input_number_value',"-1"))
            request.session["task507_froms"] = froms
            request.session["task507_before"] = before
            request.session["task507_value"] = value
            if value >=0:
                result = check_value(request.session,value)

    attempt = request.session["task507_attempt"]
    context = {
        "froms": froms,
        "before": before,
        "attempt" : attempt,
        "value": value,
        "result": result,
    }
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    return response


def check_value(session: Dict, value:int) -> str:
    list = session["task402_list"]
    attempt =int(session["task507_attempt"])
    result = "You are the loser"
    if len(list)>1:
        if attempt > 0:
            client_lst = list.split(' ')
            for i in client_lst:
                temp = i.isnumeric()
                if temp == True:
                    data = int(i)
                    if data == value:
                        result = "You are the winner"
            session["task507_attempt"] = attempt - 1
        else:
            result = f"У вас закончились попытки. Числа диапазона {list}"
    return result