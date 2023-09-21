def find_greatest(numbers):
    if not numbers:
        return "The list is empty."
    
    greatest = numbers[0]  # Initialize the greatest as the first number
    
    for num in numbers:
        if num > greatest:
            greatest = num  # Update the greatest if a larger number is found
    
    return greatest

# Input a list of numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers_list = [int(num) for num in input_numbers.split()]

# Find and display the greatest number
result = find_greatest(numbers_list)
print(f"The greatest number is: {result}")