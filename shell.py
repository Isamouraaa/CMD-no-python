import os

# Função para verificar inteiros
def isint(x):
    try:
        return int(x)
    except ValueError:
        return 'False'


# Inicialização de lista para armazenar os comandos utilizados
historico = []

# Mensagens iniciais para o usuário
print('\nPara lista de comandos, insira o comando "help".')
print('Para visualizar o histórico, insira "historico".\n')

while True:
    comando = input('>> Digite o comando:\n>> ')
    print('\n>> Caso queira sair, digite "exit".\n')

    # Mudança de diretório
    if comando.startswith('cd '):
        try:
            if comando == 'cd ..':
                os.chdir('..')
            else:
                os.chdir(comando[3:])
        except FileNotFoundError:
            print('>> Diretório não encontrado.')
            continue

    # Listagem de comandos pelo histórico
    elif comando[0] == '!' and len(comando) > 1:
        if comando == '!!' and len(historico) >= 1:
            comando = historico[-1]
        else:
            index = isint(comando[1:])
            if index == 'False':
                print('>> Comando não suportado.')
                continue
            if index > len(historico):
                print('>> Não há comandos suficiente.')
                continue
            comando = historico[int(comando[1:])]
    
    # Visualização do histórico
    elif comando == 'historico':
        print(f'Os comandos inseridos estão na seguinte lista:\n{historico}')
    
    # Mecanismo de parada do laço infinito
    elif comando.lower() == 'exit':
        exit()

    # Caso não seja nenhum dos casos especiais acima, executar o comando
    else:
        os.system(comando)

    historico.append(comando)
