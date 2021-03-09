from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.task402.logic import create_new_client, calc_sum, list_number_all, add_number, file_dell


def handle_task_402(request: HttpRequest,) -> HttpResponse:
    client_cookes = request.COOKIES
    if len(client_cookes)<=1:
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

    response = render(request, "task402/index.html", context)
    response.set_cookie('name',client_name)

    return response



