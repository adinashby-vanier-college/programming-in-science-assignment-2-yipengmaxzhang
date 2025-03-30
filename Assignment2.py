# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    position = tuple()
    initial_max = max(numbers)
    for i in range(len(numbers)):
        if numbers[i] == max(numbers):
            position = position + (i, )
    for max_index in range(len(position)):
        numbers[position[max_index]] = 0
    if len(numbers) <= 1:
        result = None
    else:
        result = max(numbers)
    return (initial_max, result)
# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
  for number_at_index in range(len(numbers)):
    for other_index_numbers in range(len(numbers)):
      if numbers[other_index_numbers] == numbers[number_at_index] and not number_at_index == other_index_numbers:
        numbers[other_index_numbers] = 0
  result = sorted(numbers)
  while result[0] == 0:
    del result[0]
  return result
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    return []

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [[]]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return []

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return 0

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    return [[0, 0], [0, 0]]