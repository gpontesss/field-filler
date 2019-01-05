#Author: gpontesss
#Date of creation: 04-01-2019
#Description:
#	Reading data from .xlsx file test

def read_worksheet(ws):
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