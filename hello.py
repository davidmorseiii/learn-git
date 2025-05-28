#Basic Python Program

user_input = ""

while user_input != "green":
    user_input = input("What is the magic color? ")
    if user_input != "green":
        print("That is not the magic color")

print("Correct! " + user_input + " is the magic color!")