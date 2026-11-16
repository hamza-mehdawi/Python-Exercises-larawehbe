"""Exercise 3 - New list append and print last and first"""


def get_first_and_last(numbers):
    if not numbers:
        return []
    return [numbers[0], numbers[-1]]

numbers_list = []

for i in range(6):
    num = int(input(f"Enter number {i + 1}: "))
    numbers_list.append(num)




if __name__ == "__main__":
    result = get_first_and_last(numbers_list)
    print("Full list:", numbers_list)
    print("First and last:", result)  

