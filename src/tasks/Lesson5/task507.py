import os
from pathlib import Path
from random import random, randrange
from typing import Optional

from django.http import HttpRequest, HttpResponse

from framework.dirs import DIR_STORAGE
from main.util import render_template

TEMPLATE = "pages_html/task507.html"

def handle_task_507(request: HttpRequest) -> HttpResponse:
    client_cookes = request.COOKIES
    if not client_cookes:
        client_name = create_new_client()
    else:
        client_name = client_cookes['name']
    result = ""
    froms = ""
    before = ""
    attempt = ""
    value = ""
    if request.method == 'POST':
        data = post_in_dict(request)
        if len(data) >=1:
            froms = int(data.get('input_number_from',"0"))
            before = int(data.get('input_number_before',"0"))
            attempt = int(data.get('input_number_attempt',"0"))
            value = int(data.get('input_number_value',"-1"))
            if value >=0:
                result = check_value(client_name, value)
            elif value == -1:
                difference = before-froms
                i=1
                while i <= difference:
                   number = randrange(froms,before)
                   add_number(client_name,number)
                   i +=1

    context = {
        "froms": froms,
        "before": before,
        "attempt" : attempt,
        "value": value,
        "result": result,
    }
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    response.set_cookie('name',client_name)
    return response

def post_in_dict(request: HttpRequest) -> dict:
    client_input = request.body.decode('utf-8')
    client_lst = (client_input.replace('&', '=')).split("=")
    data = {client_lst[i]: client_lst[i+1] for i in range(0, len(client_lst), 2)}
    return data

def create_new_client() -> str:
    return os.urandom(36).hex()


def get_client_file(client_name: str) -> Path:
    file_path = DIR_STORAGE / f"{client_name}.402.txt"

    return file_path

def file_dell(client_name: str):
    file_name = DIR_STORAGE / f"{client_name}.402.txt"
    if not file_name:
        pass
    else:
        os.remove(file_name)
    return

def check_value(client_name: str, value:int) -> int:
    data_file = get_client_file(client_name)
    result = "You are the loser"
    with data_file.open("r") as src:
        for line in src.readlines():
            data = int(line.strip())
            if data == value:
                result = "You are the winner"

    return result

def list_number_all (client_name: str) -> str:
    data_file = get_client_file(client_name)
    file = os.path.exists(data_file)
    if file == False:
        result = ""
    else:
        with data_file.open("r") as src:
             result = src.read()

    return result



def add_number(client_name: str, number: int) -> int:
    data_file = get_client_file(client_name)

    with data_file.open("a") as dst:
        dst.write(f"{number}\n")

    return number


def get_client(request: HttpRequest) -> Optional[str]:
    cookies = request.headers.get("Cookie")
    if not cookies:
        return None
    cook = cookies.split(":")[0]

    cookie_name, cookie_value = cook.split("=")
    assert cookie_name == "name"

    return cookie_value or None