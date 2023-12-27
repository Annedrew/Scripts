import fitz  # PyMuPDF
import re

def extract_options_from_pdf(pdf_path, question_number):
    # "rb" means read binary
    with open(pdf_path, 'rb') as file:
        doc = fitz.open(stream=file.read(), filetype="pdf")

    options_pattern = re.compile(f'Question #{question_number}\n(.+?)\nA\. (.+?)\nB\. (.+?)\nC\. (.+?)\nD\. (.+?)\n', re.DOTALL)
    extracted_options = []

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text()  # Specify the encoding
        decoded_text = text.encode('utf-8').decode('utf-8')

        matches = options_pattern.search(text)
        if matches:
            question = matches.group(1)
            extracted_options = [matches.group(i) for i in range(2, 6)]

    doc.close()
    return extracted_options


def write_txt(extracted_options, question_number):
    with open("options.txt", "a", encoding="utf-8") as file:
        file.write(f"{question_number}\n")
        file.write("- ")
        file.write("\n- ".join(extracted_options))
        file.write("\n\n")
