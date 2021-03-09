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

