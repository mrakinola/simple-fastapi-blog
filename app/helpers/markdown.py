from markdown import markdown
from os.path import join


def read_markdown(filename: str) -> dict:
    path = join("app/pagecontent", filename)
    with open(path, "r", encoding="utf-8") as file_to_read:
        simple_text = file_to_read.read()

    converted_html = markdown(simple_text)
    info = {
        "simple_text": converted_html
    }
    return info
