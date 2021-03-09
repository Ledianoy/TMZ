from typing import Dict


def check_value(session: Dict, value: int) -> str:
    lists = session["task402_list"]
    attempt = int(session["task507_attempt"])
    result = "You are the loser"
    if len(lists) > 1:
        if attempt > 0:
            client_lst = lists.split(' ')
            for i in client_lst:
                temp = i.isnumeric()
                if temp == True:
                    data = int(i)
                    if data == value:
                        result = "You are the winner"
            session["task507_attempt"] = attempt - 1
        else:
            result = f"У вас закончились попытки. Числа диапазона {lists}"
    return result
