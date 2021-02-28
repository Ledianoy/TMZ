import os
from pathlib import Path
from typing import Optional

from django.http import HttpRequest, HttpResponse

from framework.dirs import DIR_STORAGE
from main.util import render_template

TEMPLATE = "pages_html/task402.html"

def handle_task_402(request: HttpRequest) -> HttpResponse:
    client_cookes = request.COOKIES
    if not client_cookes:
        client_name = create_new_client()
    else:
        client_name = client_cookes['name']
    result = ""
    list_number = ""
    if request.method == 'POST':
        client = request.body
        client_str = client.decode('utf-8')
        client_data = client_str.split("=")
        if len(client_data) == 2:
            client_data.append("")
        if client_data[2] == "stop":
             result = calc_sum(client_name)
             list_number = list_number_all(client_name)
        elif client_data[1].isnumeric():
             number = int(client_data[1])
             add_number(client_name, number)
             list_number = list_number_all(client_name)
        if client_data[2] == "stop":
            file_dell(client_name)

    context = {
        "list_number": list_number,
        "result": result,
    }
    document = render_template(TEMPLATE, context)
    response = HttpResponse(document)
    response.set_cookie('name',client_name)
    return response


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

def calc_sum(client_name: str) -> int:
    data_file = get_client_file(client_name)

    with data_file.open("r") as src:
        result = sum(int(line.strip()) for line in src.readlines())

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