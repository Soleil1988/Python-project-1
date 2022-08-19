with open('./output.txt', 'r+') as f:
    text: str = f.read()
    print(text)
    text = text.replace("\t", " ").split("\n")
    done_name = []
    for lines in text:
        done_name.append('\n' + '- ' + lines + ' / labels:"MERA_HardPhones_Auto"')
    f.write("".join(done_name))
