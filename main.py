# Imports
from pathlib import Path

# Imports Libs Locais
from src.database import exportar_contatos, importar_contatos, exibir_contatos, buscar_contatos, adicionar_dados, incluir_contato, editar_contato, excluir_contato, AGENDA
from src.util import limpar_texto


def salvar():
    """
    - Utiliza a função exportar_contatos para salva o arquivo CSV com nome database.
    - Garante a reutilização dos dados da agenda de modo estatico.

    Returns:
         None: Não exibe valores, aciona a exportação da agenda.
    """
    exportar_contatos('database')

def carregar():
    """
    - Obtém o caminho do diretorio onde o script está através da função Path.
    - Junta o caminho_do_script com o nome do database.csv.
    - Verifica se o arquivo existe.
    - Caso o arquivo exista, utiliza a função importar_contatos para importar a agenda.
    - Caso o arquivo não exista, apresenta um alerta que o DB ainda não foi gerado.

    Returns:
        None: Não exibe valores, aciona a importação da agenda quando arquivo existir.

    """
    caminho_do_script = Path(__file__).parent
    arquivo  = caminho_do_script / 'database.csv'
    if arquivo.exists():
        importar_contatos('database')
    else:
        print('>>> O arquivo DB ainda não foi Gerado <<<')

def menu():
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

if __name__ == '__main__':
    carregar()
    try:
        while True:
            opcao_ = menu()
            match opcao_.lower():
                case '1':
                    exibir_contatos()
                case '2':
                    contato = input('Digite o contato que deseja Visualizar: ')
                    contato = limpar_texto(contato)
                    if contato != '':
                        buscar_contatos(contato)
                case '3':
                    contato, telefone, email, endereco = adicionar_dados()
                    incluir_contato(contato,telefone,email,endereco)
                case '4':
                    contato, telefone, email, endereco = adicionar_dados()
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
                    if AGENDA:
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