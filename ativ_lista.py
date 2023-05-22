from time import sleep

# Entrada
pacientes = []
idade = []
indenizaçao = []
c = 0

print('=' * 30)
print('         UNIMED          ')
print('=' * 30)

# Processamento

while True:
    yes_no = int(input('''Deseja inserir um novo paciente?
[0]Sim      [1]Não
'''))
    print('')
    if yes_no == 0:
        nome_paciente = str(input('Nome: '))
        idade_paciente = int(input('Idade: '))
        ind_base = float(input('''=========================
|       INDENIZAÇÃO BASE    |
=========================
|0 a 12     |  R$ 4500  |
|13 a 49    |  R$ 3000  |
|50 a 69    |  R$ 3500  |
|70 ou mais |  R$ 5000  |
=========================
Digite o valor/idade: '''))
        if idade_paciente <= 12:
            ind_ajustada = ind_base * 1.3
        elif (idade_paciente >= 13) and (idade_paciente <= 49):
            ind_ajustada = ind_base * 1.1
        elif (idade_paciente >= 50) and (idade_paciente <= 65):
            ind_ajustada = ind_base * 1.15
        else:
            ind_ajustada = ind_base * 1.35

        pacientes.append(nome_paciente)
        idade.append(idade_paciente)
        indenizaçao.append(f'{ind_ajustada:.2f}')
        print('=' * 30)
    else:
        break

sleep(1)
print('''====================================
NOME         IDADE       INDENIZAÇÃO
====================================''')
while c != len(pacientes):
    print(f'|   {pacientes[c]}  |   {idade[c]}  |   R${indenizaçao[c]}  |')
    c += 1
print('====================================')


