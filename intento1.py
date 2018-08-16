import random

def lanzar():
    return random.randint(1,6)

def apuesta():
    return (random.randint(1,10) * 100)

def reApuesta(mesa, apuesta, dado1, dado2):

    if(dado1 < dado2 ):
    
        if(mesa > apuesta):
            return apuesta
        else:
            reApuesta(mesa, apuesta())
            return
       
    

def jugador():
    return (random.randint(5,15) * 100)

##def segundoturno(apuesta,mesa,  dado, primerTurno):
##    if(dado > primerTurno):
##        print("HAZ GANADO " , apuesta)

def validar(dado, apuesta, j1, mesa):
    print("Dado: " , dado)

    if(dado == 1):
        print("Has perdido " , apuesta)
        mesa + apuesta
        return (j1 - apuesta)

    elif(dado == 6):

        if(mesa < apuesta):
            print("No hay dinero suficiente, pero GANASTE")
            return
        else:
            print("Has ganado " , apuesta)
            mesa - apuesta
            return (j1 + apuesta)


