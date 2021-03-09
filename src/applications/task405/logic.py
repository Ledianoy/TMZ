
import random

def random_number () ->str:
    number = 0
    result = ""
    while number != 7:
        number = random.randint(1,10)
        result += f"{number} "
    return result