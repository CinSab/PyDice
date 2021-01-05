from random import * # Importamos el modulo random

def numRand(min,max):  # Definimos una funcion propia
    return randint(min,max)     # Retornamos un numero aleatorio

trys=0   # Declaramos un acumulador

print('Bienvenido! Las reglas de este juego son sencillas, cuando los valores de ambos dados de como resultado 4 usted gana, de lo contrario, vuelva a intentar!')
input('Presione ENTER para comenzar!') #Definimos input para comenzar el juego.

while True: #Bucle a repetir para jugar indefinidamente
    resultado = randint(1,6)
    resultado2 = randint(1,6)
    if(resultado + resultado2) != 4: #Comparamos los resultados random diferentes a 4
        print('La suma de los dados (',resultado,'+',resultado2,') no es igual a 4, perdes esta ronda')
        trys += 1

    else:  #Cuando el valor random es igual a 4, se ejecuta este bloque
        print('La suma de los dados (',resultado,'+',resultado2,')es igual a 4, ganas la partida. Sus intentos fueron: ',trys)
        trys = 0
    
    input('Presione ENTER para voler a intentar!') #Declara el reinicio del juego
    continue #Utilizamos continue para poder seguir jugando
