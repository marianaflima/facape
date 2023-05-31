lista = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num == 0:
        break

x = 0
print('=' * 30)
while x < len(lista):
    print(lista[x])
    x += 1