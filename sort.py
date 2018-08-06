# interaktivni zadavani slov a vraceni v abecednim poradi
# konec zadavani slov - stisknout enter

words = []

word = input("Please, write a word: ")

while word != (""):
    words.append(word)
    word = input("Please, write a word: ")          
else:                                             
    print("Your words alphabetically are", sorted(words))








