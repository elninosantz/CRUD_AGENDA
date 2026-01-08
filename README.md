# 📒 Agenda em Python (CRUD + CSV)

Projeto de agenda desenvolvido em **Python**, com funcionalidades completas de **CRUD** (Criar, Ler, Atualizar e Deletar) e **persistência de dados em arquivos CSV**.  
Foi criado durante o curso de Python da **[Solyd](https://solyd.com.br/)**, com foco em organização de código e fundamentos da linguagem.

---

## 🎯 Objetivo do projeto

Demonstrar, de forma prática:

- Estruturação de código em módulos
- Uso de **dicionários** como base de dados em memória
- Persistência de dados utilizando **arquivos CSV**
- Boas práticas com **docstrings**
- Interação com o usuário via **terminal**

---

## 🚀 Funcionalidades

- **Adicionar contato**  
  Cadastro de nome, telefone, e-mail e endereço, com normalização dos dados.

- **Editar contato**  
  Atualização de informações de contatos existentes.

- **Excluir contato**  
  Remoção de contatos da agenda.

- **Buscar contato**  
  Consulta individual de contatos cadastrados.

- **Listar contatos**  
  Exibição de todos os contatos armazenados.

- **Exportar contatos**  
  Salvamento dos dados em `database.csv`.

- **Importar contatos**  
  Carregamento automático dos dados a partir de `database.csv`.

---

## 🧠 Estrutura do projeto

```
CRUD_AGENDA/
│
├── main.py               # Loop principal, menu e controle de execução
├── src/
│   ├── database.py       # Funções de CRUD, importação e exportação
│   ├── util.py           # Funções auxiliares (normalização de texto)
│   └── __init__.py
└── database.csv          # Gerado automaticamente (se existir)
```

---

## 📝 Requisitos

- Python **3.10+**
- Nenhuma biblioteca externa (apenas módulos built-in)

---

## ▶️ Como executar

No diretório raiz do projeto, execute:

```bash
python main.py
```

O sistema exibirá um **menu interativo no terminal**.

---

## 💾 Persistência de dados

- Ao encerrar o programa, a agenda é exportada automaticamente para `database.csv`
- Ao iniciar, caso o arquivo exista, os dados são carregados para a memória

---

## 📚 Conceitos aplicados

- Estruturas de repetição (`while`)
- Pattern Matching (`match`)
- Manipulação de arquivos (`open`)
- Manipulação de caminhos com `pathlib`
- Uso de **dicionários** como estrutura principal de dados
- Docstrings detalhadas para documentação do código

---

## 📂 Licença

Projeto livre para estudo e modificação.
