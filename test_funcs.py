from functions import _find_insert_position_by_salary, _find_insert_position_by_name

records_by_salary = [
    [1, "Eve", 25000.0],
    [2, "Charlie", 30000.0],
    [3, "Bob", 40000.0],
    [4, "David", 50000.0],
    [5, "Alice", 60000.0]
]

records_by_name = [
    [1, "Alice", 25000.0],
    [2, "Bob", 30000.0],
    [3, "Charlie", 40000.0],
    [4, "David", 50000.0],
    [5, "Eve", 60000.0]
]

def test_find_insert_position_by_salary():
    # Testando a inserção de um salário que já existe
    position = _find_insert_position_by_salary(records_by_salary, 40000.0)
    print(f"Position to insert $40000: {position}")
    records_by_salary.insert(position, [6, "Frank", 40000.0])

    # Testando a inserção de um salário que não existe
    position = _find_insert_position_by_salary(records_by_salary, 45000.0)
    print(f"Position to insert $45000: {position}")
    records_by_salary.insert(position, [7, "George", 45000.0])

    # Testando a inserção de um salário no início
    position = _find_insert_position_by_salary(records_by_salary, 20000.0)
    print(f"Position to insert $20000: {position}")
    records_by_salary.insert(position, [8, "Hannah", 20000.0])

    # Testando a inserção de um salário no final
    position = _find_insert_position_by_salary(records_by_salary, 70000.0)
    print(f"Position to insert $70000: {position}")
    records_by_salary.insert(position, [9, "Ian", 70000.0])
    
    # Verificando se a lista ainda está ordenada
    for record in records_by_salary:
        print(record)
    
    # Confirmar que a lista está ordenada por salário
    assert all(records_by_salary[i][2] <= records_by_salary[i+1][2] for i in range(len(records_by_salary)-1))


def test_find_insert_position_by_name():
    # Testando a inserção de um nome que já existe
    position = _find_insert_position_by_name(records_by_name, "Charlie")
    print(f"Position to insert Charlie: {position}")
    records_by_name.insert(position, [6, "Frank", 40000.0])
    
    # Testando a inserção de um nome que não existe
    position = _find_insert_position_by_name(records_by_name, "George")
    print(f"Position to insert George: {position}")
    records_by_name.insert(position, [7, "George", 45000.0])
    
    # Testando a inserção de um nome no início
    position = _find_insert_position_by_name(records_by_name, "Aaron")
    print(f"Position to insert Aaron: {position}")
    records_by_name.insert(position, [8, "Aaron", 20000.0])
    
    # Testando a inserção de um nome no final
    position = _find_insert_position_by_name(records_by_name, "Zelda")
    print(f"Position to insert Zelda: {position}")
    records_by_name.insert(position, [9, "Zelda", 70000.0])
    
    # Verificando se a lista ainda está ordenada
    for record in records_by_name:
        print(record)

test_find_insert_position_by_salary()
test_find_insert_position_by_name()