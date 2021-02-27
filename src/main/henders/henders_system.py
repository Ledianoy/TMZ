#
# from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
#
# def handle_404(_request: HttpRequest) -> HttpResponse:
#    response = HttpResponseNotFound("NotFound404.html")
#        #
#        #
#        # HttpResponse(
#        #  content_type="text/html",
#        #  payload=read_template("NotFound404.html"),
#        #  status=HTTPStatus.NOT_FOUND,
#
#    return response
import traceback
from http import HTTPStatus

from main.costom_type import RequestT, ResponseT


def handle_500(_request: RequestT) -> ResponseT:
    response = ResponseT(
        content_type="text/plain",
        payload=traceback.format_exc(),
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )
#
#     return response
#
# def handle_error(method: str, path: str, qs: str) -> ResponseT:
#     payload = str(1 / 0)
#     return "500 Internal Server Error", "text/plain", payload


