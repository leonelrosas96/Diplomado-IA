numero_secreto = 3

adivinado = False
while(adivinado == False):
    num = int(input('Introduzca un numero por favor: '))
    if (num == numero_secreto):
        print('Felicidades')
        adivinado = True
    else:
        print("Intentalo de nuevo")
