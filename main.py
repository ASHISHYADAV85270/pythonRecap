from PyPDF2 import PdfMerger

merger = PdfMerger()
totalpdfs=["barriers.pdf", "opc_sessional_1.pdf"]
for pdf in totalpdfs:
    merger.append(pdf,pages=(0,3))

merger.write("merged-pdf.pdf")
merger.close()