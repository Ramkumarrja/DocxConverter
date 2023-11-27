from pdf2docx import parse

class DocxConverter:
    def __init__(self,pdf_path,docx_path) -> None:
        self.pdf=pdf_path
        self.docx=docx_path
        return(parse(pdf_file=self.pdf, docx_with_path=self.docx))
    