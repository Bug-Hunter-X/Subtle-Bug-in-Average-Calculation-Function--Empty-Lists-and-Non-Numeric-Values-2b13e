def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    # Check if all elements are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1,2,0,4,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zero is: {average_zero}")

#Example of invalid input
try:
    invalid_list = [1,2,"a",4,5]
    calculate_average(invalid_list)
except ValueError as e:
    print(f"Error: {e}")
