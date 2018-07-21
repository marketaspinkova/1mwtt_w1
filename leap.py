year1 = int(input("Give me a year, please. "))
while year1 < 0:
    print("Something after Christ.")
    year1 = int(input("Give me a year, please. "))

year2 = int(input("And another one. "))
while year2 <= year1:
    print("A latter than the first one, please. ")
    year2 = int(input("And another one. "))

for year in range(year1, year2):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print ("Leap years are: ")
        print(year, end=", ")
        
 print("tady Eva, dalsi zkouska")
    
