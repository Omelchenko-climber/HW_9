
USERS = {}


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return 'Give me the name and the phone, please.'
        except TypeError:
            return 'Give me the name, please.'
        except KeyError:
            return 'Check the command you entered and try again, please.'
    return inner


def hello():
    return 'How can I help you?'


@input_error
def add(name: str, phone: str) -> str:
    USERS[name] = phone
    return f'I`m added new user {name}, his phone is {phone}.'


@input_error
def change(name: str, new_phone: str) -> str:
    old_phone = USERS[name]
    USERS[name] = new_phone
    return f'I`m changed the phone number of the user {name} with old phone number {old_phone} to new {new_phone}.'


@input_error
def phone(name: str) -> str:
    if not USERS.get(name):
        return 'Add some users to start, please.'
    else:
        return f'The phone number of the user {name} is {USERS[name]}.'


@input_error
def show_all():
    outcome = ''
    if not USERS:
        return 'List is empty!'
    else:
        for key, value in USERS.items():
            outcome += f'{key}: {value}\n'
        return outcome


def close():
    return 'Good bye!'


@input_error
def show_commands():
    outcome = ''
    for key in COMMANDS.keys():
        outcome += key + '\n'
    return outcome


COMMANDS = {
    'commands': show_commands,
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': close,
    'close': close,
    'exit': close
}


def unknown_command(command: str) -> str:
    return f'Unknown command: "{command}", check your input.'


def main():
    while True:
        user_input = input('Waiting for command (if you want to see all available commands enter "commands"): ')
        if not user_input:
            print('Give me the command, please!')
            continue
        if user_input.lower() in COMMANDS:
            handler = COMMANDS[user_input.lower()]()
            if not handler:
                print(handler)
                break
            else:
                print(handler)
                continue
        command, *args = user_input.strip().split(' ')
        if COMMANDS.get(command.lower()):
            action = COMMANDS.get(command.lower())
            if len(args) > 1:
                name, phone = args
                handler = action(name, phone)
                print(handler)
            else:
                handler = action(args[0])
                print(handler)
        else:
            print(unknown_command(command))


if __name__ == '__main__':
    main()
