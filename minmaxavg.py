numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

minim = numbers[0]
maxim = numbers[0]
list_sum = 0


for number in numbers:
    list_sum = list_sum + number
    if number < minim:
        minim = number
    elif number > maxim:
        maxim = number

print("The minimum number of the list is: ",minim)
print("The maximum number of the list is: ",maxim)
print("The avarage of the list is: ", list_sum/ len(numbers))