
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
    return 'hello'


@input_error
def add(*args):
    name, phone = args
    USERS[name] = phone
    return f'I`m added new user {name}, his phone is {phone}.'


@input_error
def change(*args):
    name, new_phone = args
    old_phone = USERS[name]
    USERS[name] = new_phone
    return f'I`m changed the phone number of the user {name} with old phone number {old_phone} to new {new_phone}.'


@input_error
def phone(args):
    return f'The phone number of the user {args} is {USERS[args]}.'


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
    return False


@input_error
def show_commands():
    result = ''
    for key in COMMANDS.keys():
        result += key + '\n'
    return result


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


@input_error
def command_handler(user_input: str):
    if user_input.lower() in COMMANDS:
        action = COMMANDS[user_input.lower()]
        args = ''
        action = action()
    else:
        command, *args = user_input.split()
        action = COMMANDS[command.lower()]
        action = action(*args)
    return action


def main():
    while True:
        user_input = input('Waiting for command (if you want to see all availble commands enter "commands"): ')
        if not user_input:
            print('Give me the command!')
            continue
        outcome = command_handler(user_input)
        if not outcome:
            print('Good bye!', end = '')
            break
        elif outcome == 'hello':
            print('How can I help you?')
            continue
        print(outcome)


if __name__ == '__main__':
    main()
