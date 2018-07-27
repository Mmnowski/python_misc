min = 0
max = 100
print("Think of a number between 1 and 100")
while True:
    print("Range:", min, max)
    guess = int(((min+max)/2))
    answer = input("Is your number " + str(guess) + "? (L,H,C) ")
    if (answer == 'L' or answer == 'l'):
        max = guess
    elif (answer == 'H' or answer == 'h'):
        min = guess
    elif (answer == 'C' or answer == 'c'):
        print("I knew that!")
        break
    else:
        print("Sorry, I didn't understand that. (L,H,C)")
