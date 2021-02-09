# from cgi import parse_qs

from main.costom_type import ResponseT
from main.util import read_template


# def handle_task_402(method: str, path: str, qs: str) -> ResponseT:
#     status = "200 OK"
#     content_type = 'text/html'
#     name ="xxx"
#     value = "12345678"
#     headers = [('Content-Type', content_type), set_cookie_header(name, value)]
#     payload = read_template("task402.html")
#     return status, content_type, payload