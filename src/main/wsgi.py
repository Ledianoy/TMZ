import sentry_sdk



from framework.util.settings import get_setting
from main.costom_type import RequestT
from main.henders.henders_system import  handle_500
from main.henders.hendlers import get_handler

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def application(environ, start_response):
    request = RequestT(environ)
    handler = get_handler(request)


    try:
        response = handler(request)
    except Exception:
        response = handle_500(request)

    headers = {
        "Content-Type": response.content_type,
        **response.headers,
    }

    status = f"{response.status.value} {response.status.phrase}"
    headers_list = list(headers.items())
    start_response(status, headers_list)


    yield response.payload.encode()


