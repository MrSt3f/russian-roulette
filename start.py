import random
import os
import time



def main():
    os.system('cls')


    number = random.randint(1, 10)
    
    while True:
        print(" ")
        guess = int(input("\033[1;32mTest your luck, choose a number between 1 and 10: \033[1;32m"))
        if guess < 1 or guess > 10:
            print("")
            print("\033[0;31mYour number should be between 1 and 10.\033[0;31m")
            time.sleep(2)
            main()
        else:
            break
    
    if guess == number:
        print(" ")
        print("Good job, you won the roulette")
        time.sleep(2)
        main()
    else:
        print(" ")
        print("You are dead, your number was:", number)
        time.sleep(2)
        main()

while True:
    main()
