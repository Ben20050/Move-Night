# functions go here

# checks users enter an integer to a given question
def num_check(question):

    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Invalid answer, please enter an integer")


# main routine goes here
while True:
    name = input("Please enter your name ")
    print()
    age = num_check("Hi {}, please enter your age ".format(name))
    if 12 <= age <= 120:
        break
    elif age < 12:
        print("Sorry you are too young for this movie")
    else:
        print("?? That looks like a typo, please try again ")

print(age)
