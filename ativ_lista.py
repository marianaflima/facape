from time import sleep

# Entrada
pacientes = []
idade = []
indenizaçao = []
ind_base = 850

print('=' * 15)
print('         UNIMED          ')
print('=' * 15)

# Processamento

while True:
    yes_no = int(input('''
Deseja inserir um novo paciente?
[0]Sim      [1]Não

    '''))
    if yes_no == 0:
        nome_paciente = str(input('Nome: '))
        idade_paciente = int(input('Idade: '))
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
    else:
        break



#Saída
for i in pacientes, idade, indenizaçao:
    print(f'{pacientes[i]}..........{idade[i]}.........{indenizaçao[i]}')