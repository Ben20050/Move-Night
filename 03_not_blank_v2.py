# function go here

# checks that user response is not blank
def not_blank(question):

    while True:
        user_input = input(question)

        if user_input == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return user_input


# main program goes here
while True:
    name = not_blank("Enter your name (or 'xxx' to quit)")
    if name == "xxx":
        break


print("We are done")
