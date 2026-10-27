# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
X = 10
X = X + 3
print(13)
# TODO: Multiply y by 2 using the *= operator
y = 5
y *= y * 2
print(y)
# TODO: Divide x by y and store the result in a variable called 'result'
x = y
x = x / y
result = x/y
print(result)
# TODO: Print the value of 'result'
print(x/y)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 10
b = 5
if a > b:
  print("a is greater than b")
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
a = 5
b = 5
c = 6
if b % 2 == 0:
 print("b is even")
print("a is even to b")
# TODO: Create a condition that checks if c is less than or equal to a
if c <= a:
  print("c is less than or equal to a")
else: 
  print("c is greater than a")
# TODO: Combine the above conditions using logical operators to create a 'final_condition'

# The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
if (a < b) or (b % 2 == 0 and c <= a) :
  print("Final condition is True")
else:
  print("Final condition is False")
# TODO: Print the value of 'final_condition'
a = 10
b = 4
c = 8
Final_condition = (a > b) or (b % 2 == 0 and c <= a)
print(Final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("Enter test score 0-100"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if 90 <= score <= 100:
  grade = "A"
elif 80 <= score <= 89:
  grade = "B"
elif 70 <= score <= 79:
  grade = "C"
elif 60 <= score <= 69:
  grade = "D"
else:
  grade = "F"
  print(f"Grade: {grade}")

# TODO: Print the grade for the given score
score = int(input("Enter test score 0-100"))
# Grading System
if 90 <= score <= 100:
  grade = "A"
elif 80 <= score <= 89:
  grade = "B"
elif 70 <= score <= 79:
  grade = "C"
elif 60 <= score <= 69:
  grade = "D"
else:
  grade= "F"
  print(f"score {score}, grade {grade}")
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter number"))
num2 = float(input("Enter number"))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("+, -, *, /")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
# TODO: Handle the case of division by zero
num1 = float(input("Enter number"))
num2 = float(input("Enter number"))
operation = input("+, -, *, /")
if operation == "+":
 result = num1 + num2
elif operation == "-":
 result = num1 - num2
elif operation == "*":
 result = num1 * num2
elif operation == "/":
 if num2 != 0:
  result = num1 / num2
else:
  result = "Error: cannot divide by zero"
result = "Invalid operation"
print(f"Results: {result}")
if num2 !=0:
  result = num1 / num2
else:
  result = "Error: cannot divide by zero"
  print(f"Result: {result}")
# TODO: Print the result of the operation
print(f"Result: {result}")