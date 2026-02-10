# 🏢 Sistema de Gerenciamento de Equipe (CLI)

Este é um projeto de back-end desenvolvido para gerenciar funcionários de uma empresa, utilizando uma interface de linha de comando (CLI). O foco principal foi aplicar conceitos de **Programação Orientada a Objetos (POO)** e **Persistência de Dados** em banco de dados relacional.

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **SQLAlchemy**: Para o mapeamento objeto-relacional (ORM).
* **SQLite**: Banco de dados leve para armazenamento persistente.
* **Rich**: Para criação de uma interface visual amigável no terminal (tabelas e cores).

## 🛠️ Funcionalidades

* **Cadastrar Funcionários**: Salva nome, cargo, setor e salário diretamente no banco de dados.
* **Listagem em Tabela**: Exibe todos os funcionários cadastrados de forma organizada.
* **Busca Inteligente**: Permite filtrar funcionários por nome (busca parcial).
* **Persistência**: Os dados não são perdidos ao fechar o programa, permanecendo no arquivo `empresa.db`.

## 📦 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio