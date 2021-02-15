from django.http import HttpRequest, HttpResponse

from main.henders.henders_system import handle_404
from project.urls import urlpatterns


def get_handler(request: HttpRequest) -> HttpResponse:

    handler = urlpatterns.get(request.path, handle_404)

    return handler

