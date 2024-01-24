def collatz_sequence(n):
    steps = []
    while n != 1:
        steps.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    steps.append(1)
    return steps

try:
    print("\nThis is a Collatz Conjecture Calculator")
    start_number = int(input("Enter a positive integer to start the Collatz sequence: "))
    if start_number <= 0:
        print("Please enter a positive integer.")
    else:
        result = collatz_sequence(start_number)
        print("Collatz sequence starting from {}: {}".format(start_number, result))
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
