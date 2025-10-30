import os


def display_contact(agenda):
    for contato, dados in agenda.items():
        for dado in dados:
            print(f'''
        =======================================
        | Nome: {contato}
        | Telefone: {dado['telefone']}
        | Email: {dado['email']}
        | Endereco: {dado['endereco']}
        =======================================
            ''')

def search_contacts(agenda):
    contato = input('Digite o nome do contato: ')
    if contato in agenda:
        agenda_unic = agenda[contato]
        for dado in agenda_unic:
            print(f'''
Nome: {contato}
Telefone: {dado['telefone']}
Email: {dado['email']}
Endereco: {dado['endereco']}
''')
    else:
        print(f'{contato} Não existe!')


def insert_contact(agenda):
    contato = input('Digite o nome do contato: ')
    if contato in agenda:
        print(f'Foi encontado o contato: {contato}')
        escolha = input('Quer rescreve-lo (s/n)? ')
        if escolha.lower() == 's':
            pass
        elif escolha.lower() == 'n':
            return None
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    if contato not in agenda:
        agenda[contato] = []
    agenda[contato].append({'telefone': telefone, 'email': email, 'endereco': endereco})
    os.system('cls')
    print(f'Contato de {contato} adicionado com sucesso!')
    print(agenda)
    return agenda
