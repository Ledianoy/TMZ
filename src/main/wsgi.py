
import sentry_sdk

from framework.dirs import DIR_SRC
from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

def application(environ, start_response):
    url_name = ""
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    if environ["PATH_INFO"] == "/environ/":
        url_name = "about.html"

    if environ["PATH_INFO"] == "/":
        url_name = "intex.html"

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }
    environ2 = ""

    for key in environ:
        value = environ[key]
        text = f"<p>{key} : {value}</p>"
        environ2 = environ2 + text


    #
    # payload = template.format(evrine=environ2)
    if url_name == "about.html":
        template = read_template(url_name)
        payload = template.format(evrine=environ2)
    else:
        template = read_template(url_name)
        payload = template.format()
    start_response(status, list(headers.items()))

    yield payload.encode()

def read_template(template_name:str) ->str:
    dir_template = DIR_SRC / "main" / "temples"
    template = dir_template / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()
    return content