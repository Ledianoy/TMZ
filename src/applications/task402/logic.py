import os
from pathlib import Path
from typing import Optional
from django.http import HttpRequest
from framework.dirs import DIR_STORAGE


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
