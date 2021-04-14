import random2
#variables para modificar el juego
posibilidades = 5
intentos = 0
limite = 15

print("What´s your name?")
name = input()
print("Let´s play a game " + name + " \nGuess a number between 1 to " + str(limite))
print("You´ve only have " + str(posibilidades) + " chances to guess the number")

#generamos un numero aleatorio entre 1 y 20
adivina = random2.randint(1, limite)
while intentos < posibilidades:
    
    num = int(input('intenta adivinar: '))

    if num == adivina:
        print('ganaste!')
        break
    if intentos == (posibilidades-1):
        break
    else:
        if num > adivina:
            print('intenta con un numero mas pequeño')
        else:
            print('intenta con un numero mas grande')
    
        intentos += 1
    if intentos == posibilidades-1:
        print('ultima oportunidad')
if num != adivina:
    print('game over!')

