# pip install pdfplumber

# 不能识别扫描图片做成的pdf

import pdfplumber

def getContent(pdf_path, pages:list):
    pdf = pdfplumber.open(pdf_path)

    text = ''

    for page in pages:
        get_page =pdf.pages[page]
        text += get_page.extract_text()
    
    return text


if __name__ == "__main__":
    pass
    