from django.http import HttpRequest, HttpResponse

from main.util import render_template

TEMPLATE = "pages_html/task406.html"


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
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    return response

def sum_cube (client_input_n: str, client_input_m: str) -> int:
    if int(client_input_n) == False:
        result = "User entered not a number n"
        raise ValueError(result)
    elif int(client_input_m) == False:
        result = "User entered not a number m"
        raise ValueError(result)
    else:
        client_int_n = int(client_input_n)
        client_int_m = int(client_input_m)
        result = 0
        for i in range(client_int_n, client_int_m):
            result += i **3
            i +=1
    return result

