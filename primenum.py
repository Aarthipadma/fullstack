def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    if number == 2:
        return True  # 2 is a prime number
    
    if number % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    
    # Check for factors from 3 to the square root of the number
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False  # Found a divisor, not prime
    
    return True  # No divisors found, prime number

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is prime and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")