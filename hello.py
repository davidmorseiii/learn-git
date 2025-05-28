#Basic Python Program

user_input = ""
attempts = 0

while user_input.lower() != "green":
    user_input = input("What is the magic color? ")
    attempts += 1
    if user_input != "green":
        print("That is not the magic color")

print(f"Correct! {user_input} is the magic color! It took you {attempts} tries.")