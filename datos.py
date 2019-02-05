import datetime, time
from tkinter import *

##SEBASTIAN GUANDINANGO


import time
from tkinter import messagebox
def crerar_archivo(nombre,tiempo,nomimag,fecha):
    print('Mi mimbre:',nombre)
    print('Su tipo es:', tiempo)
    fout = open("registros.txt", "w")
    fout.write('JUGADOR : '+nombre+'\n')
    fout.write('TIEMPO : ' + tiempo + '\n')
    fout.write('NOMBRE DE LA IMAGEN : ' + nomimag + '\n')
    fout.write('FACHA : ' + fecha + '\n')


    fout.close()

def iniciar(contador=2):
    proceso = 2
    time['text'] = contador
    proceso = time.after(1000, iniciar, (contador - 1))
    if (contador == 0):
        time.after_cancel(proceso)
        v = Tk()

        v.title("Image Play")
        v.configure(background="black")
        v.geometry("300x100")
        lbl = Label(v, text=" ** You Lost ** ",font=("", "30"),background="black")
        lbl.grid(column=0, row=0)
        v.mainloop()

def ventana( n,d,g,j, title):
    v = Tk()
    v.title("Image Play")
    v.configure(background="black")
    v.geometry("300x200")
    lbl = Label(v, text=title, font=("", "30"), fg="orange", background="black").place(x=30, y=10)
    lbl = Label(v, text="JUGADOR : " + n, fg="orange", background="black").place(x=30, y=60)
    lb = Label(v, text="IMAGEN : " + d, fg="orange", background="black").place(x=30, y=80)
    l = Label(v, text="TIEMPO : " + g, fg="orange", background="black").place(x=30, y=100)
    k = Label(v, text="FECHA : " + j, fg="orange", background="black").place(x=30, y=120)

def comparar( respuesta, monim):

    if (respuesta.lower()==monim.lower()):


        #datos.crerar_archivo(jugador, contador, imnom, fecha)
        #datos.ventana(jugador, imnom, contador, fecha, "Winenr")
        print("es corecto")
    else:
        print("intentelo denuevo")


