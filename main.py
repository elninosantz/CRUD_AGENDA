from create_agenda import insert_contact, search_contacts, display_contact
from edit_agenda import edit_contact, delete_contact

if __name__ == '__main__':
    agenda = {}
    while True:

        try:
            print('''
    SELECIONE A OPÇÃO:
    [1] Para adcionar contatos
    [2] Para visualizar contatos
    [3] Para buscar contatos
    [4] Para editar contatos
    [5] Para excluir contatos
    [9] Para carregar contatos
    [0] Para sair
            ''')
            select_option = input('Digite a opção desejada: ')
            if select_option == '1':
                agenda = insert_contact(agenda)
            elif select_option == '2':
                print(agenda)
                display_contact(agenda)
            elif select_option == '3':
                search_contacts(agenda)
            elif select_option == '4':
                edit_contact(agenda)
            elif select_option == '5':
                delete_contact(agenda)
            elif select_option == '0':
                break
        except Exception as e:
            print(f'Error: {e}')