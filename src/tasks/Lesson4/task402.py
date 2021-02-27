from typing import Optional, Dict
from django.http import HttpRequest, HttpResponse
from main.util import render_template
from main.henders.henders_system import post_in_dict

TEMPLATE = "pages_html/task402.html"

def get_accumulated(session: Dict) -> int:
    result = session.get("task402", 0)

    return result


def add_numberes(session: Dict, number: int) -> int:
    number_session = session.get("task402", 0)
    if number_session == '':
        number_session = 0
    number_session += number
    session["task402"] = number_session
    list = session["task402_list"]
    session["task402_list"] = f"{list} {number} "


    return number


def handle_task_402(request: HttpRequest) -> HttpResponse:
    number = ''
    list = ""
    session = request.session
    number_input = ""
    if request.method.lower() == "post":
        data = post_in_dict(request)
        if data['input_number']:
            number_input = int(data.get('input_number', "0"))
            add_numberes(session, number_input)
            list = session["task402_list"]
        elif data['input_number_stop']:
            number = get_accumulated(session)
            list = session["task402_list"]
            session["task402"] = 0
            session["task402_list"] = ""
        else:
            number = ''
            list =""

    else:
        number = get_accumulated(request.session)

    context = {
        "list_number": list,
        "result": number,
    }
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    return response
