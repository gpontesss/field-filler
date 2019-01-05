#Author: gpontesss
#Date of creation: 02-01-2019
#Description:
#	A brief script for filling PDF fields with data fetched from a .xlsx file (Excel)

from pdfrw import PdfReader, PdfWriter, PdfDict, IndirectPdfDict, PdfName
from openpyxl import load_workbook
from pdfform import PdfForm
from xlsxread import read_worksheet

xlsx_filename = 'data.xlsx'
worksheet_name ='data'
pdf_template_filename = 'template.pdf'

#Open .xlsx file as Workbook and get worksheet by name
workbook = load_workbook(xlsx_filename)
worksheet = workbook[worksheet_name]

pdf_form = PdfForm(pdf_template_filename)
data = read_worksheet(worksheet)

if filter(lambda x: x == False, map(lambda x: x.keys() == pdf_form.field_names(), data)):
	raise ValueError("Columns of xlsx file doesn't match with pdf template fields.")

for obj in data:
	for field_name in pdf_form.field_names():
		pdf_form.update_field(field_name, str(obj[field_name]))
	pdf_form.gen_pdf('filled-template-' + str(data.index(obj) + 1) + ".pdf")