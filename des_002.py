kg = float(input('Peso das frutas: '))
fruta = int(input('''Qual a fruta?
[1] Maçã
[2] Morango
----------------------
'''))

if fruta == 1:
    if kg <= 5:
        preço = kg * 1.8
    else:
        preço = kg * 1.5
elif fruta == 2:
    if kg <= 5:
        preço = kg * 2.5
    else:
        preço = kg * 2.2
else:
    print('Código inválido')

if kg >= 8 or preço > 25:
    preço = preço * 0.9

print(f'Total a pagar: R${preço}')