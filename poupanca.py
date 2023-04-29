cap = float(input('Digite o valor inicial do investimento: '))
juros = int(input('Digite a taxa de juros: '))/100
tempo = 0

while tempo < 12:
    tempo += 1
    cap = cap * (juros + 1)
    print(f'{tempo}º mês: R${(cap):.2f}')