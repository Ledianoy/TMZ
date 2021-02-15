from django.http import HttpRequest, HttpResponse

from main.util import render_template

TEMPLATE = "pages_html/task303.html"



def extract_words_from_sentence(s: str) -> list:
    w = s.split(" ")
    return w


def render(t: str, c: dict) -> str:
    r = t.format(**c)
    return r


def solution(sentence: str) -> str:
    """
    Splits a sentence to two words, exchanges them
    and adds "!" to each side of new sentence.
    """

    words = extract_words_from_sentence(sentence)
    if len(words) < 2:
        word = words[0]
        return f"!{word}!"

    if len(words) > 2:
        raise ValueError("function does not support sentences with > 2 words")

    template = "!{word2} {word1}!"
    context = {
        "word1": words[0],
        "word2": words[1],
    }


    result = render(template, context)

    return result


def handle_task_303(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    result = solution(sentence) if sentence else ""

    context = {
        "sentence": sentence,
        "result": result,

    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response
