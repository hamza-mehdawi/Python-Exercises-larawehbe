"""Exercise 2 - Even and odd."""


def Exercise_2():
    n = int(input("Enter a number: "))
    if n % 4 == 0:
        print(f"{n} is a multiple of 4")
    elif n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

    num = int(input("Enter a number to check : "))
    check = int(input("Enter a number to divide by (check): "))
    print(f"{check} divides {num} evenly" if num % check == 0 else f"{check} does not divide {num} evenly")




if __name__ == "__main__":
    Exercise_2()
