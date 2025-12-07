#!Python3
# Imports Libs Local
from src.util import limpar_texto

# Global Variable
AGENDA = {}


def exibir_contatos() -> None:
    """
    - Verifica se a agenda possui contatos.
    - Caso exista, itera sobre todos os contatos da agenda.
    - Utiliza a função buscar_contato dentro de um loop para exibir todos os contatos.
    - Caso não haja contatos, apresenta um alerta informando que a agenda está vazia.

    Returns:
        None: Essa função apenas exibe informações, não retorna valores.
    """

    if AGENDA:
        quantidade_contatos = len(AGENDA)
        for contato_ in AGENDA:
            buscar_contatos(contato_)
        print(f'>>> Total de Contatos: {quantidade_contatos} <<<')
    else:
        print('>>> Nenhum contato para exibir! <<<')


def buscar_contatos(contato_:str) -> None:
    """
    - Busca um contato específico dentro da agenda.
    - Exibe os dados caso o contato exista.
    - Caso não exista, apresenta um alerta de contato não encontrado.

    Args:
        contato_ (str): Nome do contato informado pelo usuário.

    Returns:
        None: Essa função exibe apenas os dados; não retorna valores.
    """
    if contato_ in AGENDA:
        print('=' * 50)
        print('Nome:', contato_.title())
        print('Telefone:', AGENDA[contato_]['telefone'])
        print('E-Mail:', AGENDA[contato_]['email'])
        print('Endereço:', AGENDA[contato_]['endereco'])

    else:
        print(f'>>> Contato {contato_} Não Encontrado <<<')


def adicionar_dados() -> tuple:
    """
    - Coleta os dados que serão utilizados para a criação do contato na agenda.

    Returns:
        tuple: (contato, telefone, email, endereco)
    """
    contato = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone: ').strip()
    email = input('Digite o email: ').strip()
    endereco = input('Digite o endereco: ').strip()
    return contato, telefone, email, endereco


def incluir_contato(contato_:str, telefone:str, email:str, endereco:str) -> None :
    """
    - Recebe o contato e normaliza utilizando a função limpar_texto.
    - Verifica se o contato não é vazio.
    - Caso esteja vazio, exibe um alerta para digitar um contato.
    - Caso não esteja vazio verifica se o contato existe na agenda.
    - Caso não exista o contato adiciona o contato e seus dados na agenda.
    - Caso o contato exista na agenda, apresenta um alerta de contato existente.

    Args:
        contato_ (str): Nome do contato informado pelo usuário.
        telefone (str): Telefone associado ao contato.
        email (str): Endereço de e-mail do contato.
        endereco (str): Endereço físico do contato.

    Returns:
        None: A função apenas exibe mensagens; não retorna valores.
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
    - Recebe o contato e normaliza utilizando a função limpar_texto
    - Caso o contato não seja vazio, verifica se existe na agenda
    - Caso exista atualiza/edita os dados do contato.
    - Caso contrário apresenta alertas de contato inexistente, ou digite um contato.

    Args:
        contato_ (str): Nome do contato informado pelo usuário.
        telefone (str): Telefone associado ao contato.
        email (str): Endereço de e-mail do contato.
        endereco (str): Endereço físico do contato.

    Returns:
        None: Não retorna valores; atualiza ou edita os dados quando necessário.

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
    - Verifica a existência do contato na agenda.
    - Caso não exista apresenta um alerta de contato inexistente.
    - Caso exista, deleta o contato recebido por parâmetro e confirma exibindo uma mensagem.

    Args:
        contato_ (str): Nome do contato informado pelo usuário.

    Returns:
        None: Remove contato da agenda e exibe mensagem.
    """
    if contato_ not in AGENDA:
        print(f'>>> Contato {contato_} Não Encontrado <<<')
    else:
        del AGENDA[contato_]
        print(f'>>> Contato {contato_} Excluido com Sucesso <<<')


def exportar_contatos(nome_do_arquivo_):
    """
    - Cria um arquivo CSV com o nome informado pelo usuário.
    - Itera sobre os contatos da agenda.
    - Escreve os dados de (nome, telefone, email e endereço) dentro do arquivo.

    Args:
        nome_do_arquivo_ (str): Nome do arquivo informado pelo usuário.

    Returns:
        None: Não retorna valores, salva os contatos e informações em um arquivo.
    """
    try:
        with open(f'{nome_do_arquivo_}.csv', 'w', encoding='utf-8') as agenda:
            for contato_ in AGENDA:
                agenda.write(f'{contato_},{AGENDA[contato_]['telefone']},{AGENDA[contato_]['email']},{AGENDA[contato_]['endereco']}\n')
        print('>>> Agenda exportada com sucesso!! <<<')
    except Exception as e:
        print(f'>> ERROR:{e} <<<')


def importar_contatos(nome_do_arquivo_):
    """
    - Abre o arquivo CSV com nome informado pelo usuário.
    - Transforma o arquivo em uma lista de linhas.
    - Itera sobre cada linha da lista de contatos.
    - Remove whitespaces e separa por vírgulas os dados do contato.
    - Utiliza a função incluir_contato para adicionar esses dados na AGENDA(Dicionario na Memória).
    - Exibe um alerta informando que a agenda foi importada.

    Args:
        nome_do_arquivo_ (str): Nome do arquivo CSV informado pelo usuário.

    Returns:
        None: Não retorna valores, importa os dados externos para o script
    """
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