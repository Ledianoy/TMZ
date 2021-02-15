from django.http import HttpRequest, HttpResponse

from main.util import render_template

TEMPLATE = "pages_html/task404.html"


def handle_task_404(request: HttpRequest) -> HttpResponse:
    # template = read_template('task404.html')
    client_input = request.GET.get("input_number","")
    if client_input == "":
        result = ""
    else:
        result = sum_cube(client_input)

    context = {
        "input_number": client_input,
        "result": result,
    }
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    return response

def sum_cube (client_input: str) -> int:
    if int(client_input) == False:
        result = "User entered not a number"
        raise ValueError(result)
    else:
        client_int = int(client_input)
        result = 0
        meter = 1
        while meter <= client_int:
            result += meter **3
            meter +=1
    return result

