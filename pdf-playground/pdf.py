import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
watermarked_pdf = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	watermarked_pdf.addPage(page)

	with open('watermarked_output.pdf', 'wb') as file:
		watermarked_pdf.write(file)
