from distutils import command
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename

def chose():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)

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
botoGuardar = Button(ventana, text="SELECCIONANR UNA IMAGEN",command=chose, bg="#009",width=35, height=1,
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

botoConsultar = Button(ventana, text="Guardar", bg="#009",width=35, height=1,
                       fg="white").place(x=450, y=350)
botoConsultar = Button(ventana, text="SALIR", bg="#009",width=35, height=1,
                       fg="white").place(x=450, y=400)

im=PhotoImage(file="descarga.png")
fond=Label(ventana,image=im,  width=400,height=400).place(x=20,y=60)


mainloop()
