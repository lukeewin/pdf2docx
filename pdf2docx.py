from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

# 调用函数进行转换
pdf_path = './a.pdf'
docx_path = './a.docx'
convert_pdf_to_docx(pdf_path, docx_path)

pdf2_path = './b.pdf'
docx2_path = './b.docx'
convert_pdf_to_docx(pdf2_path, docx2_path)
