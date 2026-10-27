# print numbers from 1 to n
def numbers(n):

    if n <= 0:
        return

    numbers(n - 1)
    print(n)


numbers(5)


# print number from n to 1
def numbers(n):

    if n <= 0:
        return
    print(n)
    numbers(n - 1)


numbers(5)


# sum of nubers upto n
def sum(n):

    if n <= 0:
        return 0

    return n + sum(n - 1)


print(sum(6))


# factorial
def factorial(n):

    if n <= 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# calculate power of a number
def power(n, exponent):

    if exponent <= 0:
        return 1
    return n * power(n, exponent - 1)


print(power(5, 3))


# count digits of a number
def count_digits(num):

    if num <= 0:
        return 0
    num = num // 10

    return 1 + count_digits(num)


print(count_digits(45248546))


# sum of list of elements
def list_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + list_sum(numbers[1:])


numbers = [10, 20, 30, 40, 50]
print(list_sum(numbers))


# reverse a string
def reverse_string(word):

    if word == "":
        return ""
    return reverse_string(word[1:]) + word[0]


print(reverse_string("hyderabad"))


# find the largest number in list
def largest(numbers):
    if len(numbers) == 1:
        return numbers[0]
    large = largest(numbers[1:])
    if numbers[0] > large:
        return numbers[0]
    return large


numbers = [10, 25, 36, 5, 58, 75]
print(largest(numbers))
# find minimum value in a string


def smallest(numbers):
    if len(numbers) == 1:
        return numbers[0]
    minimum = smallest(numbers[1:])
    if numbers[0] > minimum:
        return minimum
    return numbers[0]


numbers = [10, 25, 36, 5, 58, 75]
print(smallest(numbers))


# find a element in a list recursively
def find(numbers, target):
    if numbers == []:
        return "number is not found"
    if numbers[0] == target:
        return "found the number"
    return find(numbers[1:], target)


print(find([10, 58, 65, 32, 91], 100))


# Count how many times a particular value occurs in a list.
def repetition(numbers, target):
    if numbers == []:
        return 0
    if numbers[0] == target:
        return 1 + repetition(numbers[1:], target)
    return repetition(numbers[1:], target)


print(repetition([10, 25, 35, 10, 10], 10))


# Check whether a string is a palindrome using recursion.
def check_pallindrome(text):
    if len(text) == 1 or len(text) == 0:
        return True
    if text[0] == text[-1]:
        return check_pallindrome(text[1:-1])
    return False


print(check_pallindrome("cat"))

#sun of nested list using recursion
# sum of nested list
def nested_list_sum(numbers):
    total = 0
    for i in numbers:
        if type(i) == list:
            total += nested_list_sum(i)
        else:
            total += i
    return total


print(nested_list_sum([1, 2, [3, 4, 5], 10]))

