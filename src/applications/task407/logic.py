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

