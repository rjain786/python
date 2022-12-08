new_list = []
max_digit = int(input("how many digits  in a number to add to a list: "))


while max_digit > 0:
    num = input("Enter an integer: ")
    if num.isdigit():
        new_list.append(int(num))
            
    else:
        print("invalid input, not counted")
        
    max_digit -= 1

print("done")
print("Your new list is:", new_list)


choose =  input("Enter 'm' for multiply and 'a' for addition:  ").lower()
sum = 0
multiply = 1
if choose == "m":
    for num in new_list:
        multiply = multiply * num
    print("multiplication of the numbers are: ", multiply)
elif choose == "a":
    for num in new_list:
        sum += num
    print("addition of the numbers are: ", sum)
else:
    print("invalid choice")

print("all done, see you again soon!")

    



