import random

limite = 10
chances_restantes = 3
numero_secreto = random.randint(1,limite)
acertou = False

while acertou == False and chances_restantes > 0:
    chute = int(input(f'Digite um número entre 1 e {limite} \n'))
    chances_restantes -= 1

    if chute == numero_secreto:
        acertou = True
    else: 
       if numero_secreto > chute:
        print('O número secreto é maior')
       else:
        print('O número secreto é menor')

if acertou:
    print('Você venceu! :)')
else:
    print(f'Você é tabacude haha. O número era {numero_secreto}')    