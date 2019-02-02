from distutils import command
from tkinter import *
#import datos
#import pro
import datetime, time
#datos.crerar_archivo('fsdgdsgdfg','dfbdbfdbdfbb','145657687')

import os
import shutil
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import Label,Tk
from PIL import Image, ImageTk
from tkinter import filedialog
#SELECCION DE IMAGEN


def iniciarggg():
    cron = Label(ventana, text="TIEMPO",
                 fg=colorFondo).place(x=350, y=40)
    suma = 0
    while (suma <= 10):
        print(suma)
        Entry(ventana, textvariable=suma).place(x=170, y=70)
        suma = suma + 1
        time.sleep(1)





def chose():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    #filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg .png .jpeg')])
    im = Image.open(path)
    imh = ImageTk.PhotoImage(file=path)



    w = Label(ventana, image=imh, width=400, height=610)
    w.image=imh
    w.place(x=20, y=60)
    im1 = PhotoImage(file="nula.png")
    etiqueta1 = Label(ventana, image=im1, width=200, height=200).place(x=220, y=60)
    etiqueta1.image=im1
    etiqueta2 = Label(ventana, image=im1, width=200, height=200).place(x=20, y=60)
    etiqueta2.image = im1

    etiqueta3 = Label(ventana, image=im1, width=200, height=200).place(x=20, y=260)
    etiqueta3.image = im1

    etiqueta4 = Label(ventana, image=im1, width=200, height=200).place(x=20, y=463)
    etiqueta4.image = im1

    etiqueta5 = Label(ventana, image=im1, width=200, height=200).place(x=220, y=463)
    etiqueta5.image = im1

    #w.pack()

#CENTRAR VENTANA



def iniciar(contador=10):
    proceso = 10
    time['text'] = contador
    proceso = time.after(1000, iniciar, (contador - 1))
    if (contador == 0):
        time.after_cancel(proceso)


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


#INTERFAZ
ventana = Tk()

genero = StringVar()
titulo = StringVar()
descripcion = StringVar()
duracion = StringVar()
anio = StringVar()
conteliminar = StringVar()
colorFondo = "orange"
colorLetra = "BLACK"
colorBotones = "SpringGreen3"
ventana.title("Image Play")
ventana.geometry("800x698")
ventana.configure(background = colorFondo)
etiquetaTitulo= Label(ventana, text="BIENVENIDO",
                      bg="teal", fg=colorFondo,width=60).place(x=190,y=10)





botonInIma = Button(ventana, text="INSERTAR UNA IMAGEN DE TU PC", command=chose, bg=colorBotones, width=40, height=1,
                    fg=colorLetra).place(x=450, y=100)


etiquetaT1 = Label(ventana, text="NOMBRE DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=35, height=1).place(x=450, y=150)

cajanombre = Text(ventana, height=1, width=36 , borderwidth=2).place(x=450, y=175)


botoimagenins = Button(ventana, text="AÑADIR NOMBRE DE LA  IMAGEN", bg=colorBotones,width=40, height=1,
                       fg=colorLetra).place(x=450, y=200)

etiquetaT2 = Label(ventana, text="DESCRIPCIÓN DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=36, height=1).place(x=450, y=250)

cajadescripcion = Text(ventana, height=1, width=36 , borderwidth=2).place(x=450, y=275)

botoimagendes = Button(ventana, text="AÑADIR DESCRIPCIÓN DE LA IMAGEN", bg=colorBotones,width=40, height=1,
                       fg=colorLetra).place(x=450, y=300)



#ayuda para jugar básica
txtFrameinstruc = Frame(ventana, borderwidth=1, relief="sunken")
txtinstruc = Text(txtFrameinstruc, wrap = NONE, height = 4, width = 36, borderwidth=1)
vscroll = Scrollbar(txtFrameinstruc, orient=HORIZONTAL, command=txtinstruc.xview)
vscroll01 = Scrollbar(txtFrameinstruc, orient=VERTICAL, command=txtinstruc.yview)
txtinstruc['xscrollcommand'] = vscroll.set
txtinstruc['yscrollcommand'] = vscroll01.set
vscroll.pack(side="bottom", fill="x")
vscroll01.pack(side="right", fill="y")
txtinstruc.pack(side="left", fill="both", expand=True)
txtinstruc.insert(INSERT, "Complete en  la parte de abajo el nombre :)\nde la imagen  correspondiente para que así vaya\ndestapando la imagen poco a poco :) :) \n\n")
txtFrameinstruc.place(x=450, y=330)
txtinstruc.tag_add("here", "1.0", "7.4")
txtinstruc.tag_add("start", "1.8", "1.13")
txtinstruc.tag_config("here", background=colorBotones, foreground="blue")

etiquetaT3 = Label(ventana, text="DESCRIPCIÓN DE LA IMAGEN: ", bg=colorFondo,
                  fg=colorLetra,width=50, height=1).place(x=410, y=430)

#Descripcion de la imagen
txtdesi = Frame(ventana, borderwidth=1, relief="sunken")
txtodesi = Text(txtdesi, wrap = NONE, height = 1, width = 36, borderwidth=1)
vscrolldei = Scrollbar(txtdesi, orient=HORIZONTAL, command=txtodesi.xview)
vscrolldei01 = Scrollbar(txtdesi, orient=VERTICAL, command=txtodesi.yview)
txtodesi['xscrollcommand'] = vscrolldei.set
txtodesi['yscrollcommand'] = vscrolldei01.set
vscrolldei.pack(side="bottom", fill="x")
vscrolldei01.pack(side="right", fill="y")
txtodesi.pack(side="left", fill="both", expand=True)
txtodesi.insert(INSERT, "UNIVERSIDAD POLITÉCNICA SALESIANA")
txtdesi.place(x=450, y=455)
txtodesi.tag_add("here", "1.0", "7.4")
txtodesi.tag_add("start", "1.8", "1.13")
txtodesi.tag_config("here", background=colorBotones, foreground="blue")



etiquetaT4 = Label(ventana, text="ADIVINA: ", bg=colorFondo,
                  fg=colorLetra,width=50, height=1).place(x=410, y=530)





#ADIVINA LA PALABRA
cajajugar =  Text(ventana, height=5, width=38, borderwidth=2).place(x=450, y=550 )
botoFinaliza = Button(ventana, text="FINALIZAR", bg=colorBotones,width=20, height=1,
                       fg=colorLetra).place(x=610, y=665)
botoIntentar = Button(ventana, text="iniciar", bg=colorBotones,width=20, height=1,command=iniciar,
                       fg=colorLetra).place(x=450, y=665)


#REEMPLAZO DE IMAGEN

cron = Label(ventana, text="Time:",
                 fg=colorFondo).place(x=650, y=10)
time = Label(ventana, fg='red', width=5, font=("", "18"))
time.place(x=650, y=40)


# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
# iniciar()

# Generamos un frame para poner los botones de iniciar y parar

center(ventana)
mainloop()
