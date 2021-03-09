
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

