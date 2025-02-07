# user_input = '0'

# if user_input == '0':
#     raise Exception('please never use 0')


is_connected = False


def connect_to_internet():
    if not is_connected:
        raise Exception('NO internet!!!')
    else:
        print('connected to the internet')


try:
    connect_to_internet()
except Exception as e:
    print(e)
