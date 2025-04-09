# Program to print the ASCII value of a character
char = input("Enter a character: ")
print("The ASCII value of", char, "is", ord(char))


# Program to find the difference of two integers using ^ operator
a = int(input("Enter first integer (<= 10): "))
b = int(input("Enter second integer (<= 10): "))
difference = (a ^ b) - 2 * (a & b)
print("The difference is:", difference)


# Program to multiply a number by 2 without using * operator
num = int(input("Enter a number: "))
result = num << 1
print("The result is:", result)

# Program to calculate interest on a loan amount
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (years): "))
interest = (principal * rate_of_interest * time) / 100
print("The interest is:", interest)

# Program to compute the area of a circle
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)

# Program to compute n + nn + nnn
n = input("Enter an integer: ")
nn = n + n
nnn = n + n + n
result = int(n) + int(nn) + int(nnn)
print("The result is:", result)


# Program to reverse a 5-digit number without using a loop
num = input("Enter a 5-digit number: ")
reversed_num = num[::-1]
print("The reversed number is:", reversed_num)



# Program to interchange the contents of C and D
C = input("Enter value for C: ")
D = input("Enter value for D: ")
C, D = D, C
print("After interchange, C =", C, "and D =", D)


# Program to obtain the sum of the first and last digit of a four-digit number
num = input("Enter a four-digit number: ")
first_digit = int(num[0])
last_digit = int(num[-1])
sum_digits = first_digit + last_digit
print("The sum of the first and last digit is:", sum_digits)


# Program to find the total number of illiterate men and women
population = 80000
men_percentage = 52
literacy_percentage = 48
literate_men_percentage = 35

total_men = (men_percentage / 100) * population
literate_men = (literate_men_percentage / 100) * population
literate_women = (literacy_percentage / 100) * population - literate_men

illiterate_men = total_men - literate_men
illiterate_women = population - total_men - literate_women

print("Total illiterate men:", illiterate_men)
print("Total illiterate women:", illiterate_women)




