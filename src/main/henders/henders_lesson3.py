
from main.costom_type import ResponseT, RequestT
from main.util import read_template
from tasks.lesson3.task303 import task303
from tasks.lesson3.task310 import task310
from tasks.lesson3.task311 import task311


def handle_task_303(request: RequestT) -> ResponseT:
    sentence = request.query.get("sentence", [""])
    template = read_template('task303.html')

    if not sentence:
        result = ""
    else:
        sentence = sentence[0]
        result = task303.solution(sentence)

    response = ResponseT(payload=template.format(text=result),  content_type="text/html",)
    return response


def handle_task_310(request: RequestT) -> ResponseT:
    template = read_template('task310.html')
    sentence = request.query.get("sentence", [""])[0] or ""

    if not sentence:
        web_result = ""
        web_result_coins = ""
    else:
        result, result_coins = task310.solution(sentence)
        web_result = ""
        for key, value in result.items():
            web_result += f"<h2><p>banknotes {key}:{value}</p></h2>"
        web_result_coins = ""
        for key, value in result_coins.items():
            web_result_coins += f"<h2><p>coins {key}:{value}</p></h2>"

    response = ResponseT(payload=template.format(text_mone=web_result, text_coins=web_result_coins),  content_type="text/html",)
    return response

def handle_task_311(request: RequestT) -> ResponseT:
    sentence = request.query.get("sentence", [""])[0] or ""

    template = read_template('task311.html')
    if not sentence:
        result = ""
    else:
        result = task311.solution(sentence)
        result_prov = int(result)
        if result_prov == 1:
            result = "DOMAIN NAME is not supported"
        else:
            result = sentence

    response = ResponseT(payload=template.format(text=result),  content_type="text/html",)
    return response