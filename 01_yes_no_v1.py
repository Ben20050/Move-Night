# functions go here


# main routine goes here
want_instructions = input("Do you want to read the instructions? (y/n) ").lower()

if want_instructions == "y":
    print("Instructions go here")
elif want_instructions == "n":
    print("Instructions not printed")
else:
    print("Please answer y/n")

print("we are done")
