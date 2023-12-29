idade = int(input('Informe a sua idade:'))

if idade < 16:
    print('Você é menor de idade')
elif idade > 16 and idade < 18:
    print('Você é EMANCIPADO')
else:
    print('Você é maior de idade')