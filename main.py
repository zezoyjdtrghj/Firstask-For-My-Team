def find_largest(numbers):
    max=numbers[0]

    for nums in numbers:
      if nums>max:

        max=nums

    return max
    


numbers = [4, 12, 7, 19, 3]

print(find_largest(numbers))