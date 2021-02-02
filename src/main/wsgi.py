from typing import Callable
from typing import Tuple
from urllib.parse import parse_qs

import sentry_sdk

from framework.dirs import DIR_SRC
from framework.util.settings import get_setting
from tasks.lesson3.task303 import task303
from tasks.lesson3.task310 import task310
from tasks.lesson3.task311 import task311

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

ResponseT = Tuple[str, str, str]


def handle_error(method: str, path: str, qs: str) -> ResponseT:
    payload = str(1 / 0)
    return "500 Internal Server Error", "text/plain", payload


def handle_404(method: str, path: str, qs: str) -> ResponseT:
    status = "404 Not Found"
    content_type = "text/plain"
    payload = read_template("NotFound404.html")
    # payload = f"OOPS! endpoint {path} not found!"
    return status, content_type, payload


def handle_task_303(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)
    template = read_template('task303.html')

    sentence = qsi.get("sentence")

    if not sentence:
        result = ""
    else:
        sentence = sentence[0]
        result = task303.solution(sentence)

    payload = template.format(text=result)

    return status, content_type, payload


def handle_task_310(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)
    template = read_template('task310.html')

    sentence = qsi.get("sentence")

    if not sentence:
        result = ""
        result_coins = ""
    else:
        sentence = sentence[0]
        result, result_coins = task310.solution(sentence)
    # web_result = ""
    #
    # for key, value in result.items():
    #     web_result += f"<h2><p>Купюра {key}:{value} шт.</p></h2>"

    payload = template.format(text_mone=result, text_coins=result_coins)

    return status, content_type, payload


def handle_task_311(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)
    template = read_template('task311.html')

    sentence = qsi.get("sentence")

    if not sentence:
        result = ""
    else:
        sentence = sentence[0]
        result = task311.solution(sentence)
        result_prov = int(result)
        if result_prov == 1:
            result = "DOMAIN NAME is not supported"
        else:
            result = sentence

    payload = template.format(text=result)

    return status, content_type, payload


def index_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_template("index.html")
    return status, content_type, payload


def environ_page(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"
    payload = read_template("environ.html")
    return status, content_type, payload

def environ_format(environ: dict) -> str:
    show_environ = ""
    for key, value in environ.items():
        show_environ += (f"<p>{key}:{value}</p>")

    return show_environ


HANDLERS = {
    "/": index_page,
    "/e/": handle_error,
    "/environ/": environ_page,
    "/tasks/lesson3/task303/": handle_task_303,
    "/tasks/lesson3/task310/": handle_task_310,
    "/tasks/lesson3/task311/": handle_task_311,

}


def get_handler(path: str) -> Callable:
    handler = HANDLERS.get(path, handle_404)

    return handler


def application(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    query_string = environ["QUERY_STRING"]

    handler = get_handler(path)

    status, content_type, payload = handler(method, path, query_string)

 #   show_environ = environ_format(environ)
    # web_page_environ = payload.format(web_environ=show_environ).encode()

    headers = {"Content-type": content_type,}

    start_response(status, list(headers.items()))

    yield payload.encode()


def read_template(template_name: str) -> str:

    dir_templates = DIR_SRC / 'pages_html'
    template = dir_templates / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()

    return content
