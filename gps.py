t = 'Cristo Redentor', 'Machu Picchu', 'Chichén Itzá', 'Coliseu', 'Ruínas de Petra', 'Taj Mahal', 'Grande Muralha', (-22.951804, -43.210760),  (-13.163068, -72.545128), (20.962910, -89.578262), (41.890188, 12.492287), (30.328454, 35.444362), (27.175015, 78.042155), (40.43188, 116.57051) 
print(f'''
----------------------------------------------------------
|                  GPS - 7 MARAVILHAS
----------------------------------------------------------
- Mostra a latitude e longitude do local desejado!
''')

while True:
    n = int(input('''
    [0] Cristo Redentor (BRA)
    [1] Machu Picchu (PER) 
    [2] Chichén Itzá (MEX)
    [3] Coliseu (ITA)
    [4] Ruínas de Petra (JOR)
    [5] Taj Mahal (IND)
    [6] Grande Muralha (CHI)
    Digite o local desejado: '''))
    if (n < 0) or (n > 6):
        print('\n Tente novamente!')
    else:
        if n in range(0, len(t)):
            print(f'''
    {t[n]} --> {t[n + 7]}''')
        break
    