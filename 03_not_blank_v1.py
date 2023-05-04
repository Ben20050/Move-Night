# functions go here
def not_blank(question):

    while True:
        user_input = input(question)

        if not user_input.isalpha():
            print("Name CANNOT be blank or contain numbers!")
            continue
        else:
            print(user_input)
            break


# main program goes here
not_blank("What is your name?")
