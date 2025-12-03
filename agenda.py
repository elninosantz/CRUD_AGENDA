AGENDA = {}


def limpar_texto(texto):
    """
    Limpa whitespaces e padroniza o texto
    :param texto:
    :return:
    """
    texto1 = texto.strip()
    texto2 = texto1.lower()
    return texto2


def mostrar_contatos():
    """
    Intera sobre os contatos de dentro da AGENDA, passando esses contatos para a func buscar contato
    :return:
    """
    if AGENDA:
        quantidade_contatos = len(AGENDA)
        for contato_ in AGENDA:
            buscar_contatos(contato_)
        print(f'>>> Total de Contatos: {quantidade_contatos} <<<')
    else:
        print('>>> Nenhum contato para exibir! <<<')

def buscar_contatos(contato_):
    """
    verifica se existe o contato dentro de agenda, se existir ele imprime os valores de detro da agenda
    :param contato_:
    :return:
    """
    if contato_ in AGENDA:
        print('=' * 50)
        print('Nome:', contato_.title())
        print('Telefone:', AGENDA[contato_]['telefone'])
        print('E-Mail:', AGENDA[contato_]['email'])
        print('Endereço:', AGENDA[contato_]['endereco'])

    else:
        print(f'>>> Contato {contato_} Não Encontrado <<<')


def adcionar_dados():
    """
    salva em variaveis o valor dos dados do contato
    :return: str(telefone, email, endereco)
    """
    telefone = input('Digite o telefone: ').strip()
    email = input('Digite o email: ').strip()
    endereco = input('Digite o endereco: ').strip()
    return telefone, email, endereco


def dados_contatos(contato_):
    """
    adiciona os valores retornados do contato em um dict
    :param contato_:str
    :return: none
    """
    telefone, email, endereco = adcionar_dados()
    AGENDA[contato_] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }


def incluir_contato():
    """
    caso não exista o contato, cria um
    :return:
    """
    contato_ = input('Digite o contato que queira adicionar: ')
    contato_ = limpar_texto(contato_)
    if contato_ != '':
        if contato_ not in AGENDA:
            dados_contatos(contato_)
            print(f'>>> Contato {contato_} Adicionado com Sucesso <<<')
        else:
            print(f'Já existe o contato {contato_}!')
    else:
        print('Digite um contato!')


def editar_contato():
    """
    caso exista o contato edita os valores
    :return:
    """
    contato_ = input('Digite o contato que queira editar: ')
    contato_ = limpar_texto(contato_)
    if contato_ != '':
        if contato_ not in AGENDA:
            print(f'>>> O Contato {contato_} não existe! <<<')
        else:
            dados_contatos(contato_)
            print(f'>>> Contato {contato_} editado com Sucesso <<<')
    else:
        print('Digite um contato!')


def excluir_contato(contato_):
    """
    exclui contato caso ele exista

    :param contato_:
    :return:
    """
    if contato_ not in AGENDA:
        print(f'>>> Contato {contato_} Não Encontrado <<<')
    else:
        del AGENDA[contato_]
        print(f'>>> Contato {contato_} Excluido com Sucesso <<<')


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

try:
    while True:
        opcao_ = menu()
        match opcao_:
            case '1':
                mostrar_contatos()
            case '2':
                contato = input('Digite o contato que deseja Visualizar: ')
                contato = limpar_texto(contato)
                if contato != '':
                    buscar_contatos(contato)
            case '3':
                incluir_contato()
            case '4':
                editar_contato()
            case '5':
                contato = input('Digite o contato que deseja excluir: ')
                contato = limpar_texto(contato)
                if contato != '':
                    excluir_contato(contato)
            case '0':
                print('>>> PROGRAMA ENCERRADO <<<')
                break
            case _:
                print('>>> DIGITE UMA OPÇÃO VALIDA!! <<<')
except KeyboardInterrupt:
    print('\n>>> PROGRAMA ENCERRADO <<<')