from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_page(request: HttpRequest) -> HttpResponse:
    context = {}
    response = render(request, "index/index.html", context)

    return response
