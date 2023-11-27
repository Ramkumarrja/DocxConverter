from abc import ABC,abstractmethod
from  converter import DocxConverter
class DocConverter(ABC):
    @abstractmethod
    def Docxconvert(self):
        pass

pdf="MedFit form.pdf"
docx="MedFit form.docx"
file=DocxConverter(pdf,docx)