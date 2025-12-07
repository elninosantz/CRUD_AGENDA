# 📒 Agenda em Python (CRUD + Arquivos CSV)

Um projeto simples de agenda desenvolvido durante o curso de Python da Solyd com funcionalidades de CRUD (Criar, Ler, Atualizar e Deletar), além de exportar e importar contatos através de arquivos CSV.

O objetivo do projeto é demonstrar:
- Estruturação de código em módulos.
- Uso de dicionários como base de dados em memória.
- Persistência de dados em arquivos CSV.
- Boas práticas com docstrings.
- Interação com o usuário via terminal.

---

## 🚀 Funcionalidades

- **Adicionar contato**  
  Solicita nome, telefone, e-mail e endereço, normaliza os dados e salva na AGENDA.

- **Editar contato**  
  Atualiza informações de um contato existente.

- **Excluir contato**  
  Remove um contato da agenda.

- **Buscar contato**  
  Exibe os dados de um contato específico.

- **Exibir todos os contatos**  
  Lista todos os contatos salvos.

- **Exportar contatos**  
  Salva a agenda em `database.csv`.

- **Importar contatos**  
  Carrega dados de `database.csv` para a AGENDA.

---

## 🧠 Estrutura do Projeto

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

- Python 3.10+
- Nenhuma biblioteca externa (somente built-ins)

---

## ▶️ Como executar

No diretório raiz do projeto, execute:

```bash
python main.py
```

O sistema exibe um menu interativo no terminal.

---

## 💾 Persistência de Dados

- Ao sair do programa, a agenda é exportada automaticamente para `database.csv`.  
- Ao iniciar o programa, se o arquivo existir, os dados são importados para memória.

---

## 📚 Sobre o código

Este projeto faz uso de:
- Estruturas de repetição (`while`)
- Pattern matching (`match`)
- Manipulação de arquivos (`open`)
- Manipulação de caminhos com `pathlib`
- Dicionários como estrutura principal de dados
- Docstrings detalhadas em estilo bullet-points

---

## 📂 Licença

Projeto livre para estudo e modificação.