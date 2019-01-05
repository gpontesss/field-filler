# Field Filler
A brief script for filling fields of a PDF with forms with data fetched from a .xlsx file (Excel 2010, so I heard). It is quite strict, in a sense that you need to follow a specific format for it to work. Here are the rules to follow by now:

- The first row of your worksheet must have the names of fields on your pdf form template, else it won't like you. Make sure to put brackets around your field name. Example: '(name)'.
- Name your pdf template.pdf.
- Name your xlsx data.xlsx and your target worsheet as 'data'.

## Requirements
You will need to install pdfrw (read/write .pdf) and openpyxl (read/write .xlsx) libraries. To do so, run the following, if you're on linux:

``` bash
sudo pip install pdfrw openpyxl
```

This is python 2.7, just for knowledge.

## Ideas for a far future
If I ever mess with this again, would be cool to add some functions on PdfForm class for customizing fonts and stuff like that. Can't think of much else.

## Useful links for debugging
Fields not showing updated values without refreshing: https://github.com/pmaupin/pdfrw/issues/84