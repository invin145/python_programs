def is_neon_number(number):
    # Calculate the square of the number
    square = number * number
    
    # Calculate the sum of the digits in the square
    digit_sum = sum(int(digit) for digit in str(square))
    
    # Check if the digit sum is equal to the original number
    return digit_sum == number

# Input a number to check if it's a neon number
number = int(input("Enter a number: "))

if is_neon_number(number):
    print(number, "is a neon number.")
else:
    print(number, "is not a neon number.")
