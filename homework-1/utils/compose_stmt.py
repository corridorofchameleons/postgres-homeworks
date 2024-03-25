def convert_data(data):
    '''
    Преобразует данные в строку, понимаемую SQL
    '''
    data = [d.rstrip() for d in data]
    values = ''
    for d in data:
        tmp = [d.replace("'", "-").replace('"', "'") for d in d.split(',')]
        tmp = ', '.join([f'{t}' for t in tmp])
        values += f'({tmp}),'

    values = values[:-1]

    return values


def insert_data(data, table, echo=True):
    '''
    Добавляет данные в таблицу
    data: тело csv-файла
    table: название таблицы
    echo: вывод текста запроса на экран
    '''
    values = convert_data(data)

    stmt = f'''
    INSERT INTO {table}
    VALUES {values};
    '''
    if echo:
        print(stmt)

    return stmt
