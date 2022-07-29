time = input(f'Введите время ')
task = input(f'Введите занятие ')


def print_hi(name):
    print(f'Hi, {name}, your schedule is')


with open('./output.txt', 'a') as out_file:
    out_file.write(f'{time} --- {task}\n')
