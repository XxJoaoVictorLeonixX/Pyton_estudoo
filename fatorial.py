num = int(input('Informe um numero:'))
fat = 1

if num < 0:
    print('Não existe fatorial de numeros negativos')
elif num == 0:
    print(f'O fatorial de {num} é 1 ')
else:
    for x in range(1,num+1):
        fat = fat * x
    print(f'O fatorial de {num} é: {fat}')