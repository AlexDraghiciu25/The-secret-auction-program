import art
#from os import system   # For delete what was on the screen recently
# You can acces with system("cls")

# Logo printed
print(art.logo)

# We should create an empty dictionary first
players = {}

name = input("What is your name?: ")
bid = input("What's your bid?: $")

players[name] = bid

continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
ok = 0

if continue_bid == "yes":
    ok = 1

while ok == 1:
    ok = 0
    print("\n" * 20)
    # Equivalent of this print is
    # system("cls")

    name = input("What is your name?: ")
    bid = input("What's your bid?: $")

    players[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if continue_bid == "yes":
        ok = 1

maximum = 0
name_of_winner = ""
for key in players:
     if int(players[key]) > maximum:
         maximum = int(players[key])
         name_of_winner = key

print(f"The winner is {name_of_winner} with a bid of ${maximum}")