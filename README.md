# 🚀 Agenda de Contatos CLI em Python

Um projeto simples de Agenda de Contatos (CRUD) desenvolvido em Python, que roda diretamente no terminal (CLI - Command-Line Interface). Este projeto permite ao usuário adicionar, visualizar, buscar, editar e deletar contatos de forma interativa.

## ✨ Funcionalidades

O programa apresenta um menu simples com as seguintes operações:

* **[1] Adicionar Contatos:** Salva um novo contato com nome, telefone, email e endereço.
* **[2] Visualizar Contatos:** Lista todos os contatos atualmente salvos na agenda.
* **[3] Buscar Contatos:** Procura por um contato específico usando o nome.
* **[4] Editar Contatos:** Permite atualizar as informações (telefone, email, endereço) de um contato existente.
* **[5] Excluir Contatos:** Remove um contato da agenda.
* **[0] Sair:** Encerra a aplicação.

## 📂 Estrutura do Projeto

O código é modularizado para facilitar a manutenção:

* `main.py`: Contém o loop principal da aplicação e o menu de seleção. É o ponto de entrada do programa.

<br>

* `create_agenda.py`: Inclui as funções para inserir (`insert_contact`), buscar (`search_contact`) e exibir (`display_contact`) os contatos.

<br>

* `edit_agenda.py`: Inclui as funções para modificar (`edit_contact`) e deletar (`delete_contact`) os contatos.

## 🔧 Como Executar

Para rodar este projeto, você precisa ter o **Python 3** instalado em sua máquina.

1.  **Clone o repositório:**
    ```bash
    # Substitua pela URL do seu repositório quando o tiver
    git clone [https://github.com/elninosantz/CRUD_AGENDA](https://github.com/elninosantz/CRUD_AGENDA)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd CRUD_AGENDA
    ```

3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```

4.  Pronto! O menu da agenda aparecerá no seu terminal.

## 🔮 Próximos Passos (Roadmap)

Este projeto está em desenvolvimento. As próximas funcionalidades planejadas são:

* **Persistência de Dados:** Implementar a funcionalidade de **salvar** os contatos da agenda em um arquivo (ex: JSON, CSV ou TXT).
* **Carregamento de Dados:** Implementar a funcionalidade de **ler** os contatos de um arquivo ao iniciar o programa (complementando a opção [9] do menu).

## Autor

* **Augusto** - [Linkedin](https://www.linkedin.com/in/elninosantz/)