#Author: gpontesss
#Date of creation: 04-01-2019
#Description:
#	PdfForm class with utilities for handling pdf forms more easily.

#Importing pdfrw ibrary utilities
from pdfrw import PdfReader, PdfWriter, PdfDict, IndirectPdfDict, PdfName

class PdfForm():
	def __init__(self, path):
		self.path = path
		self.file = PdfReader(path)
		self.fields_info = self.read_fields()

	def read_fields(self):
		fields = {}
		list = self.file.Root.AcroForm.Fields
		
		for field in list:
			fields[field.T] = {
				'index': list.index(field),
				'value': field.V
			}
		return fields

	def field_names(self):
		return self.fields_info.keys()

	def field_index(self, name):
		return self.fields_info[name]['index']

	def update_field(self, name, value):
		file_fields = self.file.Root.AcroForm.Fields
		field = file_fields[self.field_index(name)]

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
		xobj.stream = "/Tx BMC\nBT\n /Helvetica 8.0 Tf\n 1.0 5.0 Td\n 0 g\n (" + value + ") Tj\nET EMC"
		file_fields[self.field_index(name)].AP = PdfDict(N = xobj)

		#Change the value when field is foccused
		field.update(PdfDict(V=value))
		return field

	def gen_pdf(self, name):
		PdfWriter().write(name, self.file)
		return name + " was created."