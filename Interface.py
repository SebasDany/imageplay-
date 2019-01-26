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
ventana.title("Imge Play")
ventana.geometry("800x500")
ventana.configure(background = colorFondo)
etiquetaTitulo= Label(ventana, text="Bienvenido",
                      bg="red", fg=colorFondo,width=60).place(x=150,y=10)
botoGuardar = Button(ventana, text="SELECCIONANR UNA IMAGEN", bg="#009",width=35, height=1,
                     fg="White" ).place(x=450, y=100)


etiquetaT = Label(ventana, text="NOMBRE DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=35, height=1).place(x=450, y=150)
cajaT = Entry(ventana, textvariable=titulo, width=40).place(x=450, y=175)


botoConsultar = Button(ventana, text="AÑADIR NOMBRE DE LA  IMAGEN", bg="#009",width=35, height=1,
                       fg="white").place(x=450, y=200)
etiquetaT = Label(ventana, text="DESCRIPCION DE LA IMAGEN", bg=colorFondo,
                  fg=colorLetra,width=35, height=1).place(x=450, y=250)
cajaT = Entry(ventana, textvariable=titulo, width=40).place(x=450, y=275)

botoConsultar = Button(ventana, text="AÑADIR DESCRIPCION  IMAGEN", bg="#009",width=35, height=1,
                       fg="white").place(x=450, y=300)

botoConsultar = Button(ventana, text="INICIAR", bg="#009",width=35, height=1,
                       fg="white").place(x=450, y=350)
botoConsultar = Button(ventana, text="SALIR", bg="#009",width=35, height=1,
                       fg="white").place(x=450, y=400)

r = Text(ventana, width=50 )
r.insert(INSERT, "IMAGE")
r.place(x=20, y=60)
mainloop()
