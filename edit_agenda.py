import os

def edit_contact(agenda):
    contato = input('Digite o contato que deseja editar: ')
    if contato in agenda:
        dados = agenda[contato]
        for dado in dados:
            dado['telefone'] = input('Digite o telefone do contato: ')
            dado['email'] = input('Digite o email do contato: ')
            dado['endereco'] = input('Digite o endereco do contato: ')
        os.system('cls')
        print(f'Contato {contato} foi atualizado!')
    else:
        print(f'{contato} não foi encontrado!')


def delete_contact(agenda):
    contato = input('Digite o contato que deseja deletar: ')
    if contato in agenda:
        os.system('cls')
        print('Contato {contato} foi deletado!')
        agenda.pop(contato)
    else:
        print(f'{contato} não encontrado!')