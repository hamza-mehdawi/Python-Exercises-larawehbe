"""Exercise 4 """


def find_gpt(ordered_list, target):
    return target in ordered_list         

ordered = []

for i in range(6):
    num = int(input(f"Enter number {i + 1}: "))
    ordered.append(num)

if __name__ == "__main__":

    for x in [5, 10, 15, 20, 25]:
        print(f"{x} in list? Boolean: {find_gpt(ordered, x)} ")
