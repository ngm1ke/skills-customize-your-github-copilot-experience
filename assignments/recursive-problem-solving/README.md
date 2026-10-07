# 📘 Assignment: Recursive Problem Solving

## 🎯 Objective

Practice recursion by solving problems with functions that call themselves. Implement a factorial function, then apply the same base-case and recursive-case reasoning to sum a list.

## 📝 Tasks

### 🛠️ Calculate a Factorial Recursively

#### Description
Complete `factorial(n)` so it returns the factorial of a non-negative integer using recursion.

#### Requirements
Completed program should:

- Return `1` for the base case `factorial(0)`.
- For positive `n`, return `n * factorial(n - 1)`.
- Work for non-negative integers without using loops.
- Produce `factorial(5) == 120`.

### 🛠️ Sum a List Recursively

#### Description
Complete `sum_list(numbers)` to return the sum of the integers in a list, using recursion instead of a loop.

#### Requirements
Completed program should:

- Return `0` when the list is empty.
- Add the first number to the recursive sum of the remaining numbers.
- Work with both an empty list and a list containing multiple integers.
- Produce `sum_list([2, 4, 6]) == 12`.
