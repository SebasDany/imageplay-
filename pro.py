from tkinter import Tk, Label, Button, Frame

proceso = 0

def iniciar(contador=0):
    global proceso

    # mostramos la variable contandor
    time['text'] = contador

    # hacemos un llamamient a la funcion mostrarContador pasando el
    # contador mas uno
    proceso = time.after(1000, iniciar, (contador + 1))


def parar():
    global proceso
    time.after_cancel(proceso)


root = Tk()
root.title('Cronometro')

time = Label(root, fg='red', width=20, font=("", "18"))
time.pack()

# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
# iniciar()

# Generamos un frame para poner los botones de iniciar y parar
frame = Frame(root)
btnIniciar = Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnParar = Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=2)
frame.pack()

root.mainloop()