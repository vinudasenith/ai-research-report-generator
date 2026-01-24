import os

def save_md(md_text, filename="report.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_text)
    return filename
