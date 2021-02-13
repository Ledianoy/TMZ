from main.costom_type import RequestT, ResponseT
from main.util import read_template


def handle_task_406(request: RequestT) -> ResponseT:
    template = read_template('task406.html')
    client_input_n = request.query.get("input_number_n",[""])[0]
    client_input_m = request.query.get("input_number_m",[""])[0]
    if client_input_n == "":
        result = ""
    elif client_input_m == "":
        result = ""
    else:
        result = sum_cube(client_input_n,client_input_m)

    response = ResponseT(
        payload=template.format(result=result, result_n=client_input_n, result_m=client_input_m),
        content_type="text/html",
    )
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

