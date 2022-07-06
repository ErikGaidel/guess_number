from random import randint


def is_valid(inp: str):
    if inp.isdigit():
        return 1 <= int(inp) <= 100
    return False


def guess_number():
    n1 = ""
    while not n1.isdigit():
        n1 = input("Enter the max random number or q to exit: ")
        if n1 == "q":
            print("Bye-bye!")
            return False

    n = randint(1, int(n1))
    count = 0

    inp = input("Enter the number between 1 and 100 to start new game, or q to exit:")
    while True:
        if inp == "q":
            print("Bye-bye!")
            return False
        if not is_valid(inp):
            inp = input("Please, enter the correct number between 1 and 100, or q to exit:")
            continue
        count += 1
        inp = int(inp)
        if inp < n:
            inp = input("Your number less than n! Try again (q exit):")
        elif inp > n:
            inp = input("Your number bigger than n! Try again (q exit):")
        else:
            print(f"Congratulation! You guess! Your tryings {count}")
            break

    ans = input("You wanna play again (y/n)? ")
    if ans == "y":
        return True
    else:
        print("Bye-bye!")
        return False


print("Welcome to guess_number!")
cont = True
while cont:
    cont = guess_number()
