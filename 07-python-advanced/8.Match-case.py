status: int = 400

# if status == 400:
#     print('bad request')
# elif status == 403:
#     print('forbidden request')
# elif status == 404:
#     print('not found request')
# else:
#     print('internal server error')


# identical as above

match status:
    case 400:
        print('bad request')
    case 403:
        print('forbidden request')
    case 404:
        print('not found request')
    case _:
        print('internal server error')


# ex
user_input: str = 'find hello.jpg'
p_command = user_input.split()

match p_command:
    case ['find', *images]:
        print(f'finding:{images}')
    case ['download', *images]:
        print(f'downloading:{images}')
    case ['cancle' | 'delete', *images] if len(images) > 1:
        print(f'deleting: {images}')
    case _:
        print('command not found')
