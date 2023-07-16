def find_second_largest(arr):
    if len(arr) < 2:
        return "No second largest element exists."
    first_max = float('-inf')
    second_max = float('-inf')
    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    if second_max == float('-inf'):
        return "No second largest element exists."
    else:
        return second_max
A = [2, 1, 2]
result = find_second_largest(A)
print("Second largest element:", result)
