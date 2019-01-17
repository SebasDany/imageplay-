from tkinter import *
from tkinter import messagebox
from tkinter import ttk

ventana = Tk()

genero = StringVar()
titulo = StringVar()
descripcion = StringVar()
duracion = StringVar()
anio = StringVar()
conteliminar = StringVar()
colorFondo = "BLACK"
colorLetra = "WHITE"
ventana.title("CINE PELIS")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)
etiquetaTitulo= Label(ventana, text="REGISTRO PELICULAS",
                      bg="red", fg=colorFondo,width=50).place(x=150,y=10)
etiquetaG= Label(ventana, text="Genero", bg=colorFondo,
                 fg=colorLetra).place(x=50, y=50)
combo= ttk.Combobox(ventana,textvariable=genero,width=47)
combo.place(x=150, y=50)


etiquetaT = Label(ventana, text="Titulo", bg=colorFondo,
                  fg=colorLetra).place(x=50, y=80)
cajaT = Entry(ventana, textvariable=titulo, width=50).place(x=150, y=80)
etiquetaD = Label(ventana, text="Descripcion", bg=colorFondo,
                  fg=colorLetra).place(x=50, y=110)
cajaD = Entry(ventana, textvariable=descripcion,width=50).place(x=150, y=110)
etiquetaAnio = Label(ventana, text="Anio", bg=colorFondo,
                  fg=colorLetra).place(x=50, y=140)
cajaAnio = Entry(ventana, textvariable=anio,width=50).place(x=150, y=140)
etiquetaDura = Label(ventana, text="Duracion", bg=colorFondo,
                  fg=colorLetra).place(x=50, y=170)
cajaDura = Entry(ventana, textvariable=duracion,width=50).place(x=150, y=170)
botoGuardar = Button(ventana, text="Guardar   ", bg="#009",
                     fg="White").place(x=480, y=100)
botoConsultar = Button(ventana, text="Consultar", bg="#009",
                       fg="white").place(x=480, y=150)
r = Text(ventana, width=80, height=15)
r.insert(INSERT, "IMAGE")
r.place(x=20, y=230)
mainloop()
