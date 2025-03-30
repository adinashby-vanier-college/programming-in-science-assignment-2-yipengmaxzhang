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
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] + arr[i]
    return arr

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    transposed = [0] * len(matrix[0])
    for i in range(len(matrix[0])):
        transposed[i] = [row[i] for row in matrix]
    return transposed
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    new_list = [lst[i] for i in range(len(lst)) if i % step == 0]
    return new_list

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    product_list = [a * b for a, b in zip(list1, list2)]
    sum_products = sum(product_list)
    return sum_products

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    rows2 = len(matrix2)
    column1 = len(matrix1[0])
    column2 = len(matrix2[0])
    new_matrix = [[0] * rows2 for i in range(column1)]
    for row in range(rows1):
        for index in range(column2):
            for matrix1_index in range(rows2):
                new_matrix[row][index] += matrix1[row][matrix1_index] * matrix2[matrix1_index][index]
    return new_matrix
