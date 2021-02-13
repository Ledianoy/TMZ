from main.costom_type import RequestT, ResponseT
from main.util import read_template


def handle_task_407(request: RequestT) -> ResponseT:
    template = read_template('task407.html')
    client_input_a = request.query.get("input_number_a",[""])[0]
    client_input_b = request.query.get("input_number_b",[""])[0]
    if client_input_a == "":
        result = ""
    elif client_input_b == "":
        result = ""
    else:
        result = whole_numbers_sum(client_input_a, client_input_b)

    response = ResponseT(
        payload=template.format(result=result, result_a=client_input_a, result_b=client_input_b),
        content_type="text/html",
    )
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

