def read_data(file):
    '''
    Читает файл
    '''
    with open(file) as f:
        data = f.readlines()[1:]
        return data

