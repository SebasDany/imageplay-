import datetime, time
##SEBASTIAN GUANDINANGO



def crerar_archivo(nombre,tiempo,nomimag):
    print('Mi mimbre:',nombre)
    print('Su tipo es:', tiempo)
    fout = open("registros.txt", "w")
    fout.write('JUGADOR : '+ nombre+'\n')

    fout.write('TIEMPO : ' + tiempo + '\n')
    fout.write('NOMBRE DE LA IMAGEN : ' + nomimag + '\n')
    fout.close()
def cromometro():
    suma = 0
    while (suma <= 10):
        print("segundos:", suma)
        suma = suma + 1
        time.sleep(1)


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

def iniciar(contador=0):
    proceso = 0
    time['text'] = contador
    proceso = time.after(1000, iniciar, (contador + 1))
    if (contador == 10):
        time.after_cancel(proceso)





