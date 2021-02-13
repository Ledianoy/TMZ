from main.costom_type import RequestT, ResponseT
from main.util import read_template


def division_into_email(n1:str) ->str:
    email_info = 1
    index = n1.find("@")
    if index == -1:
        raise ValueError("function does not support sentences with > 2 words")
        return email_info
    input = n1.split("@")
    return input

def email_look(n2:str) ->int:
    email_info = 1
    if n2 == 'gmail.com':
        email_info = 2
    return email_info

def solution(sentence: str) -> int:

    input_user = division_into_email(sentence)
    email = input_user[1]
    email_info = email_look(email)
    return email_info

def handle_task_311(request: RequestT) -> ResponseT:
    sentence = request.query.get("sentence", [""])[0] or ""

    template = read_template('task311.html')
    if not sentence:
        result = ""
    else:
        result = solution(sentence)
        result_prov = int(result)
        if result_prov == 1:
            result = "DOMAIN NAME is not supported"
        else:
            result = sentence

    response = ResponseT(payload=template.format(text=result),  content_type="text/html",)
    return response