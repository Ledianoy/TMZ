from pathlib import Path
from string import Template
from typing import Dict
from typing import Optional
from typing import Union

from django.http import HttpRequest, HttpResponse
from framework.dirs import DIR_SRC

TEMPLATE = "pages_html/index.html"


def read_template1(template_name: str) -> str:
    dir_templates = DIR_SRC / 'pages_html'
    template = dir_templates / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()

    return content

def read_template(template_path: Union[str, Path]) -> str:
    template = DIR_SRC / template_path

    assert template.is_file(), f"template {template_path!r} is not a file"

    with template.open("r") as fd:
        content = fd.read()

    return content


def index_page(_request: HttpRequest) -> HttpResponse:
    context = {}
    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response


def render_template(
        template_path: Union[str, Path],
        context: Optional[Dict] = None,
        *,
        engine: str = "{",
        ) -> str:
    template = read_template(template_path)
    context = context or {}

    engines = {
        "{": lambda _ctx: template.format(**_ctx),
        "$": Template(template).safe_substitute,
    }

    renderer = engines[engine]
    document = renderer(context)

    return document
