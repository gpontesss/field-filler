# Field Filler
A brief script for filling fields of a PDF with forms with data fetched from a .xlsx file (Excel). This has a single porpose for now, but eventually I want to make it modular, so it can be used in a more general situation.

## Requirements
You will need to install pdfrw (read/write .pdf) and openpyxl (read/write .xlsx) libraries. To do so, run the following, if you're on linux:

    ``` bash
    sudo pip install pdfrw openpyxl
	```

It is not yet finished, and may not be useful for you for porpuses other than consulting or inspiration.

## Useful links for debugging
Fields not showing updated values without refreshing: https://github.com/pmaupin/pdfrw/issues/84