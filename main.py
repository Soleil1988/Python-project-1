time = input(f'Введите время ')
task = input(f'Введите занятие ')

with open('./output.txt', 'a') as out_file:
    out_file.write(f'{time} --- {task}\n')
