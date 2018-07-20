from random import randrange

grandma = input("HOW ARE YOU, DEAR?")
while grandma.islower():
    print("HUH?! SPEAK UP SONY!")
    grandma = input("HOW ARE YOU, DEAR?")
if grandma.isupper and grandma != str("BYE"):
    print("NO, NOT SINCE", randrange(1930, 1951))
    grandma = input("HOW ARE YOU, DEAR?")
if grandma == str("BYE"):
    print("BYE")
