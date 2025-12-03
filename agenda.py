AGENDA = {}


def limpar_texto(texto):
    texto1 = texto.strip()
    texto2 = texto1.lower()
    return texto2


def mostrar_contatos():
    """
    Intera sobre os contatos de dentro da AGENDA, passando esses contatos para a func buscar contato
    :return:
    """
    for contato in AGENDA:
        buscar_contatos(contato)


def buscar_contatos(contato):
    """
    verifica se existe o contato dentro de agenda, se existir ele imprime os valores de detro da agenda
    :param contato:
    :return:
    """
    if contato in AGENDA:
        print('=' * 50)
        print('Nome:', contato.title())
        print('Telefone:', AGENDA[contato]['telefone'])
        print('E-Mail:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])

    else:
        print(f'>>> Contato {contato} Não Encontrado <<<')


def adcionar_dados():
    """
    salva em variaveis o valor dos dados do contato
    :return: str(telefone, email, endereco)
    """
    telefone = input('Digite o telefone: ').strip()
    email = input('Digite o email: ').strip()
    endereco = input('Digite o endereco: ').strip()
    return telefone, email, endereco


def dados_contatos(contato):
    """
    adiciona os valores retornados do contato em um dict
    :param contato:str
    :return: none
    """
    telefone, email, endereco = adcionar_dados()
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }


def incluir_contato():
    """
    caso não exista o contato, cria um
    :return:
    """
    contato = input('Digite o contato que queira adicionar: ')
    contato = limpar_texto(contato)
    if contato not in AGENDA:
        dados_contatos(contato)
        print(f'>>>>> Contato {contato} Adicionado com Sucesso <<<<<')
    else:
        print(f'Já existe o contato {contato}!')


def editar_contato():
    """
    caso exista o contato edita os valores
    :return:
    """
    contato = input('Digite o contato que queira editar: ')
    contato = limpar_texto(contato)
    if contato not in AGENDA:
        print(f'>>>>> O Contato {contato} não existe! <<<<<')
    else:
        dados_contatos(contato)
        print(f'>>>>> Contato {contato} editado com Sucesso <<<<<')


def excluir_contato(contato):
    """
    exclui contato caso ele exista

    :param contato:
    :return:
    """
    if contato not in AGENDA:
        print(f'>>> Contato {contato} Não Encontrado <<<')
    else:
        del AGENDA[contato]
        print(f'>>>>> Contato {contato} Excluido com Sucesso <<<<<')


def menu():
    """
    1- mostrar todos os contatos da agenda
    2- Consultar contato na agenda
    3- incluir contatos da agenda caso não existam
    4- editar contatos da agenda, caso existam
    5- excluir contatos da agenda
    0- sair do programa
    :return:
    """
    print('=' * 50)
    print('''
MENU DA AGENDA:
[1] Mostrar todos os contatos da agenda.
[2] Consultar contato na agenda.
[3] Inluir contatos da agenda(caso não existam).
[4] Editar contatos da agenda(caso existam).
[5] Excluir contatos da agenda.

>>> [0] PARA SAIR DO PROGRAMA <<<\n''')
    opcao = input('ESCOLHA 1 OPÇÃO VALIDA(Ex: 1): ')
    return opcao

while True:
    opcao = menu()
    match opcao:
        case '1':
            mostrar_contatos()
        case '2':
            contato = input('Digite o contato que deseja Visualizar: ')
            contato = limpar_texto(contato)
            buscar_contatos(contato)
        case '3':
            incluir_contato()
        case '4':
            editar_contato()
        case '5':
            contato = input('Digite o contato que deseja excluir: ')
            contato = limpar_texto(contato)
            excluir_contato(contato)
        case '0':
            print('>>> PROGRAMA ENCERRADO <<<')
            break
        case _:
            print('>>> DIGITE UMA OPÇÃO VALIDA!! <<<')
