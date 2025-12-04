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
    contato = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone: ').strip()
    email = input('Digite o email: ').strip()
    endereco = input('Digite o endereco: ').strip()
    return contato, telefone, email, endereco


def incluir_contato(contato_, telefone, email, endereco):
    """
    caso não exista o contato, cria um
    :return:
    """
    contato_ = limpar_texto(contato_)
    if contato_ != '':
        if contato_ not in AGENDA:
            AGENDA[contato_] = {
                'telefone': telefone,
                'email': email,
                'endereco': endereco,
            }
            print(f'>>> Contato {contato_} Adicionado com Sucesso <<<')
        else:
            print(f'Já existe o contato {contato_}!')
    else:
        print('Digite um contato!')


def editar_contato(contato_, telefone, email, endereco):
    """
    caso exista o contato edita os valores
    :return:
    """

    contato_ = limpar_texto(contato_)
    if contato_ != '':
        if contato_ not in AGENDA:
            print(f'>>> O Contato {contato_} não existe! <<<')
        else:
            AGENDA[contato_] = {
                'telefone': telefone,
                'email': email,
                'endereco': endereco,
            }
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


def exportar_contatos(nome_do_arquivo_):
    """
    Exporta os dados da agenda em um arquivo csv
    :param nome_do_arquivo_:
    :return:
    """
    try:
        with open(f'{nome_do_arquivo_}.csv', 'w', encoding='utf-8') as agenda:
            for contato_ in AGENDA:
                agenda.write(f'{contato_},{AGENDA[contato_]['telefone']},{AGENDA[contato_]['email']},{AGENDA[contato_]['endereco']}\n')
        print('>>> Agenda exportada com sucesso!! <<<')
    except Exception as e:
        print(f'>> ERROR:{e} <<<')


def importar_contatos(nome_do_arquivo_):
    try:
        with open(f'{nome_do_arquivo_}.csv', 'r', encoding='utf-8') as agenda:
            contatos = agenda.readlines()
            for contato_ in contatos:
                dados = contato_.strip().split(',')
                nome = dados[0]
                telefone = dados[1]
                email = dados[2]
                endereco = dados[3]
                incluir_contato(nome, telefone, email, endereco)
        print(f'>>> Agenda importada com sucesso!! Total de Contatos: {len(AGENDA)} <<<')

    except Exception as e:
        print(f'>> ERROR:{e} <<<')


def salvar():
    exportar_contatos('database')

def carregar():
    importar_contatos('database')

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

------------------------------------------------
[E] Exportar Agenda em CSV
[I] Importar Contatos

>>> [0] PARA SAIR DO PROGRAMA <<<\n''')
    opcao = input('ESCOLHA 1 OPÇÃO VALIDA(Ex: 1): ')
    return opcao

carregar()
try:
    while True:
        opcao_ = menu()
        match opcao_.lower():
            case '1':
                mostrar_contatos()
            case '2':
                contato = input('Digite o contato que deseja Visualizar: ')
                contato = limpar_texto(contato)
                if contato != '':
                    buscar_contatos(contato)
            case '3':
                contato, telefone, email, endereco = adcionar_dados()
                incluir_contato(contato,telefone,email,endereco)
            case '4':
                contato, telefone, email, endereco = adcionar_dados()
                editar_contato(contato,telefone,email,endereco)
            case '5':
                contato = input('Digite o contato que deseja excluir: ')
                contato = limpar_texto(contato)
                if contato != '':
                    excluir_contato(contato)
            case 'e':
                nome_do_arquivo = input('Digite o nome do arquivo: ')
                exportar_contatos(nome_do_arquivo)
            case 'i':
                nome_do_arquivo = input('Digite o nome do arquivo: ')
                importar_contatos(nome_do_arquivo)

            case '0':
                print('>>> PROGRAMA ENCERRADO <<<')
                if AGENDA != {}:
                    salvar()
                    break
                else:
                    break
            case _:
                print('>>> DIGITE UMA OPÇÃO VALIDA!! <<<')
except KeyboardInterrupt:
    salvar()
    print('\n>>> PROGRAMA ENCERRADO <<<')
except Exception as e:
    print(f'>> ERROR:{e} <<<')
    salvar()