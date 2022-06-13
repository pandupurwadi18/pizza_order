# -- Pizza Order --
# Pandu Purwadi

print("Welcome to Pizza Pythonizta!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    else :
        print ("Honestly, add pepperoni is the best choice")
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    else :
        print ("Honestly, add pepperoni is the best choice")
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    else :
        print ("Honestly, add pepperoni is the best choice")
else :
    print("Please try again typing your size pizza")
if extra_cheese == "Y":
    bill += 1
else :
    print("No regret without extra cheese")

print(f"Your final bill is: ${bill}.")