print('''-------------------------------------------------------
         |                      WIKICOMP                       |
         -------------------------------------------------------''')

print('CADASTRO:')
input_usuario = str(input('Digite seu e-mail: '))
input_senha = str(input('Digite uma senha: '))

while True:
    print('LOGIN:')
    log_usuario = str(input('E-mail: '))
    log_senha = str(input('Senha: '))
    if (log_usuario == input_usuario) and (input_senha == log_senha):
        print('Login realizado com sucesso!')
        break
    else:
        print('Tente novamente!') 

