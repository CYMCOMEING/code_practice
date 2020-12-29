import random

def get_dxdata():
    date = ''
    title = ''
    content = ''
    num = random.randint(2, 366)
    with open(r"./bin/dx2019.txt", "r", encoding="utf-8") as f:
        for i in range(num):
            date = f.readline()
            title = f.readline()
            content = f.readline()
            if not (date and title and content):
                break
    return date, title, content