from django.http import HttpRequest, HttpResponse
from main.util import render_template
TEMPLATE = "pages_html/task407.html"


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
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    return response

def whole_numbers_sum (client_input_a: str, client_input_b: str) -> str:
    if int(client_input_a) == False:
        result = "User entered not a number n"
        raise ValueError(result)
    elif int(client_input_b) == False:
        result = "User entered not a number m"
        raise ValueError(result)
    else:
        client_int_a = int(client_input_a)
        client_int_b = int(client_input_b)+1
        result = ""
        kol = 0
        for i in range(client_int_a, client_int_b):
            kol += 1
            result += str(i)+ "-"
            i +=1
        result += str(kol)
    return result

