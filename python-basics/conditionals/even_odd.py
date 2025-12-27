s = input("enter the number: ")

if s.isdigit():
    n = int(s)

    if n % 2 == 0:
        print(f"The number {n} is even")
    else:
        print(f"The number {n} is odd")
else:
    print("Invalid input. Please enter a positive integer.")
