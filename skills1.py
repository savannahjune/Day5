# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for i in range(len(number_list)):
        if number_list[i] % 2 != 0:
            new_list.append(number_list[i])
        else:
            continue
    return new_list

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0:
            new_list.append(number_list[i])
        else:
            continue
    return new_list   

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_four_greater = []
    for i in range(len(word_list)):
        if len(word_list[i]) >= 4:
            new_four_greater.append(word_list[i])
        else:
            continue
    return new_four_greater

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    smallest = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] < smallest:
            smallest = number_list[i]
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    largest = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] > largest:
            largest = number_list[i]
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    half_list = []
    for i in range(len(number_list)):
        half_list.append(float(number_list[i]) / 2)
    return half_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    list_lengths = []
    for i in range(len(word_list)):
        length = len(word_list[i])
        list_lengths.append(length)
    return list_lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum_of_list = 0
    print number_list
    for i in range(len(number_list)):
        sum_of_list += number_list[i]
    return sum_of_list

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    mult_of_list = 1
    for i in range(len(number_list)):
        mult_of_list = mult_of_list * number_list[i]
    return mult_of_list

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    joined_string = ''
    for i in range(len(word_list)):
        joined_string = joined_string + " " + word_list[i]
    return joined_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    total_of_numbers = 0
    for i in range(len(number_list)):
        total_of_numbers += float(number_list[i])
    # print total_of_numbers
    average_of_list = total_of_numbers / len(number_list)
    return average_of_list

print all_odd(number_list)
print all_even(number_list)
print long_words(word_list)
print smallest(number_list)
print largest(number_list)
print halvesies(number_list)
print word_lengths(word_list)
print sum_numbers(number_list)
print mult_numbers(number_list)
print join_strings(word_list)
print average(number_list)