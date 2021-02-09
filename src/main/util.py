
from framework.dirs import DIR_SRC
from main.costom_type import RequestT, ResponseT
from typing import Dict
from urllib.parse import parse_qs

from tasks.envirion import environ_format


def read_template(template_name: str) -> str:

    dir_templates = DIR_SRC / 'pages_html'
    template = dir_templates / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()

    return content


# def build_request(environ: Dict) -> RequestT:
#     qs = environ["QUERY_STRING"]
#     query = parse_qs(qs)
#
#     request = RequestT(
#         method=environ["REQUEST_METHOD"],
#         path=environ["PATH_INFO"],
#         query=query,
#     )
#
#     return request


def index_page(_request: RequestT) -> ResponseT:
    response = ResponseT(payload=read_template("index.html"),  content_type="text/html",)
    return response


def environ_page(request: RequestT, environ:dict) -> ResponseT:
    template = read_template("environ.html")
    result = environ_format(environ)
    payload = template.format(web_environ=result)
    response = ResponseT(payload=template.format(web_environ=result),  content_type="text/html",)
    return response