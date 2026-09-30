# this is a python program to creat a calculator at basics level

#  it have 3 steps to create a calculator
#  1. funcution to opperation
#  2. users input
#  3. prrint result

# step 1 (function creation)
# function to add two numbers
def add(num1, num2):
    return num1 + num2

#function to sub two numbers
def sub(num1, num2):
    return num1 - num2

# function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
        return num1 / num2

# function to find average of two numbers
def avg(num1, num2):
    return (num1 + num2) / 2

# step 2 (user input)

print ("please select any opption from below:\n "\
       "1. Addition\n " \
       "2. Subtraction\n " \
       "3. Multiplication\n " \
       "4. Division\n " \
       "5. Average\n")

select = int(input("Select opption from 1,2,3,4,5"))

number1 =int(input("Enterfirst number:"))
number2 =int(input("Enter second number:"))

# step 3 (print result)

if select == 1:
    print(number1, "+", number2, "= ",\
        add(number1, number2))
        
elif select ==2:
    print(number1, "-", number2,"= ",\
        sub(number1, number2))

elif select ==3:
    print(number1, "*", number2,"= ",\
        multiply(number1,number2))

elif select ==4:
    print(number1, "/", number2, "= ",\
        divide(number1, number2))

elif select ==5:
    print("(", number1, "+", number2, ")", "/", "2", "= ",\
        average(number1, number2))

else:
    print("this option is invalid choos a valid option")

user = input("do you want to continue yes or no")