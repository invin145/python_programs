def generate_pronic_numbers(n):
    pronic_numbers = []
    for i in range(n):
        pronic_numbers.append(i * (i + 1))
    return pronic_numbers

n = int(input("Enter the number of pronic numbers to generate: "))
pronic_numbers = generate_pronic_numbers(n)
print("The first", n, "pronic numbers are:", pronic_numbers)