valorProdut = float(input('Informe o valor do produto:'))
porcen = int(input('Informe o valor do desconto:'))
desconto = (valorProdut * porcen / 100)
novoVal = valorProdut - desconto

print(f'O novo valor do produto com {desconto}% de desconto ficara: {novoVal}')