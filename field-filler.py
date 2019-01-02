#A brief script for filling PDF fields with data fetched from a .xlsx file (Excel)
from pdfrw import PdfReader, PdfWriter, PdfDict, IndirectPdfDict, PdfName

#file = 'S-89-T-4up.pdf'
file = 'tester.pdf'

values = {
    '(name)': "Gabriel",
    '(email)': "gabriel@gmail.com",
    '(address)': "Rua do Gabriel, 01",
    '(age)': "18",
    '(cep)': "100100100"
}

template = PdfReader(file)
for field in template.Root.Pages.Kids[0].Annots:
    
    label = field.T
    
    rct = field.Rect
    height = round(float(rct[3]) - float(rct[1]), 2)
    width = round(float(rct[2]) - float(rct[0]), 2)

    xobj = IndirectPdfDict(
        BBox = [0, 0, width, height],
        FormType = 1,
        Resources = PdfDict(Prosec = [PdfName.PDF, PdfName.Text]),
        Subtype = PdfName.Form,
        Type = PdfName.XObject
    )

    value = values[label]
    xobj.stream = "/Tx BMC\nBT\n /Helvetica 8.0 Tf\n 1.0 5.0 Td\n 0 g\n (" + value + ") Tj\nET EMC"

    template.Root.AcroForm.Fields[template.Root.Pages.Kids[0].Annots.index(field)].AP = PdfDict(N = xobj)

PdfWriter().write('test-out.pdf', template)