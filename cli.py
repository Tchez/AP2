import typer
from functions import create_files, populate_csv, create_person, search_by_name, search_by_salary

app = typer.Typer()

@app.command()
def initialize() -> None:
    """
    Inicializa o ambiente, criando os arquivos CSV ("pessoas_by_name.csv" e "pessoas_by_salary.csv") com as colunas ID, nome e salário. E populando com 500 registros.
    """
    create_files()
    populate_csv(500)


@app.command()
def create(name: str, salary: float):
    """
    Cria um registro com o nome e salário informados.
    """
    create_person(name, salary)


@app.command()
def find_name(name: str):
    """
    Procura uma pessoa pelo nome.
    """
    result = search_by_name(name)
    if result:
        typer.echo(f"Found: ID: {result[0]}, Name: {result[1]}, Annual Salary: ${result[2]}")
    else:
        typer.echo(f"Person named '{name}' not found.")


@app.command()
def find_salary(salary: float):
    """
    Procura uma pessoa pelo salário.
    """
    result = search_by_salary(salary)
    if result:
        typer.echo(f"Found: ID: {result[0]}, Name: {result[1]}, Annual Salary: ${result[2]}")
    else:
        typer.echo(f"No person with an annual salary of ${salary} found.")


if __name__ == "__main__":
    app()
