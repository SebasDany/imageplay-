from distutils import command
from tkinter import *
import time
import Validacion
import datos
import os
import shutil
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from distutils import command
import shutil
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import Label,Tk
from PIL import Image, ImageTk
from tkinter import filedialog
objeto_validacion=Validacion.validacion()

global lista_de_textbox
lista_de_textbox = list()



#SELECCION DE IMAGEN


fecha=str(time.strftime("%d/%m/%y"))
def iniciar(contador=30):





    nombre_imagen = cajanombre.get()

    jugarcaja = cajaju.get()

    jugador = cajaju.get()
    imnom = cajanombre.get()
    print(imnom)
    datos.crerar_archivo(jugador, "4", imnom, fecha)

    proceso = 30
    variable=""

    if (nombre_imagen != variable  and jugarcaja != variable ):
      if(nombre_imagen.isalpha()  and jugarcaja.isalpha() ):

        cadena = ""
        nombre_imagen = cajanombre.get()
        objeto_validacion.set_nombre_imagen(nombre_imagen)
        texto = objeto_validacion.return_tamanio_de_palabra()
        for i in range(texto):
            cadena += "_ "

        if (contador == 30):
            global etiquetaTitulo
            etiquetaTitulo = Label(ventana, text=cadena,
                                   bg="teal", fg=colorFondo, width=40, font=("", "18"))
            etiquetaTitulo.place(x=30, y=10)

        time['text'] = contador
        proceso = time.after(1000, iniciar, (contador - 1))

        if (contador == 0):
            datos.crerar_archivo(jugador, proceso, imnom, fecha)
            datos.ventana(jugador, imnom, proceso, fecha, "you lost")
            cadena = ""
            for l in nombre_imagen:
                cadena += l
            etiquetaTitulo.config(text=cadena)
            # eliminar_text_boxs()
            time.after_cancel(proceso)


        if (contador == 25):
            cadena = ""

            for i in range(texto):
                if i == 0:
                    cadena += nombre_imagen[i]
                else:
                    cadena += " _ "

            etiquetaTitulo.config(text=cadena)
            # if (contador==15):
        if (contador == 20):

            cadena = ""
            for i in range(texto):
                if i == 0:
                    cadena += nombre_imagen[i]
                elif i == 1:
                    cadena += nombre_imagen[i]
                else:
                    cadena += " _ "

            etiquetaTitulo.config(text=cadena)

        if (contador == 10):
            cadena = ""

            for i in range(texto):
                if i == 0:
                    cadena += nombre_imagen[i]
                elif i == 1:
                    cadena += nombre_imagen[i]
                elif i == 2:
                    cadena += nombre_imagen[i]
                else:
                    cadena += " _ "

            etiquetaTitulo.config(text=cadena)

        if (contador == 1):
            cadena = ""

            for i in range(texto):
                if i == 0:
                    cadena += nombre_imagen[i]
                elif i == 1:
                    cadena += nombre_imagen[i]
                elif i == 2:
                    cadena += nombre_imagen[i]
                elif i == 3:
                    cadena += nombre_imagen[i]
                else:
                    cadena += " _ "

            etiquetaTitulo.config(text=cadena)

      else:
          messagebox.showerror("Error", "Por favor solo ingrese letras en los campos nombre del jugador y nombre imagen")
    else:
        messagebox.showerror("Error", "Por favor llene todos los campos")
def chose():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg .png .jpeg')])
    im = Image.open(path)
    imh = ImageTk.PhotoImage(file=path)

    w = Label(ventana, image=imh, width=400, height=610)
    w.image=imh
    w.place(x=20, y=60)
    im1 = PhotoImage(file="nula.png")
    etiqueta1 = Label(ventana, image=im1, width=200, height=200).place(x=220, y=60)
    etiqueta1.image=im1
    #etiqueta2 = Label(ventana, image=im1, width=200, height=200).place(x=20, y=60)
    #etiqueta2.image = im1

    #etiqueta3 = Label(ventana, image=im1, width=200, height=200).place(x=20, y=260)
    #etiqueta3.image = im1

    #etiqueta4 = Label(ventana, image=im1, width=200, height=200).place(x=20, y=463)
    #etiqueta4.image = im1

   # etiqueta5 = Label(ventana, image=im1, width=200, height=200).place(x=220, y=463)
    #etiqueta5.image = im1

    #w.pack()

#CENTRAR VENTANA
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








def anadir_descripcion():
    descripcion_imagen = cajadescripcion.get()
    objeto_validacion.set_descripcion_imagen(descripcion_imagen)
#INTERFAZ
ventana = Tk()
#############Objeto validacion




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
ventana.geometry("820x698")
ventana.configure(background = colorFondo)
etiquetaTitulo= Label(ventana, text="BIENVENIDO",
                      bg="teal", fg=colorFondo,width=60).place(x=190,y=10)

etiquetajug = Label(ventana, text="NOMBRE DEL JUGADOR", bg=colorFondo,
                  fg=colorLetra,width=35, height=1).place(x=450, y=50)
#---->
cajaju = Entry(ventana, width=46)
cajaju.place(x=450, y=70)

botonInIma = Button(ventana, text="INSERTAR UNA IMAGEN DE TU PC", command=chose, bg=colorBotones, width=40, height=1,
                    fg=colorLetra).place(x=450, y=100)


etiquetaT1 = Label(ventana, text="NOMBRE DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=35, height=1).place(x=450, y=150)
#---->
cajanombre = Entry(ventana,  width=46)
cajanombre.place(x=450, y=175)



etiquetaT2 = Label(ventana, text="DESCRIPCIÓN DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=36, height=1).place(x=450, y=250)
#---->
cajadescripcion = Entry(ventana, width=46 )
cajadescripcion.place(x=450, y=275)





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

botoFinaliza = Button(ventana, text="FINALIZAR", bg=colorBotones,width=20, height=1,
                       fg=colorLetra).place(x=610, y=665)
botoIntentar = Button(ventana, text="INICIAR", bg=colorBotones,width=20, height=1,
                       fg=colorLetra,command=iniciar).place(x=450, y=665)
cajares = Entry(ventana, width=46)
cajares.place(x=450, y=550)
botonprobar = Button(ventana, text="Probar", bg=colorBotones,width=20, height=1,
                       fg=colorLetra).place(x=450, y=600)


#REEMPLAZO DE IMAGEN
label_principal=Label(ventana,width=60,height=70)
label_principal.place(x=20,y=60)
label_principal.pack
imh = PhotoImage(file="descarga.png")
cron = Label(ventana, text="Time:",
                 fg=colorFondo,font=("", "18")).place(x=620, y=10)
time = Label(ventana, fg='red', width=5, font=("", "18"))
time.place(x=700, y=10)
ventana.title("wm min/max")

# this removes the maximize button
ventana.resizable(0,0)

center(ventana)
mainloop()


