notas = []
c = 0

while c != 5:
    n = int(input(f'Digite a {c + 1}ª nota: '))
    notas.append(n)
    c += 1

m = sum(notas)

print(f'Média final: {(m/c):.1f}')