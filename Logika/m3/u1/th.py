with open('t.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)

with open('t.txt', 'a', encoding='utf-8') as file:
    file.write(input("Хто написав ці рядки?"))

with open('t.txt', 'a', encoding='utf-8') as file:
    file.write(input("Хочете добавити цитату? (так/ні)"))