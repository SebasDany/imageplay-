from distutils import command
from tkinter import *
import time
import Validacion
import Datos
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
def llenarcampodescrip():
    valordes=cajadescripcion.get()
    return valordes

def finalizar():
    Datos.crerar_archivo(jugador, proceso, imnom, fecha)
    Datos.ventana(jugador, imnom, proceso, fecha, "you lost")

    time.after_cancel(proceso)
    toggle_entry()

def autores():
       messagebox.showinfo("Autores","Sebastián Guandinango, Fausto Borja, Fabián Garrido")

#SELECCION DE IMAGEN
def probar():
    global proceso
    a=cajanombre.get()
    b=cajares.get()
    if ( cajanombre.get()==cajares.get()):

        time.after_cancel(proceso)
        Datos.ventana(cajaju.get(), cajanombre.get(), proceso, fecha, "Winner")
        toggle_entry()
    else:
        etiquetaintente = Label(ventana, text="INTENTE OTRA VEZ :)", bg="BLACK",
                            fg="white", width=40, height=1)
        etiquetaintente.place(x=450, y=610)


def toggle_entry():
    global hidden
    if hidden:
        cajanombre.place(x=450, y=120)
        cajadescripcion.place(x=450, y=180)
    else:
        cajanombre.place_forget()
        cajadescripcion.place_forget()
    hidden = not hidden

def imagen1():
    llenarcampodescrip()
    etiqueta1.place_forget()

def imagen2():
    etiqueta2.place_forget()

def imagen3():
    etiqueta3.place_forget()

def imagen4():
    etiqueta4.place_forget()

def imagen5():
    etiqueta5.place_forget()




fecha=str(time.strftime("%d/%m/%y"))
def iniciar(contador=30):

    global proceso



    nombre_imagen = cajanombre.get()

    jugarcaja = cajaju.get()
    global jugador
    global imnom
    jugador = cajaju.get()
    imnom = cajanombre.get()

    Datos.crerar_archivo(jugador, "4", imnom, fecha)

    proceso = 30
    variable=""

    if (nombre_imagen!=variable and jugarcaja != variable ):
      if(nombre_imagen.isalpha()  and jugarcaja.isalpha() ):

        cadena = ""
        nombre_imagen = cajanombre.get()
        global etiquetasobre




        objeto_validacion.set_nombre_imagen(nombre_imagen)
        texto = objeto_validacion.return_tamanio_de_palabra()
        for i in range(texto):
            cadena += "_ "

        if (contador == 30):
            anadir_descripcion()
            txtdesi = Frame(ventana, borderwidth=1, relief="sunken")

            txtodesi = Text(txtdesi, wrap=NONE, height=1, width=34, borderwidth=1)
            vscrolldei = Scrollbar(txtdesi, orient=HORIZONTAL, command=txtodesi.xview)
            vscrolldei01 = Scrollbar(txtdesi, orient=VERTICAL, command=txtodesi.yview)
            txtodesi['xscrollcommand'] = vscrolldei.set
            txtodesi['yscrollcommand'] = vscrolldei01.set
            vscrolldei.pack(side="bottom", fill="x")
            vscrolldei01.pack(side="right", fill="y")
            txtodesi.pack(side="left", fill="both", expand=True)

            txtodesi.insert(INSERT, objeto_validacion.get_descripcion_imagen())
            txtdesi.place(x=450, y=455)
            txtodesi.tag_add("here", "1.0", "7.4")
            txtodesi.tag_add("start", "1.8", "1.13")
            txtodesi.tag_config("here", background="black", foreground="white")
            txtodesi.config(state=DISABLED)
            var = objeto_validacion.get_descripcion_imagen()



            mostrar_imagenes()
            toggle_entry()
            global etiquetaTitulo
            etiquetaTitulo = Label(ventana, text=cadena,bg="teal", fg=colorFondo, width=30, font=("", "18"))
            etiquetaTitulo.place(x=20, y=10)


        time['text'] = contador
        proceso = time.after(1000, iniciar, (contador - 1))

        if (contador == 0):
            toggle_entry()
            Datos.crerar_archivo(jugador, proceso, imnom, fecha)
            Datos.ventana(jugador, imnom, proceso, fecha, "you lost")
            cadena = ""
            for l in nombre_imagen:
                cadena += l
            etiquetaTitulo.config(text=cadena)
            # eliminar_text_boxs()
            time.after_cancel(proceso)


        if (contador == 25):

            imagen1()
            cadena = ""

            for i in range(texto):
                if i == 0:
                    cadena += nombre_imagen[i]
                else:
                    cadena += " _ "

            etiquetaTitulo.config(text=cadena)
            # if (contador==15):
        if (contador == 20):
            imagen2()
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
            imagen3()
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

        if (contador == 3):
            imagen4()
        if (contador == 1):


            imagen5()
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


def mostrar_imagenes():

    etiqueta1.place(x=20, y=470)
    etiqueta2.place(x=20, y=60)
    etiqueta3.place(x=241, y=470)
    etiqueta4.place(x=241, y=60)
    etiqueta5.place(x=20, y=265)


def chose():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing

    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg .png .jpeg')])
    im = Image.open(path)
    imh = ImageTk.PhotoImage(file=path)
    w.configure(image=imh)
    w.image=imh






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
hidden = False
ventana = Tk()
#############Objeto validacion
imh12 = PhotoImage(file="azules.png")
fo = Label(ventana, image=imh12, width=980, height=675)
fo.image=imh12
fo.place(x=0, y=0)


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
ventana.geometry("770x675")
ventana.configure(background = colorFondo)
etiquetaTitulo= Label(ventana, text=" Aquí se muestra  una pista de la Palabrita",
                      bg="teal", fg=colorFondo,width=38,font=("", "14")).place(x=20,y=10)

etiquetajug = Label(ventana, text="NOMBRE DEL JUGADOR", bg=colorFondo,
                  fg=colorLetra,width=40, height=1).place(x=450, y=210)
#---->
cajaju = Entry(ventana, width=47)
cajaju.place(x=450, y=240)

botonInIma = Button(ventana, text="INSERTAR UNA IMAGEN DE TU PC", command=chose, bg=colorBotones, width=39, height=1,
                    fg=colorLetra).place(x=450, y=60)


etiquetaT1 = Label(ventana, text="NOMBRE DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=40, height=1).place(x=450, y=90)
#---->
global cajanombre
cajanombre = Entry(ventana,  width=47)
cajanombre.place(x=450, y=120)



etiquetaT2 = Label(ventana, text="DESCRIPCIÓN DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=40, height=1).place(x=450, y=150)
#---->
cajadescripcion = Entry(ventana, width=47 )
cajadescripcion.place(x=450, y=180)


etiquetaQUE = Label(ventana, text="¿QUE SE DEBE HACER?", bg=colorFondo,
                  fg=colorLetra,width=40, height=1).place(x=450, y=290)


#ayuda para jugar básica
txtFrameinstruc = Frame(ventana, borderwidth=1, relief="sunken")
txtinstruc = Text(txtFrameinstruc, wrap = NONE, height = 4, width = 34, borderwidth=1)
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
txtinstruc.tag_config("here", background="black", foreground="white")
txtinstruc.config(state=DISABLED)
etiquetaT3 = Label(ventana, text="DESCRIPCIÓN DE LA IMAGEN: ", bg=colorFondo,
                  fg=colorLetra,width=40, height=1)
etiquetaT3.place(x=450, y=430)

#Descripcion de la imagen




etiquetaT4 = Label(ventana, text="ADIVINA: ", bg=colorFondo,
                  fg=colorLetra,width=40, height=1).place(x=450, y=530)

cajares = Entry(ventana, width=47)
cajares.place(x=450, y=560)







#ADIVINA LA PALABRA

botoFinaliza = Button(ventana, text="FINALIZAR", bg=colorBotones,width=17, height=1,
                       fg=colorLetra,command=finalizar).place(x=610, y=650)
botoIntentar = Button(ventana, text="INICIAR JUEGO", bg=colorBotones,width=20, height=1,
                       fg=colorLetra,command=iniciar).place(x=450, y=650)

botonprobar = Button(ventana, text="PROBAR PALABRA INGRESADA", command=probar, bg=colorBotones,width=40, height=1,
                       fg=colorLetra).place(x=450, y=588)
botonautores = Button(ventana, text="AUTORES", command=autores, bg=colorBotones,width=40, height=1,
                       fg=colorLetra).place(x=450, y=615)




#REEMPLAZO DE IMAGEN
label_principal=Label(ventana,width=60,height=70)
label_principal.place(x=20,y=60)
label_principal.pack
#imh = PhotoImage(file="descarga.png")




cron = Label(ventana, text="Time:",
                 fg=colorFondo,font=("", "18")).place(x=590, y=10)
time = Label(ventana, fg='red', width=5, font=("", "18"))
time.place(x=660, y=10)


im=PhotoImage(file="nula.png")
w = Label(ventana,image=im, width=423, height=610)

w.place(x=20, y=60)

im1 = PhotoImage(file="nula.png")
etiqueta1 = Label(ventana, image=im1, width=225, height=200)
etiqueta2 = Label(ventana, image=im1, width=225, height=205)
etiqueta3 = Label(ventana, image=im1, width=200, height=200)
etiqueta4 = Label(ventana, image=im1, width=200, height=200)
etiqueta5 = Label(ventana, image=im1, width=225, height=205)





# this removes the maximize button
ventana.resizable(0,0)

center(ventana)
mainloop()


