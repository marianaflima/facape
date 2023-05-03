print('Bem vindo(a) ao GPS das 7 maravilhas do mundo')
print('''
[0] Cristo Redentor (BRA)
[1] Coliseu (ITA)
[2] Chichén Itzá (MEX)
[3] Muralha da China (CHI)
[4] Petra (JOR)
[5] Machu Picchu (PER)
[6] Taj Mahal (IND)
''')
lista=('Cristo Redentor: 22.9519° S e 43.2106° W','Coliseu: 41.8902° N e 12.4922° E','Chichén Itzá: 40.6769° N e 88.5692° W', 'Muralha da China: 40.6769° N e 117.2319° E', 'Petra: 30.3285° N e 35.4444° E','Machu Picchu: 13.1631° S e 72.5450° W','Taj Mahal: 27.1750° N e 78.0422° E')

while True:
    Local = int(input('Qual das 7 maravilhas gostaria de encontrar?\n'))
    if (Local < 0) or (Local > 6):
        print('Digite um número válido')
    else:
        if Local in range(0,7):
            print(lista[Local])
            break