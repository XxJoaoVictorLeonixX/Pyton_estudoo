idade = int(input('Informe a sua idade:'))

if idade > 5 and idade < 7:
    print('Categoria Infantil A')
elif idade > 8 and idade < 10:
    print('Categoria Infantil B')
elif idade > 11 and idade < 13:
    print('Categoria Juvenil A')
else:
    print('Categoria Juvenil B')
