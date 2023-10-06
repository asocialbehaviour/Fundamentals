ammount_of_strings = int(input())

for i in range(ammount_of_strings):
    string = input()
    for index, symbol in enumerate(string):
       if symbol == "," or symbol == "." or symbol == "_":
           break
    if symbol == '.':
        print(f"{string} is not pure!")
    elif symbol == ",":
        print(f"{string} is not pure!")
    elif symbol == "_":
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")