import pathlib

base_dir = pathlib.Path(__file__).parent
# print(base_dir)
default_dir = base_dir / 'files'

support_dict = {
    "excel": "write_excel",
    "text": "write_text",
    "pdf": "write_pdf",
}

choices_dict = support_dict.keys()
