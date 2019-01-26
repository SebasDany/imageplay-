from distutils import command
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename


def chose():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)
    a=filename
    imh = PhotoImage(file=a)
    w = Label(ventana, image=imh, width=400, height=610).place(x=20, y=60)
    im1 = PhotoImage(file="nula.png")
    etiqueta = Label(ventana, image=im1, width=200, height=200).place(x=220, y=60)

    im3 = PhotoImage(file="nula.png")
    etiqueta = Label(ventana, image=im3, width=200, height=200).place(x=20, y=60)
    im2 = PhotoImage(file="nula.png")
    etiqueta = Label(ventana, image=im2, width=200, height=200).place(x=20, y=260)
    im4 = PhotoImage(file="nula.png")
    etiqueta = Label(ventana, image=im4, width=200, height=200).place(x=20, y=463)
    im5 = PhotoImage(file="nula.png")
    etiqueta = Label(ventana, image=im5, width=200, height=200).place(x=220, y=463)
    w.pack()


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

ventana = Tk()

genero = StringVar()
titulo = StringVar()
descripcion = StringVar()
duracion = StringVar()
anio = StringVar()
conteliminar = StringVar()
colorFondo = "WHITE"
colorLetra = "BLACK"
colorBotones = "SpringGreen3"
ventana.title("Imge Play")
ventana.geometry("800x698")
ventana.configure(background = colorFondo)
etiquetaTitulo= Label(ventana, text="Bienvenido",
                      bg="teal", fg=colorFondo,width=60).place(x=190,y=10)
botonSeIma = Button(ventana, text="SELECCIONAR UNA IMAGEN", command=chose, bg=colorBotones, width=40, height=1,
                    fg=colorLetra).place(x=450, y=60)
botonInIma = Button(ventana, text="INSERTAR UNA IMAGEN DE TU PC", command=chose, bg=colorBotones, width=40, height=1,
                    fg=colorLetra).place(x=450, y=100)


etiquetaT1 = Label(ventana, text="NOMBRE DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=35, height=1).place(x=450, y=150)

cajanombre = Text(ventana, height=1, width=36).place(x=450, y=175)


botoimagenins = Button(ventana, text="AÑADIR NOMBRE DE LA  IMAGEN", bg=colorBotones,width=40, height=1,
                       fg=colorLetra).place(x=450, y=200)

etiquetaT2 = Label(ventana, text="DESCRIPCIÓN DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=36, height=1).place(x=450, y=250)

cajadescripcion = Text(ventana, height=1, width=36).place(x=450, y=275)

botoimagendes = Button(ventana, text="AÑADIR DESCRIPCIÓN DE LA IMAGEN", bg=colorBotones,width=40, height=1,
                       fg=colorLetra).place(x=450, y=300)
etiquetaT3 = Label(ventana, text="Complete en  la parte de abajo\n el nombre de la imagen \n correspondiente para que así\n vaya destapando la imagen poco a poco :)", bg=colorFondo,
                  fg=colorLetra,width=50, height=5).place(x=400, y=330)

etiquetaT3 = Label(ventana, text="Descripción de la Imagen: ", bg=colorFondo,
                  fg=colorLetra,width=50, height=1).place(x=400, y=410)

etiquetaT3 = Label(ventana, text="Universidad del Ecuador ", bg=colorFondo,
                  fg=colorLetra,width=50, height=5).place(x=400, y=430)





cajajugar =  Text(ventana, height=5, width=36).place(x=450, y=550)
botoFinaliza = Button(ventana, text="FINALIZAR", bg=colorBotones,width=20, height=1,
                       fg=colorLetra).place(x=610, y=665)
botoIntentar = Button(ventana, text="VOLVER A INTENTAR", bg=colorBotones,width=20, height=1,
                       fg=colorLetra).place(x=450, y=665)


im=PhotoImage(file="descarga.png")
fond=Label(ventana,image=im,  width=400,height=610).place(x=20,y=60)
im1=PhotoImage(file="nula.png")
etiqueta=Label(ventana,image=im1,  width=200,height=200).place(x=220,y=60)

im3=PhotoImage(file="nula.png")
etiqueta=Label(ventana,image=im3,  width=200,height=200).place(x=20,y=60)
im2=PhotoImage(file="nula.png")
etiqueta=Label(ventana,image=im2,  width=200,height=200).place(x=20,y=260)
im4=PhotoImage(file="nula.png")
etiqueta=Label(ventana,image=im4,  width=200,height=200).place(x=20,y=463)
im5=PhotoImage(file="nula.png")
etiqueta=Label(ventana,image=im5,  width=200,height=200).place(x=220,y=463)

center(ventana)
mainloop()
