count = int(input('Сколько новых задач вы хотите добавить? Введите число '))

while count > 0:
    day = input('Введите день задачи ')
    time = input('Введите время задачи ')
    name = input('Введите название задачи ')
    day_week = [day]
    task = [time, name]
    with open('./schedule.txt', 'a') as schedule:
        schedule.write(day_week[0] + '\n' + task[0] + ' --- ' + task[1] + '\n')
    count = count-1
