print("collecting user input")
all_user_input = []
while True:
    try:
        single_user_input = input("Type something: ")
        all_user_input.append(single_user_input)
    except EOFError:
        print("finished collecting user input")
        break
print("printing user input in opposite order")
for line in reversed(all_user_input):
    print(line)