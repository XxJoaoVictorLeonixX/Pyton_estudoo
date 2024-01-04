palpite = 5
numero = 9

while bool(palpite) is True:
    print('Adivinhe qual o numero correto:')
    palpite = int(input())
    if palpite == numero:
        print('Parabens você acertou')
        break
    else:
        print('Voce errou')
else:
    print('Erro na aplicação')
        



print(bool(palpite))