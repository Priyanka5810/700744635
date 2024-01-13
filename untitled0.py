
#PROGRAM 1
# Input the string "Python"
ip = list(input("Enter the string: "))

# Deleting at least 2 characters
if len(ip) >= 2:
    del ip[:2]

# Reverse the obtained string
resultant_string = ip[::-1]

# Print the final reversed string
print("Sample output:")
print("".join(resultant_string))

#-------------------------------------------------

#PROGRAM 2
# Taking two numbers from the user
n1 = int(input("First number: "))
n2 = int(input("Second number: "))

# Performing arithmetic operations
add_result = n1 + n2
sub_result = n1 - n2
multi_result = n1 * n2
div_result = n1 / n2

# Print the results of arithmetic operations
print("Arithmetic Operations:")
print(f"Addition: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {multi_result}")
print(f"Division: {div_result}")

#-------------------------------------------------

#PROGRAM 3
# Taking a sentence from the user
inp_sentence = input("Enter a sentence: ")

# Replacing each occurrence of 'python' with 'pythons'
op_sentence = inp_sentence.replace('python', 'pythons')

# Print the modified sentence
print("Sample output:")
print(op_sentence)

#-------------------------------------------------

#PROGRAM 4
# Take the class score from the user
cls_score = float(input("Enter class score: "))

# Determining the letter grade based on the grading scheme
if 90 <= cls_score <= 100:
    grade = 'A'
elif 80 <= cls_score < 90:
    grade = 'B'
elif 70 <= cls_score < 80:
    grade = 'C'
elif 60 <= cls_score < 70:
    grade = 'D'
else:
    grade = 'F'

# Print the letter grade
print(f"The grade {cls_score} is: {grade}")
