from main.costom_type import RequestT, ResponseT
from main.util import read_template


def handle_task_404(request: RequestT) -> ResponseT:
    template = read_template('task404.html')
    client_input = request.query.get("input_number",[""])[0]
    if client_input == "":
        result = ""
    else:
        result = sum_cube(client_input)
    response = ResponseT(
        payload=template.format(result=result),
        content_type="text/html",
    )
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

