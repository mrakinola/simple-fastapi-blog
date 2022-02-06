from fastapi import HTTPException, status
from markdown import markdown
from os.path import join


def read_markdown(filename: str):
    path = join("app/page-content", filename)
    try:
        with open(path, "r", encoding="utf-8") as file_to_read:
            simple_text = file_to_read.read()
    except Exception as e:
        file_without_markup = filename[:-3]
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Markdown page for {file_without_markup} not found"
        )

    converted_html = markdown(simple_text)
    info = {"simple_text": converted_html}
    return info
