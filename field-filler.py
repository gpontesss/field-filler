#A brief script for filling PDF fields with data fetched from a .xlsx file (Excel)
from pdfrw import PdfReader, PdfWriter, PdfDict, IndirectPdfDict, PdfName
from openpyxl import load_workbook

file = 'tester.pdf'

#Open .xlsx file as Workbook
wb = load_workbook('data.xlsx')
#Open sheet on wb acessing it by name index
ws = wb[u'fields-data']

def read_data():
    map = {}
    data = []

	#Get column names and map to their title
    for cell in ws[1]:
        map[cell.column] = cell.value

    for row in ws.iter_rows(min_row=2, max_col=len(map.keys()), max_row=ws.max_row):
        person_data = {}
        for cell in row:
            person_data[map[cell.column]] = cell.value
        if not filter(lambda x: x is not None, person_data.values()):
			break
        data.append(person_data)

    return data

xlsx_data = read_data()

template = PdfReader(file)

for obj in xlsx_data:
    for field in template.Root.Pages.Kids[0].Annots:
        
        #Field label
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

        #Change the value of field when not foccused
        xobj.stream = "/Tx BMC\nBT\n /Helvetica 8.0 Tf\n 1.0 5.0 Td\n 0 g\n (" + str(obj[label]) + ") Tj\nET EMC"
        template.Root.AcroForm.Fields[template.Root.Pages.Kids[0].Annots.index(field)].AP = PdfDict(N = xobj)

        #Change the value when field is foccused
        field.update(PdfDict(V=str(obj[label])))

    filename = 'test-out-' + str(xlsx_data.index(obj) + 1) + '.pdf'
    PdfWriter().write(filename, template)
    print filename + " was generated."