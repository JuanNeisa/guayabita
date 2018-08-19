import random

##Retorna un numero aleatorio entre 1 y 6
def lanzar():
    return random.randint(1,6)

## Retorna un numero aleatorio entre 1 y 10, luego lo multiplica por 100
def apuesta():
    return (random.randint(1,10) * 100)

##Es la segunda apuesta, cuando se saca un numero entre 2 y 5 en el primer lanzamiento, cuando juego contra lo que hay en la mesaa
def reApuesta(mesa, apuesta, dado1, dado2):

    print("Segundo lanzamiento: " , dado2)

    if(dado1 < dado2 ):
    
        if(mesa > apuesta):
            return apuesta
        else:
            reApuesta(mesa, apuesta())
            return

##Numero aleatorio entre 5 y 15, luego lo multiplica por 100. Es el dinero que posee un jugador
def jugador():
    return (random.randint(5,15) * 100)

##Definicion del turno de cualquiera de los 2 jugarores
def turno(dado, apuesta, j1, mesa):
    print("Dado: " , dado)

    ##Caso 1: numero 1 gana
    if(dado == 1):
        print("Has perdido " , apuesta)
        mesa + apuesta
        return (j1 - apuesta)

    ##Caso 2: numero 6 gana
    elif (dado == 6):
        print("Has ganado " , apuesta)
        mesa - apuesta
        return (j1 + apuesta)

    ##Caso 3: numeros entre 2 y 5 juegan de nuevo
    else:
        if(mesa < apuesta):
            print("No hay dinero suficiente, pero GANASTE")
            return
        else:
            reApuesta(mesa,apuesta(),dado, lanzar())

##Definicion del juego dependiendo el monto de dinero de cada uno
def jugar(j1,j2, apuesta, mesa):
    print("JUGADOR 1")

    ##HAcer el juego iterativo hasta que se acabe el dinero de alguno de los dos jugadores(No funciona correctamente)
    while x != 0:
        if(j1>0):
            turno(lanzar(),apuesta, j1, mesa)
        elif(j2>0):
            turno(lanzar(),apuesta, j2, mesa)
        else:
            print("Fin del juego")
            return 0

##Ejecutar la primera funcion que alberga todas las demas
jugar(jugador(), jugador(),apuesta(), 0 )
