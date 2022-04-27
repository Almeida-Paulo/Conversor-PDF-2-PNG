# Para transformar em .exe necessita que a versão do python instalado na máquina seja a mesma utilizada para a criação do código (versão suportada pelas bibliotecas em uso!!!!)
from tkinter import *
from tkinter.filedialog import askopenfilenames 
import fitz #mudou de nome

root = Tk()
root.geometry('400x200')
root.title("Agnus Converter")

def select__PDF_file():
    global pdf_file
    global pdf_name
    global page
    global pix_page
    global matriz
    global directory_
    pdf_name = askopenfilenames(initialdir="/", title="Selecionar Arquivos") # uma lista com os nomes # ou askopenfilename, para apenas um nome
    pdf_file = fitz.open(str(pdf_name[0])) # com askopenfilenames é desnecessário [0] para selecionar o primeiro elemento
    page = pdf_file.load_page(None)
    matriz = fitz.Matrix(4, 4)
    pix_page = page.get_pixmap(matrix=matriz)
    if pdf_name != ():
        directory_ = str(pdf_name[0])
        Label(root, text=directory_, font="normal 10 bold").pack(pady=10)
    else:
        None
    return pix_page

def pdf_to_image():
    pix_page.save('{}.png'.format(directory_)) # o que está em directory_ será onde estão as chaves {}
    return None

Label(root, text="Conversor: .pdf para .png", font="normal 15 bold").pack(pady=10)

Button(root, text="Selecionar Arquivos", relief="solid", command=select__PDF_file, font=14).pack(pady=10)
Button(root, text="Converter", relief="solid", command=pdf_to_image, bg="white", font=15).pack(pady=10)

root.mainloop()
