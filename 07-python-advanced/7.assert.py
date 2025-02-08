def start_program(data):
    assert isinstance(data, dict), 'Invalid JSON'

    assert data, "no data found ..."

    print('program loaded successfuly')


if __name__ == '__main__':

    # json: dict = {'name': 'mario'}
    json = {}
    start_program(json)
