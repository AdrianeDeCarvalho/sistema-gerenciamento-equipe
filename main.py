from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from core.gerenciador import inicializar_banco, salvar_funcionario, listar_funcionario, buscar_funcionario_nome

console = Console()

def exibir_tabela(funcionarios):
    if not funcionarios:
        console.print("[yellow]Nenhum funcionario encontrado.[/]")
        return
    
    table = Table(title="Lista de Funcionários", show_header=True, header_style="bold blue")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Nome", min_width=20)
    table.add_column("Cargo", min_width=15)
    table.add_column("Setor", min_width=15)
    table.add_column("Salário", justify="right")

    for f in funcionarios:
        table.add_row(str(f.id), f.nome, f.cargo, f.setor, f"R$ {f.salario:,.2f}")

    console.print(table)


def main():
    inicializar_banco()

    while True:
        console.print(Panel.fit("SISTEMA DE RH", style="bold green"))
        print("1. Cadastrar Funcionário")
        print("2. Listar Todos")
        print("3. Buscar por Nome")
        print("4. Sair")
        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 1:
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            setor = input("Setor: ")
            
            try:
                salario = float(input("Salário: "))
                salvar_funcionario(nome, cargo, setor, salario)
                console.print(f"[bold green]Sucesso:[/] {nome} foi adicionado!")
            except ValueError:
                console.print("[bold red]Erro:[/] Salário deve ser um número.")


        elif opcao == 2:
            funcionarios = listar_funcionario()
            exibir_tabela(funcionarios)

        elif opcao == 3:
            nome_busca = input("Digite o nome para buscar: ")
            resultado = buscar_funcionario_nome(nome_busca)
            exibir_tabela(resultado)

        elif opcao == 4:
            console.print("[italic cyan]Encerrando o sistema... Até logo![/]")
            break

        else:
            console.print("[bold red]Opção inválida![/]")

if __name__ == "__main__":
    main()