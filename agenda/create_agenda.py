import os

def dados_view(contato, dado):
    print(f'''
    =======================================
    | Nome: {contato}
    =======================================
    | ID Contato: {dado['ID']}
    | Telefone: {dado['telefone']}
    | Email: {dado['email']}
    | Endereco: {dado['endereco']}
    =======================================
        ''')

def display_contact(agenda):
    """
    AQUI EXIBE OS DADOOS DA AGENDA

    """
    for contato, dados in agenda.items():
        for dado in dados:
            dados_view(contato, dado)


def search_contacts(agenda):
    """
    AQUI BUSCA DADOS DA AGENDA
    :param agenda:
    :return:

    TODO: .isdigit() OR TRY
    """
    contato = input('Digite o nome do contato: ')
    if contato in agenda:
        agenda_unic = agenda[contato]
        for dado in agenda_unic:
            print(f'ID: {dado['ID']} | Nome: {contato} | Telefone: {dado["telefone"]}....')
        select_option = int(input('Por ID selecione o contato que deseja mais informação: '))
        for dado in agenda_unic:
            if select_option == dado['ID']:
                dados_view(contato, dado)
    else:
        print(f'{contato} Não existe!')


def insert_contact(agenda):
    contato = input('Digite o nome do contato: ')
    if contato in agenda:
        "SE O CONTATO EXISTE DENTRO DA AGENDA"
        print(f'Foi encontado o contato: {contato}')
        escolha = input('Quer adicionar mais um dado nesse contato (s/)? ')
        if escolha.lower() == 's':
            pass
        else:
            os.system('cls')
            print('Operação cancelada, retornando para o menu.')
            return agenda
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    if contato not in agenda:
        agenda[contato] = []
    id_contato = len(agenda[contato]) + 1
    agenda[contato].append({'ID': id_contato, 'telefone': telefone, 'email': email, 'endereco': endereco})
    os.system('cls')
    print(f'Contato de {contato} adicionado com sucesso!')
    return agenda

