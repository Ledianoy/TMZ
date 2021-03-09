import pandas as pd
import random

def matrix(client_input: str) -> str:
    if int(client_input) == False:
        result = "User entered not a number"
        result_sum = ""
        raise ValueError(result)
    else:
        result = ""
        sum_3 = 0

        my_matrix = pd.DataFrame(columns=range(int(client_input)), index=range(int(client_input)))
        x = 0
        y = 0
        while x <= int(client_input) - 1:
            while y <= int(client_input) - 1:
                zn = random.randint(1, 100)
                my_matrix.loc[[x], [y]] = zn
                y += 1
                if (zn % 3 == 0):
                    sum_3 += zn
            x += 1
            y = 0
        result = my_matrix.to_html(table_id="my_id")

    return result, sum_3