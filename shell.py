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

def main():
    while True:
        print('\n>> Caso queira sair, digite "sair".\n')
        comando = input('>> Digite o comando:\n>> ')
    
        # Mecanismo de parada do laço infinito
        if comando.lower() == 'sair':
            exit()
    
        # Mudança de diretório
        elif comando.startswith('cd '):
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
            if len(historico) == 0:
                print('>> Ainda não há comandos no histórico.')
            else:
                print('>> Os comandos inseridos estão na seguinte lista:')
                for i in range(len(historico)):
                    print(f'[{i}] {historico[i]}')
        
        # Caso não seja nenhum dos casos especiais acima, executar o comando
        else:
            os.system(comando)
        
        # Armazena o comando no histórico
        historico.append(comando)
main()






