from create_agenda import display_contact

def edit_contact(agenda):
    contato = input('Digite o contato que deseja editar: ')
    if contato in agenda:
        dados = agenda[contato]
        for dado in dados:
            dado['telefone'] = input('Digite o telefone do contato: ')
            dado['email'] = input('Digite o email do contato: ')
            dado['endereco'] = input('Digite o endereco do contato: ')
        print('Contato foi atualizado!')
    else:
        print(f'{contato} não foi encontrado!')
