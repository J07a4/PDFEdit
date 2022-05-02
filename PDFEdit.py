from reportlab.pdfgen.canvas import Canvas
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import os
import pdb

pdf_path = (
    Path.home()
    / "desktop"
    / "Pruebas python"
    / "PyPDF"
    / "pre_tfg-5.pdf"
)
pdf_reader = PdfFileReader(str(pdf_path))

pdf_path = (
    Path.home()
    / "desktop"
    / "Pruebas python"
    / "PyPDF"
)

def extract_chapter(pdf,n,m):
    pdf_writer = PdfFileWriter()
    for i in range(m):
        page = pdf.getPage(i+n)
        pdf_writer.addPage(page)
    return pdf_writer

def save_pdf(pdf_writer,name):
    with Path('output/'+ name+".pdf").open(mode="wb") as output_file:
        pdf_writer.write(output_file)

def delete_pdf (name):
    os.system('del output\\'+ name)

def split_pdf(pdf,pg):
    pg=[0]+pg+[pdf.getNumPages()]
    for i in range(0,len(pg)-1):
        save_pdf(extract_chapter(pdf,pg[i],pg[i+1]-pg[i]),"chapter"+str(i+1))

def introduce_pdf (pdf1,pdf2,n):
    pdf_writer = PdfFileWriter()
    for i in range(n):
        page = pdf1.getPage(i)
        pdf_writer.addPage(page)
    for i in range(pdf2.getNumPages()):
        page = pdf2.getPage(i)
        pdf_writer.addPage(page)
    for i in range(pdf1.getNumPages()-n):
        page = pdf1.getPage(n+i)
        pdf_writer.addPage(page)
    return pdf_writer
def blank_pages(pdf,pg,n):
    aux=0
    for i in range(len(pg)):
        pdf_writer = PdfFileWriter()
        #hola mundo
        print('hoja:')
        print(n[i])
        for j in range(n[i]):
            pdf_writer.addBlankPage(width=612, height=792)
        save_pdf(pdf_writer,'auxi')
        pdf_aux = PdfFileReader(str(pdf_path)+'\\output\\auxi.pdf')
        print('pg+aux:')
        print(pg[i]+aux)
        save_pdf(introduce_pdf(pdf,pdf_aux,pg[i]+aux),'result')
        pdf = PdfFileReader(str(pdf_path)+'\\output\\result.pdf')
        aux+=n[i]
        print('contador:')
        print(aux)
    pdf=introduce_pdf(pdf,pdf_aux,n[i])
    save_pdf(pdf,'result')
        
    
    # pg=[0]+pg+[pdf.getNumPages()]
    # pdf_writer = PdfFileWriter()
    # for i in range(0,len(pg)-1):
    #     for j in range(pg[i+1]-pg[i]):
    #         page = pdf.getPage(pg[i]+j)
    #         pdf_writer.addPage(page)
    #     if i!=len(pg)-2:
    #         for j in range(n[i]):
    #             pdf_writer.addBlankPage()
    # with Path("chapter"+str(i+1)+".pdf").open(mode="wb") as output_file:
    #     pdf_writer.write(output_file)

def main():
    #n=input("\n\nPDFEdit.\n\nSelect any opction:\n 1.Split pdf by an array of pages")
    #delete_pdf('*.pdf')
    V=[2,5]
    n=[2,1]
    blank_pages(pdf_reader,V,n)
    
main()
