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






