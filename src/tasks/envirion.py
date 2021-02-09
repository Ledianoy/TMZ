
def environ_format(environ: dict) -> str:
    show_environ = ""
    for key, value in environ.items():
        show_environ += (f"<p>{key}:{value}</p>")

    return show_environ

