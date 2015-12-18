from datetime import datetime
import json


def get_current_date():
    date_now = datetime.now()
    return "{}.{}.{}".format(date_now.day, date_now.month, date_now.year)


def read_json():
    json_file = 'food.json'
    with open(json_file, 'r') as f:
        diary = json.load(f)

    return diary


def write_json(dict):
    json_file = 'food.json'
    with open(json_file, 'w') as f:
        json.dump(dict, f)


def add_meal(meal):
    diary = read_json()
    current_date = get_current_date()

    if current_date in diary:
        diary[current_date].append(meal)
    else:
        diary[current_date] = [meal]

    write_json(diary)

    return 'OK, it\'s done'


def list_meal(date):
    diary = read_json()
    if date in diary:
        return '\n'.join(diary[date])
    else:
        return 'No meal for this day.'


def food_diary(command, parameter):
    if command == 'list':
        return list_meal(parameter)
    elif command == 'meal':
        return add_meal(parameter)
    else:
        return 'Wrong command. Try again.'


def main():
    # print(get_current_date())
    # # dict = {'rumen': 'hahaha'}
    # # write_json(dict)
    # print(read_json())
    # print(add_meal('bob'))
    # print(add_meal('leshta'))
    # print(list_meal('4.12.2015'))
    # print(list_meal('5.12.2015'))

    menu = (
        'Hello and Welcome!' + '\n'
        + 'Choose an option.' + '\n'
        + '1. meal - to write what are you eating now.' + '\n'
        + '2. list <dd.mm.yyyy> - lists all the meals that you ate that day'
        + '\n'
        + '3. help - to show help messege.' + '\n'
        + '4. exit - to exit from the program.')

    help = (
        '1. meal - to write what are you eating now.' + '\n'
        + '2. list <dd.mm.yyyy> - lists all meals that you ate that day' + '\n'
        + '3. help - show help messege.' + '\n'
        + '4. exit - to exit from the program' + '\n')

    print(menu)

    while True:
        user_input = input('Enter command> ')
        split_input = user_input.split()
        command = split_input[0]

        if command == 'help':
            print(help)
        elif command == 'exit':
            break
        else:
            parameter = split_input[1]
            print(food_diary(command, parameter))

if __name__ == '__main__':
    main()
