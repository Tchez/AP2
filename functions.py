import csv
import random

from time import time
from faker import Faker

def create_files() -> None:
    """
    Cria os arquivos CSV ("pessoas_by_name.csv" e "pessoas_by_salary.csv") com as colunas ID, nome e salário.
    """
    with open('pessoas_by_name.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Annual Salary"])  
    
    with open('pessoas_by_salary.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Annual Salary"])


def populate_csv(num_records: int):
    """
    Popula os arquivos CSV com dados fictícios.

    Parâmetros:
        - num_records (int): número de registros a serem adicionados.

    Retorna:
        None
    """
    fake = Faker()
    for _ in range(num_records):
        name = fake.name()
        salary = fake.random_int(min=20000, max=100000)
        create_person(name, salary)


def create_person(name: str, salary: float):
    """
    Adiciona um registro aos arquivos CSV de forma ordenada. Usando busca binária.

    Parâmetros:
        - name (str): nome da pessoa.
        - salary (float): salário anual da pessoa.
    """
    name_records, salary_records = _load_records()

    new_id = _generate_id()
    new_record = [new_id, name, salary]
    
    pos_salary = _find_insert_position_by_salary(salary_records, salary)
    salary_records.insert(pos_salary, new_record)
    
    pos_name = _find_insert_position_by_name(name_records, name)
    name_records.insert(pos_name, new_record)
    
    _write_records_to_csv('pessoas_by_salary.csv', salary_records)
    _write_records_to_csv('pessoas_by_name.csv', name_records)


def search_by_name(name: str) -> list or None:
    """
    Usa busca binária para encontrar um registro pelo nome.

    Parâmetros:
    - name (str): Nome a ser procurado.

    Retorna:
    - Registro encontrado ou None se não for encontrado.
    """
    records = _load_records_from_file('pessoas_by_name.csv')
    
    achou = False
    inicio = 0
    fim = len(records) - 1
    meio = (inicio + fim) // 2

    while inicio <= fim and not achou:       
        current_name = records[meio][1]  # Coluna de nome

        if current_name == name:
            achou = True
        else:
            if name < current_name:
                fim = meio - 1
            else:
                inicio = meio + 1
            meio = (inicio + fim) // 2

    if achou:
        return records[meio]
    else:
        return None


def search_by_salary(salary: float) -> list or None:
    """
    usa busca binária para encontrar um registro pelo salário.
    
    Parâmetros:
    - salary (float): Salário a ser procurado.
    
    Retorna:
    - Registro encontrado ou None se não for encontrado.
    """
    records = _load_records_from_file('pessoas_by_salary.csv')
    
    achou = False
    inicio = 0
    fim = len(records) - 1
    meio = (inicio + fim) // 2
    
    while inicio <= fim and not achou:
        current_salary = float(records[meio][2]) # Coluna de salário
        
        if current_salary == salary:
            achou = True
        else:
            if salary < current_salary:
                fim = meio - 1
            else:
                inicio = meio + 1
            meio = (inicio + fim) // 2
        
    if achou:
        return records[meio]
    else:
        return None


def _generate_id() -> int:
    """
    Gera um ID único com base no timestamp.

    Retorna:
        int: ID gerado.
    """
    timestamp_part = int(time() * 1000)
    random_part = random.randint(0, 999)
    return timestamp_part + random_part


def _load_records_from_file(filename: str) -> list:
    """
    Carrega os registros de um arquivo CSV especificado.

    Parâmetros:
    - filename (str): Nome do arquivo CSV.

    Retorna:
    - Lista de registros.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return list(reader)


def _load_records():
    """
    Carrega os registros dos arquivos ("pessoas_by_name.csv" e "pessoas_by_salary.csv").
    """
    name_records = _load_records_from_file('pessoas_by_name.csv')
    salary_records = _load_records_from_file('pessoas_by_salary.csv')
    
    return name_records, salary_records


def _find_insert_position_by_salary(X: list, salary: float) -> int:
    """
    Usa busca binária ordenada para encontrar a posição correta para inserir um novo salário na lista de dados.

    Parâmetros:
    - X: lista de registros ordenados por salário.
    - salary: salário a ser inserido.

    Retorna:
    - Índice da posição correta para inserir o novo registro.
    """
    inicio = 0
    fim = len(X) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        current_salary = float(X[meio][2])  # Coluna de salário

        if current_salary == salary:
            return meio
        elif salary < current_salary:
            fim = meio - 1
        else:
            inicio = meio + 1

    return inicio


def _find_insert_position_by_name(X: list, name: str) -> int:
    """
    Usa busca binária ordenada para encontrar a posição correta para inserir um novo nome na lista de dados.

    Parâmetros:
    - X: lista de registros ordenados por nome.
    - name: nome a ser inserido.

    Retorna:
    - Índice da posição correta para inserir o novo registro.
    """
    inicio = 0
    fim = len(X) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        current_name = X[meio][1]  # Coluna de nome

        if current_name == name:
            return meio
        elif name < current_name:
            fim = meio - 1
        else:
            inicio = meio + 1

    return inicio


def _write_records_to_csv(filename: str, records: list) -> None:
    """
    Escreve os registros no arquivo CSV especificado.

    Parâmetros:
        - filename (str): Nome do arquivo CSV.
        - records (list): Lista de registros a serem escritos.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Annual Salary"])
        writer.writerows(records)
