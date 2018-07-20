number = ""

for number in range(101):
    number = 100 - number
    if number > 1 or number == 0:
        print(number, "bottles of beer on the wall,", number, "bottles of beer. \nTake one down and pass it around,", number, "bottles of beer on the wall.")
    if number == 1:
        print(number, "bottle of beer on the wall,", number, "bottle of beer. \nTake one down and pass it around,", number, "bottle of beer on the wall.")