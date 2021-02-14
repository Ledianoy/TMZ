import pandas as pd
import random
from main.costom_type import RequestT, ResponseT
from main.util import read_template


def handle_task_502(request: RequestT) -> ResponseT:
    template = read_template('task502.html')
    client_input = request.query.get("input_number",[""])[0]
    if client_input == "":
        result = ""
        result_sum = ""
    else:
        result, result_sum = matrix(client_input)

    response = ResponseT(
        payload=template.format(result=result, result_sum=result_sum),
        content_type="text/html",
    )
    return response


def matrix(client_input: str) -> str:
    if int(client_input) == False:
        result = "User entered not a number"
        result_sum = ""
        raise ValueError(result)
    else:
        result = ""
        sum_3 = 0

        my_matrix =pd.DataFrame(columns=range(int(client_input)), index=range(int(client_input)))
        x=0
        y=0
        while x<= int(client_input)-1:
            while y<= int(client_input)-1:
                zn = random.randint(1,100)
                my_matrix.loc[[x],[y]] = zn
                y+=1
                if (zn % 3 == 0):
                    sum_3 += zn
            x+=1
            y=0
        result = my_matrix.to_html(table_id="my_id")

    return result, sum_3

