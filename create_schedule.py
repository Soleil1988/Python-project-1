new_task = input('Введите время новой задачи и её название через пробел ')
task = new_task.split(' ')
print(task)







# with open('./schedule.txt', 'a') as schedule:
#     text: str = f.read()
#     print(text)
#     text = text.replace("\t", " ").split("\n")
#     done_name = []
#     for lines in text:
#         done_name.append('\n' + '- ' + lines + ' / labels:"MERA_HardPhones_Auto"')
#     f.write("".join(done_name))