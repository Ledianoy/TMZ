from main.costom_type import RequestT, ResponseT
from main.util import read_template


def ask_user_to_input_a_sentence() -> str:
    s = input("введи предложение из двух слов: ")
    return s


def extract_words_from_sentence(s: str) -> list:
    w = s.split(" ")
    return w


def render_template(t: str, c: dict) -> str:
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

    result = render_template(template, context)

    return result


def handle_task_303(request: RequestT) -> ResponseT:
    sentence = request.query.get("sentence", [""])
    template = read_template('task303.html')

    if not sentence:
        result = ""
    else:
        sentence = sentence[0]
        result = solution(sentence)

    response = ResponseT(payload=template.format(text=result),  content_type="text/html",)
    return response