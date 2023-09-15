with open('t.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)

author = input("Вкажіть автора")

with open('t.txt', 'a', encoding='utf-8') as file:
    file.write(f'({author})')