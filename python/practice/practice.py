# # # # # #check whether the given string is palindrome or not
# # # # # # string=input("Enter the string:")
# # # # # # if(string==string[::-1]):
# # # # # #       print("The string is a palindrome")
# # # # # # else:
# # # # # #         print("Not a palindrome")
# # # # #  ############################################################
# # # # # # string = input("Enter the string:")
# # # # # # if string.reverse == string:
# # # # # #       print("The string is a palindrome")
# # # # # # else:
# # # # # #       print("Not a palindrome")
# # # # # # for i in range(4):
# # # # # #     for j in range(4):
# # # # # #         print("#" , end="")
# # # # # #     print()

# # # # # # num=int(input("Enter the number:"))
# # # # # # factorial=1
# # # # # # if num<0:
# # # # # #     print("does not exist")
# # # # # # elif num==0:
# # # # # #     print("1")
# # # # # # else:
# # # # # #     for i in range(1,num+1):
# # # # # #         factorial=factorial*i
# # # # # # #     print(factorial)
# # # # # # print(~(1010010))
# # # # # # print(~(-64675))
# # # # # # print(~(-123))
# # # # # # a=0b1010
# # # # # # b=0b1100
# # # # # # print(bin(a&b))
# # # # # # print(bin(a|b))
# # # # # # print(bin(a^b))
# # # # # # print(bin(~a))
# # # # # # print(bin(a<<2))
# # # # # # print(bin(a>>2))
# # # # # # print(int("0777888119"))

# # # # # # print(num2)
# # # # # a=int(input("Enter the number:"))
# # # # # b=int(input("Enter the number:"))
# # # # # c=int(input("Enter the number:"))
# # # # # if a==b and a==c:
# # # # #     print ("all are equal")
# # # # # elif a==b or a==c or b==c:
# # # # #     print("two are equal")
# # # # # else:
# # # # #     if(a>b and a>c):
# # # # #         print("a is greater")
# # # # #     else:
# # # # #         if(b>a and b>c):
# # # # #             print("b is greater")
# # # # #         else:
# # # # #             print("c is greater")

# # # # # message="welcomtomycore"
# # # # # message.split()
# # # # # print(message)

# # # # # python-v       ##1
# # # # # print(ord('a')) #2
# # # # # n=int(input("Enter the number:"))#4
# # # # # print(n+n)

# # # # # principal=int(input("Enter the principal amount:"))           ##5
# # # # # rate=float(input("Enter the rate of interest:"))
# # # # # time=int(input("Enter the time:"))#2
# # # # # simple_interest=(principal*rate*time)/100
# # # # # print("The simple interest is:",simple_interest)
# # # # # radius=float(input("Enter the radius of the circle:"))        ##6
# # # # # area=3.14*radius*radius
# # # # # print("The area of the circle is:",area)
# # # # # a=int(input("Enter the number:"))                             ##8
# # # # # print(a.reverse())
# # # # # n=int(input("Enter the number:"))                             ##7
# # # # # print(n+n*n+n*n*n)
# # # # # n=int(input("Enter the number:"))                             ##10
# # # # # sum=n[0]+n[-1]
# # # # # print(sum)

# # # # # x=20
# # # # # def test():
# # # # #     x=30
# # # # #     print(x)
# # # # # test()
# # # # # print(x)
# # # # # x=20
# # # # # def test():
# # # # #     global x
# # # # #     #x=30
# # # # #     print(x)
# # # # # test()
# # # # # print(x)
# # # # # b=10
# # # # # x=20
# # # # # print(id(x))
# # # # # def test():
# # # # #     x=30
# # # # #     a= globals()
# # # # #     print(x,  id(x))
# # # # #     print(a)
# # # # # test()
# # # # # print(x)


# # # # # a=("A","B","C","g")
# # # # # b=("D","E","F")
# # # # # x=zip(a,b)
# # # # # print(tuple(x))

# # # # # dict1={"brand":"A"
# # # # # ,"model":"B"
# # # # # ,"year":2018
# # # # # ,"year":2019}
# # # # # print(dict1)
# # # # # print(dict1["brand"])

# # # # # key=['A','B','C']
# # # # # value=[1,2,3]
# # # # # key_value=zip(key,value)
# # # # # d=dict(key_value)
# # # # # # print(d)
# # # # # import string
# # # # # text="hello. how are you?"

# # # # # print(text.capitalize())
# # # # # print(text.endswith("you",15,18))

# # # # # text="how are you and where are you going london,delhi, lucknow?"
# # # # # # print(text.split(','))
# # # # # text="One person is sitting. One is standing"
# # # # # print(text.replace("sitting","standing"))
# # # # # print(text.replace("One","Two",3))

# # # # #!/bin/python3

# # # # import math
# # # # import os
# # # # import random
# # # # import re
# # # # import sys

# # # # #
# # # # # Complete the 'maxMin' function below.
# # # # #
# # # # # The function is expected to return an INTEGER.
# # # # # The function accepts following parameters:
# # # # #  1. INTEGER k
# # # # #  2. INTEGER_ARRAY arr
# # # # #

# # # # # def maxMin(k, arr):
# # # # #     # Write your code here
# # # # #     arr.sort()
# # # # #     stack=[]
# # # # #     for i in range (k):
# # # # #         stack.append(i)
# # # # #     return max(stack)-min(stack)
    

# # # # # def linear_search(arr,k):
# # # # #     for i in range(len(arr)):
# # # # #         if arr[i]==k:
# # # # #             print("Found and location",i)
# # # # #             return
# # # # #     print("Not Found")

# # # # # linear_search([1,2,3,4,5,6,7,8,9],7)

# # # # # def linear_search(arr,k):     # if multiple times key repeat in the array then print all the indexes
# # # # #     for i in range(len(arr)):
# # # # #         if arr[i]==k:
# # # # #             print("Found and location",i)
# # # # #     return
# # # # # print("Not Found")

# # # # # linear_search([1,2,3,2,4,5,2,5,44,3,2,22,2,2,2,54,66,43],222)

    



# # # # # #1.Find maximum of three numbers
# # # # # a=int(input("Enter the number:"))
# # # # # b=int(input("Enter the number:"))
# # # # # c=int(input("Enter the number:"))
# # # # # print("a is greater" if a>b and a>c else "b is greater" if b>c else "c is greater")


# # # # # #2.Check whether a number is prime.
# # # # # a=int(input("Enter the number:"))
# # # # # if a>1:
# # # # #     for i in range(2,a):
# # # # #         if a%i==0:
# # # # #             print("Not a prime number")
# # # # #             break
# # # # #     else:
# # # # #         print("Prime number")

# # # # # # 3.Check whether a number is Armstrong
# # # # # num=int(input("Enter the number:"))
# # # # # sum=0
# # # # # temp=num
# # # # # while temp>0:
# # # # #     digit=temp%10
# # # # #     sum+=digit**3
# # # # #     temp//=10
# # # # # if num==sum:
# # # # #     print("Armstrong number")
# # # # # else:
# # # # #     print("Not an armstrong number")

# # # # # #4. Find all primes between a given range
# # # # # lower=int(input("Enter the lower range:"))
# # # # # upper=int(input("Enter the upper range:"))
# # # # # for num in range(lower,upper+1):
# # # # #     if num>1:
# # # # #         for i in range(2,num):
# # # # #             if num%i==0:
# # # # #                 break
# # # # #         else:
# # # # #             print(num)

# # # # # # 5. Write a Python program that accepts a word from the user and reverse it.
# # # # # word=input("Enter the word:")
# # # # # print(word[::-1])
# # # # # # 6. Write a Python program to count the number of even and odd numbers from a series of numbers
# # # # # lower=int(input("Enter the lower range:"))
# # # # # upper=int(input("Enter the upper range:"))
# # # # # even=0
# # # # # odd=0
# # # # # for num in range(lower,upper+1):
# # # # #     if num%2==0:
# # # # #         even+=1
# # # # #     else:
# # # # #         odd+=1
# # # # # print("Even numbers:",even "\nOdd numbers:",odd)
# # # # # # 7. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# # # # # # Note : Use 'continue' statement.
# # # # # for i in range(0,7):
# # # # #     if i==3 or i==6:
# # # # #         continue
# # # # #     print(i)

# # # # # # 8. Write a Python program to get the Fibonacci series between 0 to 50
# # # # # a=0
# # # # # b=1
# # # # # while a<50:
# # # # #     print(a)
# # # # #     a,b=b,a+b

# # # # # # 9. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# # # # # for i in range(1,51):
# # # # #     if i%3==0 and i%5==0:
# # # # #         print("FizzBuzz")
# # # # #     elif i%3==0:
# # # # #         print("Fizz")
# # # # #     elif i%5==0:
# # # # #         print("Buzz")
# # # # #     else:
# # # # #         print(i)
# # # # # # 10. Write a Python program to check whether an alphabet is a vowel or consonant
# # # # # char=input("Enter the character:")
# # # # # char.lower()
# # # # # if char in ('a','e','i','o','u'):
# # # # #     print("Vowel")
# # # # # else:
# # # # #     print("Consonant")
# # # # # # 11. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
# # # # # sum=0
# # # # # count=0
# # # # # while True:
# # # # #     num=int(input("Enter the number:"))
# # # # #     if num==0:
# # # # #         break
# # # # #     sum+=num
# # # # #     count+=1
# # # # # print("Sum:",sum)
# # # # # print("Average:",sum/count)
# # # # # # 12. Write a Python program to create the multiplication table (from 1 to 10) of a number.
# # # # # num=int(input("Enter the number:"))
# # # # # for i in range(1,11):
# # # # #     print(num,"*",i,"=",num*i)

# # # # # # 13. Write a program to sum seven terms of given series.
# # # # # #1/1!+2/2!+3/3!+.....
# # # # # # [Hint: use Math.factorial(x) by import math]
# # # # # import math
# # # # # sum=0
# # # # # for i in range(1,8):
# # # # #     sum+=i/math.factorial(i)
# # # # # print(sum)
# # # # # # 14. When interest compounds q times per year at an annual rate of r % for n years, the principle p compounds to an amount a as per the following formula a = p ( 1 + r / q )**q
# # # # # # Write a program to read 10 sets of p, r, n & q and calculate the corresponding as.
# # # # # for i in range(10):
# # # # #     p=int(input("Enter the principle:"))
# # # # #     r=int(input("Enter the rate:"))
# # # # #     n=int(input("Enter the year:"))
# # # # #     q=int(input("Enter the number of times interest compounds:"))
# # # # #     a=p*(1+r/q)**(q*n)
# # # # #     print("Amount:",a)

# # # # # # 15. The policy followed by a company to process customer orders is given by the following rules:
# # # # # # a. (a) If a customer order is less than or equal to that in stock and has credit is OK, supply has requirement.
# # # # # # b. (b) If has credit is not OK do not supply. Send him intimation.
# # # # # # c. (c) If has credit is Ok but the item in stock is less than has order, supply what is in stock. Intimate to him data the balance will be shipped.
# # # # # # Write a  program to implement the company policy.
# # # # # order=int(input("Enter the order:"))
# # # # # stock=int(input("Enter the stock:"))
# # # # # credit=input("Enter the credit:")
# # # # # if order<=stock and credit=="OK":
# # # # #     print("Supply has requirement")
# # # # # elif credit!="OK":
# # # # #     print("Do not supply. Send him intimation")
# # # # # else:
# # # # #     print("Supply what is in stock. Intimate to him data the balance will be shipped")


# # # # # # 16. A university has the following rules for a student to qualify for a degree with A as the
# # # # # # main subject and B as the subsidiary subject:
# # # # # # a. (a) He should get 55 percent or more in A and 45 percent or more in B.
# # # # # # b. (b) If he gets than 55 percent in A he should get 55 percent or more in B.
# # # # # # However, he should get at least 45 percent in A.
# # # # # # c. (c) If he gets less than 45 percent in B and 65 percent or more in A he is allowed
# # # # # # to reappear in an examination in B to qualify.
# # # # # # d. (d) In all other cases he is declared to have failed.
# # # # # # Write a program to receive marks in A and B and Output whether the student has
# # # # # # passed, failed or is allowed to reappear in B.

# # # # # marks_A=int(input("Enter the marks in A:"))
# # # # # marks_B=int(input("Enter the marks in B:"))
# # # # # if marks_A>=55 and marks_B>=45:
# # # # #     print("Passed")
# # # # # elif marks_A>=55 and marks_B>=45:
# # # # #     print("Passed")
# # # # # elif marks_A>=65 and marks_B<45:
# # # # #     print("Allowed to reappear in B")
# # # # # else:
# # # # #     print("Failed")

# # # # # # 17. An Insurance company follows following rules to calculate premium.
# # # # # # a. (1) If a person’s health is excellent and the person is between 25 and 35 years of age and lives in a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.
# # # # # # b. (2) If a person satisfies all the above conditions except that the sex is female then the premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
# # # # # # c. (3) If a person’s health is poor and the person is between 25 and 35 years of age and lives in a village and is a male cannot exceed Rs. 10,000.
# # # # # # d. (4) In all other cases the person is not insured.
# # # # # # Write a program to output whether the person should be insured or not, his/her premium rate and maximum amount for which he/she can be insured.
# # # # # health=input("Enter the health:")
# # # # # age=int(input("Enter the age:"))
# # # # # location=input("Enter the location:")

# # # # #binary search time complexity O(log n) 
# # # # class Solution:
# # # #     def bin_search(self, nums: List[int], target: int) -> int:
# # # #         low,high=0,len(nums)-1
# # # #         while low<=high:
# # # #             mid=(low+high)//2
# # # #             if nums[mid]==target:
# # # #                 return mid
# # # #             elif nums[mid]<target:
# # # #                 low=mid+1
# # # #             else:
# # # #                 high=mid-1
# # # #         return -1
    


# # # # #if the target is present in the list then return the index of the target else return the index where taget can be placed

# # # # class Solution:
# # # #     def bin_search(self, nums: List[int], target: int) -> int:
# # # #         if target in nums:
# # # #             return nums.index(target)
# # # #         else:
# # # #             nums.append(target)
# # # #             nums.sort()
# # # #             return nums.index(target)
        
# # # # class Solution:
# # # #     def bin_search(self, nums: List[int], target: int) -> int:
# # # #         low,high=0,len(nums)-1
# # # #         while low<=high:
# # # #             mid=(low+high)//2
# # # #             if nums[mid]==target:
# # # #                 return mid
# # # #             elif nums[mid]<target:
# # # #                 low=mid+1
# # # #             else:
# # # #                 high=mid-1
# # # #         return low
    
# # # # # 1413. Minimum Value to Get Positive Step by Step Sum
# # # # # Easy
# # # # # Topics
# # # # # Companies
# # # # # Hint
# # # # # Given an array of integers nums, you start with an initial positive value startValue.

# # # # # In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# # # # # Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 
# # # #  PSeudocode:
# # # # # Initialize startValue to 1
# # # # # Iterate over the array
# # # # # For each element, calculate the step by step sum
# # # # # If the step by step sum is less than 1, update startValue to be the step
# # # # # by step sum plus 1

# # # # class Solution:
# # # #     def minStartValue(self, nums: List[int]) -> int:
# # # #         startValue=1
# # # #         for i in range(len(nums)):
# # # #             startValue+=nums[i]
# # # #             if startValue<1:
# # # #                 startValue=1
# # # #         return startValue
    


# # # # algorith
# # # # find lowest and greatest element in the array
# # # # if low>0
# # # # then return 1
# # # # else return top +[high-low]


# # # # class Solution:
# # # #     def minStartValue(self, nums: List[int]) -> int:
# # # #         low=min(nums)
# # # #         high=max(nums)
# # # #         if low>0:
# # # #             return 1
# # # #         else:
# # # #             return 1-high+abs(low)
        
# # # # class solution:
# # # #     def minStartValue(self, nums: List[int]) -> int:
# # # #         Sum, ans = 0, 0
# # # #         for i in len(nums):
# # # #             Sum = Sum + el
# # # #             ans = min(ans, Sum)
# # # #         return -ans + 1
        

# # # # # 744. Find Smallest Letter Greater Than Target
# # # # class Solution:
# # # #     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
# # # #         smallest=letters[0]
# # # #         for i in range(len(letters)):
# # # #             if letters[i]>target:
# # # #                 return letters[i]
# # # #         return smallest

# # # # using priority  queue

# # # # class Solution:
# # # #     def nextGreatestLetter(self, letters: List[str], target: str) -> str:




# # # # using binary search

# # # # class Solution:
# # # #     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        









# # # #lambda

# # # # x=lambda a:a+2
# # # # print(x(5))


# # # # explain lambda
# # # # lambda is a small anonymous function
# # # # lambda can take any number of arguments but can only have one expression
# # # # lambda is used to create small anonymous functions at runtime
# # # # lambda is used to pass a function as an argument to higher-order functions
# # # # lambda is used to return the function


# # # #syntax
# # # # lambda arguments:expression

# # # #example
# # # # x=lambda a:a+10
# # # # print(x(5))

# # # # x=lambda a,b:a*b
# # # # print(x(5,6))
# # # # output 30

# # # # x=lambda a,b,c:a+b+c
# # # # print(x(5,6,7))
# # # # output 18

# # # # def myfunc(n):
# # # #     return lambda a:a*n
# # # # mydoubler=myfunc(2)
# # # # print(mydoubler(11))
# # # # output 22

# # # # 10 use of lambda
# # # # lambda is used to pass a function as an argument to higher-order functions
# # # # lambda is used to return the function
# # # # lambda is used to create small anonymous functions at runtime
# # # # lambda is used to filter data
# # # # lambda is used to map data
# # # # lambda is used to reduce data
# # # # lambda is used to sort data
# # # # lambda is used to groupby data
# # # #lambda is used to create a dictionary from a list of tuples
# # # # # lambda is used to create a list of tuples from dictionary








# # # # s=['1','2','3','4']
# # # # res=map(int,s)
# # # # print(list(res))

# # # # output
# # # # <map object at 0x000002433866BE80>

# # # # what does the map function do in python?
# # # # The map() function applies a given function to each item of an iterable (such as a list, tuple, or string) and returns a map object.
# # # # The map() function takes two arguments: a function(spoon) and an iterable(plate). It applies the function to each item of the iterable and returns a map object.
# # # # The map object is an iterator, so you can convert it to a list or iterate over it using a for loop.
# # # # The map() function is a built-in function in Python, so you don't need to import it.

# # # # # a=[1,2,3,4,5]
# # # # # b=list (map(lambda x: x*3,a))
# # # # # print(b)

# # # # # name=['ABC','DEF','GHI']
# # # # # r=map(str.lower,name)
# # # # # print(list(r))

# # # # def fun(**a):
# # # #     print(a['fname'])

# # # # fun(fname='ABC',lname='DEF')




# # # #!/bin/python3

# # # import math
# # # import os
# # # import random
# # # import re
# # # import sys

# # # #
# # # # Complete the 'cookies' function below.
# # # #
# # # # The function is expected to return an INTEGER.
# # # # The function accepts following parameters:
# # # #  1. INTEGER k
# # # #  2. INTEGER_ARRAY A
# # # #

# # # def cookies(k, A):
# # #     # Write your code here
# # #     A.sort()
# # #     count = 0
# # #     while len(A) < k:
# # #         if len(A) == 0:
# # #             return -1
# # #         max_val = A[-1]
# # #         min_val = A[0]
# # #         if min_val == 0:
# # #             return -1
# # #         avg = (max_val + min_val) / 2
# # #         A[0] = math.ceil(avg - min_val)
# # #         A[-1] = math.ceil(avg - min_val)
# # #         A.sort()
# # #         count += 1
# # #         return count
    

# # # #     STDIN               Function
# # # # -----               --------
# # # # 6 7                 A[] size n = 6, k = 7
# # # # 1 2 3 9 10 12       A = [1, 2, 3, 9, 10, 12]  

# # # if __name__ == '__main__':
# # #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# # #     first_multiple_input = input().rstrip().split()

# # #     n = int(first_multiple_input[0])

# # #     k = int(first_multiple_input[1])

# # #     A = list(map(int, input().rstrip().split()))

# # #     result = cookies(k, A)

# # #     fptr.write(str(result) + '\n')

# # #     fptr.close()



# # # example
# # # 6 7
# # # 1 2 3 9 10 12

# # # output
# # # 2



# # #!/bin/python3

# # import math
# # import os
# # import random
# # import re
# # import sys

# # #
# # # Complete the 'pangrams' function below.
# # #
# # # The function is expected to return a STRING.
# # # The function accepts STRING s as parameter.
# # #

# # def pangrams(s):
# #     # Write your code here
# #     alphabet = "abcdefghijklmnopqrstuvwxyz"
# #     for char in alphabet:
# #         if char not in s.lower():
# #             return "not pangram"
# #         return "pangarm"
    
# # def pangrams(s):
# #     alphabet= "abcdefghijklmnopqrstuvwxyz"
# #     s=s.lower()
# #     set(s)
# #     if len (s)==len(alphabet):
# #         return "pangram"
# #     else: 
# #         return "not pangram"


# # uisng set
# # def pangrams(s):
# #     alphabet = "abcdefghijklmnopqrstuvwxyz"
# #     return len(set(alphabet) - set(s.lower())) == 0

    

# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# #     s = input()

# #     result = pangrams(s)

# #     fptr.write(result + '\n')

# #     fptr.close()

# # #print the content of the text file "C:\Users\lalkr\OneDrive\Desktop\Doc3.txt"
# # f=open("C:/Users/lalkr/OneDrive/Desktop/Doc3.txt","r+")
# # print(f.read())
# # print(f.readline())
# # print(f.readlines())
# # print(f.write("hello i am laxmi narayan"))
# # print(f.truncate())
# # print(f.seek(0))
# # print(f.flush())
# # print(f.read())

# # print(f.readline(5))
# # print(f.close())







# # f1=open("c:/Users/lalkr/OneDrive/Desktop/IMG-20241120-WA0018[1].jpg","r")
# # f2=open("c:/Users/lalkr/OneDrive/Desktop/IMG-20241120-WA0018[1].jpg","w")
# # print(f1.read())
# # print(f2.write("hello i am laxmi narayan"))





























# # opening mode in file handling
# # r: read mode : it will open the file in read mode. It will not create the file if it does not exist.
# # It will return an error if the file does not exist.

# # w: write mode: it will open the file in write mode. It will create the file if it does not exist.
# # It will overwrite the file if it already exists.

# # a: append mode: it will open the file in append mode. It will create the file if it does not exist.
# # It will append the file if it already exists.

# # r+: read and write mode: it will open the file in read and write mode
# # . It will not create the file if it does not exist.

# # w+: write and read mode: it will open the file in write and read mode.
# # It will create the file if it does not exist.
# # It will overwrite the file if it already exists.

# # a+: append and read mode: it will open the file in append and read mode.
# # It will create the file if it does not exist.
# # It will append the file if it already exists.

















# # problem


# # Yet Another GCD Problem
# # Chef was trying to solve a famous problem, counting co-prime pairs, for his friend. The problem is straightforward:
# # Given an array 
# # A
# # A of size 
# # N
# # N, find the total number of pairs of indices 
# # (
# # i
# # ,
# # j
# # )
# # (i,j) such that 
# # A
# # i
# # A 
# # i
# # ​
# #   and 
# # A
# # j
# # A 
# # j
# # ​
# #   are co-prime i.e., 
# # gcd
# # ⁡
# # (
# # A
# # i
# # ,
# # A
# # j
# # )
# # =
# # 1
# # gcd(A 
# # i
# # ​
# #  ,A 
# # j
# # ​
# #  )=1.

# # Being too busy with his delicious recipes, Chef didn't have enough time to solve the problem. So, instead of actually solving it, he guessed the answer and gave it to his friend. Since he already told the answer to his friend, he can't take his words back, but he can change the array to make it correspond to the answer he gave.

# # Chef needs your help to construct an array 
# # A
# # A of size 
# # N
# # N, containing only elements between 
# # 2
# # 2 and 
# # 2
# # ×
# # 1
# # 0
# # 6
# # 2×10 
# # 6
# #  , such that the number of co-prime pairs in it is exactly 
# # K
# # K.

# # Input Format
# # The first line of input will contain a single integer 
# # T
# # T, denoting the number of test cases.
# # Each test case consists of a single line containing two space-separated integers 
# # N
# # N and 
# # K
# # K — the size of the required array and the number of co-prime pairs in it.
# # Output Format
# # For each test case, output on a new line, 
# # N
# # N space-separated integers denoting the elements of array 
# # A
# # A you constructed.

# # If no such array exists, print the single integer 
# # −
# # 1
# # −1.

# # Constraints
# # 1
# # ≤
# # T
# # ≤
# # 10
# # 1≤T≤10
# # 1
# # ≤
# # N
# # ≤
# # 1
# # 0
# # 5
# # 1≤N≤10 
# # 5
 
# # 2
# # ≤
# # A
# # i
# # ≤
# # 2
# # ×
# # 1
# # 0
# # 6
# # 2≤A 
# # i
# # ​
# #  ≤2×10 
# # 6
# #   for each 
# # 1
# # ≤
# # i
# # ≤
# # N
# # 1≤i≤N
# # 1
# # ≤
# # K
# # ≤
# # 1
# # 0
# # 9
# # 1≤K≤10 
# # 9
 
# # Sum of 
# # N
# # N over all testcases is 
# # ≤
# # 1
# # 0
# # 5
# # ≤10 
# # 5
 
# # Sample 1:
# # Input
# # Output
# # 4
# # 5 10
# # 4 13
# # 2 1
# # 6 7
# # 6 19 85 77 3887
# # -1
# # 2 3
# # 5 2 2 7 10 50 
# # Explanation:
# # In first case each number is co-prime with others so total number of co-prime pairs are 
# # 10
# # 10.
# # In second case it's not possible to create an array with given 
# # N
# # N and 
# # K
# # K.
# # In third case seven pairs of indices 
# # {
# # (
# # 1
# # ,
# # 2
# # )
# # ,
# # (
# # 1
# # ,
# # 3
# # )
# # ,
# # (
# # 1
# # ,
# # 4
# # )
# # ,
# # (
# # 2
# # ,
# # 4
# # )
# # ,
# # (
# # 3
# # ,
# # 4
# # )
# # ,
# # (
# # 4
# # ,
# # 5
# # )
# # ,
# # (
# # 4
# # ,
# # 6
# # )
# # }
# # {(1,2),(1,3),(1,4),(2,4),(3,4),(4,5),(4,6)} contain co-prime pairs of elements.



# #input
# # 4
# # 5 10
# # 4 13
# # 2 1
# # 6 7

# #output
# # 6 19 85 77 3887
# # -1
# # 2 3
# # 5 2 2 7 10 50 



# # code 

# # for _ in range(int(input())):
# #     n = int(input())
# #     a = list(map(int, input().split()))
# #     b = list(map(int, input().split()))
# #     c = set()
# #     for i in range(n):
# #         for j in range(n):
# #             if math.gcd(a[i], b[j]) == 1:
# #                 c.add((a[i], b[j]))
# #     print(*[x[1] for x in c])


# # tertiary operator for finding max betwen 3 umber
# # # a,b,c=map(int,input().split())
# # # print(max(a,b,c))
# # using tertiary operator
# # # a,b,c=map(int,input().split())
# # (())



# # # debug this given code
# # def equalStacks(h1, h2, h3):
# #     # Write your code here 
# #     s1,s2,s3= sum(h1),sum(h2),sum(h3)
# #     if h1==h2==h3==0:
# #         return 0
# #     while s1==s2==s3:
# #         if (s1>=s2)and (s1>=s3):
# #             s1-=h1.pop(0)
# #         elif (s2>=s1)and (s2>=s3):
# #             s2-=h2.pop(0)
# #         else:
# #             s3-=h3.pop(0)
# #     return s1


# # # write the correct code
# # def equalStacks(h1, h2, h3):
# #     # Write your code here
# #     s1,s2,s3=sum(h1),sum(h2),sum(h3)
# #     if h1==h2==h3==[]:
# #         return 0
# #     while s1!=s2 or s1!=s3 or s2!=s3:
# #         if (s1>=s2)and (s1>=s3):
# #             s1-=h1.pop(0)
# #         elif (s2>=s1)and (s2>=s3):
# #             s2-=h2.pop(0)
# #         else:
# #             s3-=h3.pop(0)
# #     return s1





















# # 374. Guess Number Higher or Lower
# # Easy
# # Topics
# # Companies
# # We are playing the Guess Game. The game is as follows:

# # I pick a number from 1 to n. You have to guess which number I picked.

# # Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# # You call a pre-defined API int guess(int num), which returns three possible results:

# # -1: Your guess is higher than the number I picked (i.e. num > pick).
# # 1: Your guess is lower than the number I picked (i.e. num < pick).
# # 0: your guess is equal to the number I picked (i.e. num == pick).
# # Return the number that I picked.

 

# # Example 1:

# # Input: n = 10, pick = 6
# # Output: 6
# # Example 2:

# # Input: n = 1, pick = 1
# # Output: 1
# # Example 3:

# # Input: n = 2, pick = 1
# # Output: 1
 

# # Constraints:

# # 1 <= n <= 231 - 1
# # 1 <= pick <= n

# # The guess API is already defined for you.
# # @param num, your guess
# # @return -1 if num is higher than the picked number
# #          1 if num is lower than the picked number
# #          otherwise return 0
# # # def guess(num: int) -> int:

# # class Solution:
# #     def guessNumber(self, n: int) -> int:
# #         left, right = 1, n
# #         while left <= right:
# #             mid = (left + right) // 2
# #             result = guess(mid)
# #             if result == 0:
# #                 return mid
# #             elif result == -1:
# #                 right = mid - 1
# #             else:
# #                 left = mid + 1
# #         return -1
    

# # # 2nd differnt approach 

# # class Solution:
# #     def guessNumber(self, n: int) -> int:
# #         for i in range(1, n+1):
# #             if guess(i) == 0:
# #                 return i
# # #         return -1
    

# # 278. First Bad Version
# # Easy
# # Topics
# # Companies
# # You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# # Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# # You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# # Example 1:

# # Input: n = 5, bad = 4
# # Output: 4
# # Explanation:
# # call isBadVersion(3) -> false
# # call isBadVersion(5) -> true
# # call isBadVersion(4) -> true
# # Then 4 is the first bad version.
# # Example 2:

# # Input: n = 1, bad = 1
# # Output: 1
 

# # Constraints:

# # 1 <= bad <= n <= 231 - 1


# # The isBadVersion API is already defined for you.
# # def isBadVersion(version: int) -> bool:

# # class Solution:
# #     def firstBadVersion(self, n: int) -> int:
# #         left, right = 1, n
# #         while left < right:
# #             mid = left + (right - left) // 2
# #             if isBadVersion(mid):
# #                 right = mid
# #             else:
# #                 left = mid + 1
# #         return left
    






# # 852. Peak Index in a Mountain Array
# # Medium
# # Topics
# # Companies
# # You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# # Return the index of the peak element.

# # Your task is to solve it in O(log(n)) time complexity.

 

# # Example 1:

# # Input: arr = [0,1,0]

# # Output: 1

# # Example 2:

# # Input: arr = [0,2,1,0]

# # Output: 1

# # Example 3:

# # Input: arr = [0,10,5,2]

# # Output: 1

 

# # Constraints:

# # 3 <= arr.length <= 105
# # 0 <= arr[i] <= 106
# # arr is guaranteed to be a mountain array.


# # explain the above problem
# # The problem is asking to find the index of the peak element in a mountain array.
# #  A mountain array is an array where the values increase to a peak element and then decrease
# #  The problem requires a solution with a time complexity of O(log(n)) which means we need to use binary search to solve the problem.
# #  The problem constraints are that the array length is between 3 and 10^5, the values in the array are between 0 and 10^6, and the array is guaranteed to be a 
# # mountain array. The problem is asking to find the index of the peak element in the array.
# #  The problem can be solved using binary search, we start by finding the middle element of the array and then check if the element is greater than the next element
# #  and the previous element, if it is then we return the index of the element, if it is not then we check if the element is greater than the next element and if it is
# #  then we search in the right half of the array, if it is not then we search in the left half of the array.


# # aproach
# # 1. start by finding the middle element of the array
# # 2. check if the middle element is greater than the next element and the previous element , if it is then return the index of the middle element
# # 3. if it is then return the index of the middle element
# # 4. if the middle element is not greater than the next element and the previous element then check if the middle element is greater than the next element
# # 5. if it is then search in the right half of the array, if it is not then search in the left half of the array
# # 6. repeat the process until the peak element is found



# # class Solution:
# #     def peakIndexInMountainArray(self, arr: List[int]) -> int:
# #         mid = len(arr) // 2
# #         if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
# #             return mid
# #         elif arr[mid] > arr[mid - 1]:
# #             return self.peakIndexInMountainArray(arr[mid + 1:])
# #         else:
# #             return self.peakIndexInMountainArray(arr[:mid])
        


# # calculate no of uppercase and lowercase in string using function in given string [ Hello I Am Laxmi Narayan]

# # def count_upper_lower(s):
# #     upper = 0
# #     lower = 0
# #     for char in s:
# #         if char.isupper():
# #             upper += 1
# #         elif char.islower():
# #             lower += 1
# #             return upper, lower





# # # assignmnet 3

# # # 1. Write a program that accepts a sentence and calculates the number of letters and digits.
# # def count_letters_digits(sentence):
# #     letters = sum(c.isalpha() for c in sentence)
# #     digits = sum(c.isdigit() for c in sentence)
# #     return f"LETTERS {letters}\nDIGITS {digits}"

# # # Sample Input
# # sentence = "hello world! 123"
# # print(count_letters_digits(sentence))  # Expected Output: LETTERS 10, DIGITS 3

# # # 2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# # # If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# # def add_ing(string):
# #     if len(string) < 3:
# #         return string
# #     if string.endswith('ing'):
# #         return string + 'ly'
# #     return string + 'ing'

# # # Sample Inputs
# # print(add_ing("abc"))  # Expected Output: 'abcing'
# # print(add_ing("string"))  # Expected Output: 'stringly'

# # # 3. Write a Python function that takes a list of words and returns the length of the longest one.
# # def longest_word_length(words):
# #     return max(len(word) for word in words)

# # # Sample Input
# # words = ["apple", "banana", "cherry"]
# # print(longest_word_length(words))  # Expected Output: 6

# # # 4. Write a Python program to check if a string contains all letters of the alphabet.
# # def contains_all_alphabet(string):
# #     alphabet = set('abcdefghijklmnopqrstuvwxyz')
# #     return alphabet <= set(string.lower())

# # # Sample Input
# # string = "The quick brown fox jumps over the lazy dog"
# # print(contains_all_alphabet(string))  # Expected Output: True

# # # 5. Write a Python program to count the number of characters (character frequency) in a string.
# # from collections import Counter

# # def char_frequency(string):
# #     return dict(Counter(string))

# # # Sample Input
# # string = "hello world"
# # print(char_frequency(string))

# # # 6. Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# # # If the string length is less than 2, return instead of the empty string.
# # def first_last_2_chars(string):
# #     if len(string) < 2:
# #         return ''
# #     return string[:2] + string[-2:]

# # # Sample Input
# # string = "hello"
# # print(first_last_2_chars(string))  # Expected Output: 'helo'

# # # 7. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# # def replace_char(string):
# #     if not string:
# #         return string
# #     first_char = string[0]
# #     return first_char + string[1:].replace(first_char, '$')

# # # Sample Input
# # string = "restart"
# # print(replace_char(string))  # Expected Output: 'resta$t'

# # # 8. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# # def swap_first_two_chars(s1, s2):
# #     if len(s1) < 2 or len(s2) < 2:
# #         return s1 + ' ' + s2
# #     return s2[:2] + s1[2:] + ' ' + s1[:2] + s2[2:]

# # # Sample Input
# # s1, s2 = "abc", "xyz"
# # print(swap_first_two_chars(s1, s2))  # Expected Output: 'xyc abz'

# # # 9. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# # def replace_not_poor(string):
# #     not_index = string.find('not')
# #     poor_index = string.find('poor')
# #     if not_index < poor_index and not_index != -1 and poor_index != -1:
# #         return string[:not_index] + 'good' + string[poor_index + 4:]
# #     return string

# # # Sample Input
# # string = "The movie is not that poor!"
# # print(replace_not_poor(string))  # Expected Output: 'The movie is good!'

# # # 10. Write a Python program to remove the nth index character from a nonempty string.
# # def remove_nth_char(string, n):
# #     return string[:n] + string[n+1:]

# # # Sample Input
# # string = "hello"
# # n = 2
# # print(remove_nth_char(string, n))  # Expected Output: 'helo'

# # # 11. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
# # def exchange_first_last(string):
# #     if len(string) < 2:
# #         return string
# #     return string[-1] + string[1:-1] + string[0]

# # # Sample Input
# # string = "hello"
# # print(exchange_first_last(string))  # Expected Output: 'oellh'

# # # 12. Write a Python program to remove the characters which have odd index values of a given string.
# # def remove_odd_index_chars(string):
# #     return ''.join([char for index, char in enumerate(string) if index % 2 == 0])

# # # Sample Input
# # string = "hello"
# # print(remove_odd_index_chars(string))  # Expected Output: 'hlo'

# # # 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# # def display_upper_lower():
# #     user_input = input("Enter a string: ")
# #     print("Upper case:", user_input.upper())
# #     print("Lower case:", user_input.lower())

# # # Note: Uncomment the following lines to run the function
# # # display_upper_lower()

# # # 14. Write a Python program that accepts a comma-separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# # def sort_unique_words():
# #     words = input("Enter words: ").split(',')
# #     unique_words = sorted(set(words))
# #     print(','.join(unique_words))

# # # Note: Uncomment the following lines to run the function
# # #  sort_unique_words()

# # # 15. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# # def four_copies_last_two(string):
# #     if len(string) < 2:
# #         return ''
# #     return string[-2:] * 4

# # # Sample Input
# # string = "hello"
# # print(four_copies_last_two(string))  # Expected Output: 'lolololo'

# # # 16. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
# # def convert_to_upper_if_cond(string):
# #     if sum(1 for char in string[:4] if char.isupper()) >= 2:
# #         return string.upper()
# #     return string

# # # Sample Input
# # string = "HeLLo"
# # print(convert_to_upper_if_cond(string))  # Expected Output: 'HELLO'

# # # 17. Write a Python program to sort a string lexicographically.
# # def lexicographic_sort(string):
# #     return ''.join(sorted(string))

# # # Sample Input
# # string = "hello"
# # print(lexicographic_sort(string))  # Expected Output: 'ehllo'

# # # 18. Write a Python program to remove a newline in Python.
# # def remove_newline(string):
# #     return string.replace('\n', '')

# # # Sample Input
# # string = "hello\nworld\n"
# # print(remove_newline(string))  # Expected Output: 'helloworld'



# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         #USE HASH MAP 
# #         hashmap = {}
# #         for i in range(len(nums)):
# #             if target - nums[i] in hashmap:
# #                 return [hashmap[target - nums[i]], i]
# #             hashmap[nums[i]] = i
# #         return [-1,-1]




# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         #using two pointer
# #         left, right = 0, len(nums) - 1
# #         while left < right:
# #             if nums[left] + nums[right] == target:
# #                 return [left, right]
# #             elif nums[left] + nums[right] < target:
# #                 left += 1
# #             else:
# #                 right -= 1
# #         return [-1, -1]


# # class Solution:
# #     def findPeakElement(self, nums: List[int]) -> int:
# #         #brute force
# #         for i in range(1, len(nums) - 1):
# #             if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
# #                 return i
# #         return 0



# # class Solution:
# #     def findPeakElement(self, nums: List[int]) -> int:
# #         #using binary search
# #         left, right = 0, len(nums) - 1
# #         while left < right:
# #             mid = (left + right) // 2
# #             if nums[mid] > nums[mid + 1]:
# #                 right = mid
# #             else:
# #                 left = mid + 1
# #         return left
        



# # def reverse(llist):
# #     # Write your code here for reverse a singly linked list 
# #     # using stack
# #     stack = []
# #     while llist:
# #         stack.append(llist.val)
# #         llist = llist.next
# #     head = ListNode(stack.pop())
# #     current = head
# #     while stack:
# #         current.next = ListNode(stack.pop())
# #         current = current.next
# #     return head


# #write a program to copy the content of file 1 to file 2



# # Open file1 in read mode and file2 in write mode
# with open('c:/Users/lalkr/OneDrive/Desktop/Doc3.txt', 'r') as file1:
#     with open('C:/Users/lalkr/OneDrive/Desktop/New folder/coding/file2.txt', 'w') as file2:
#         print("Content of file1:")
#         content = file1.read() 
#         print(content)
#         file2.write(content) 
#         print(file2.seek(8))  #to move cursor
#         print(file2.tell()) #current position of cursor
#         print("########################################################################################")
# with open('C:/Users/lalkr/OneDrive/Desktop/New folder/coding/file2.txt', 'r') as file:
#     print(file.read())


# #add a code to print he location /path of the file
# import os
# print(os.path.abspath('C:/Users/lalkr/OneDrive/Desktop/New folder/coding/file2.txt'))
# print(os.path.dirname('C:/Users/lalkr/OneDrive/Desktop/New folder/coding/file2.txt'))
# print(os.path.basename('C:/Users/lalkr/OneDrive/Desktop/New folder/coding/file2.txt'))
# print(os.path.join('C:/Users/lalkr/OneDrive/Desktop/New folder/coding/file2.txt','C:/Users/lalkr/OneDrive/Desktop/New folder/coding/file2.txt'))



# Problem Statement
# One day, Mary wanted to give a present to her friend. She decided on a beautiful bouquet of flowers and began collecting them. She needed precisely 2 types of flowers, and the total number of flowers required was 't'. To gather these, she started picking from her garden, which contained 'N' types of flowers. Each type was arranged in a queue in non-decreasing order, such as 1, 3, 6, 15, and so forth.

# Now, she seeks your help in determining the indexes of the flowers she should collect.

# Note: For every case, there will always be a pair of flowers whose sum equals 't'. If multiple pairs exist, select the first occurrence.

# Input Format
# The first line contains integers N and t where, N is the total types of flowers and t is the total number of flowers needed.

# The second line contains n integers a1,a2,…,an — elements of the a array.

# Output Format
# Print the indexes of the two flowers that sum up to 't'. The first index should be smaller than the second index. Both indexes should be zero-based.

# Constraints
# 2 <= N <= 10^4

# 1 <= a[i] <= 10^3

# 2 <= t <= 2*10^3

# Sample Testcase 0
# Testcase Input
# 5 2
# 1 1 2 3 4
# Testcase Output
# 0 1
# Explanation
# Flowers at 0th and 1st indexes sum up to the target only i.e. 1 + 1 = 2.

# Sample Testcase 1
# Testcase Input
# 7 5
# 1 2 2 4 5 7 10
# Testcase Output
# 0 3
# Explanation
# Flowers at 0th and 3rd indexes sum up to the target only i.e. 1 + 4 = 5 .


def find_flower_indices(n, t, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Total types of flowers
        t (int): Total number of flowers needed
        arr (list): List of integers representing types of flowers
    Returns:
        tuple: A tuple with two integers representing the indices of the two flowers
    """
    # write code for function of above problem  
    # Create a dictionary to store the elements of the array as keys and their corresponding indices as values
    flower_dict = {}
    for i, flower in enumerate(arr):
        if flower not in flower_dict:
            flower_dict[flower] = [i]
            else:
    flower_dict[flower].append(i)
    # Iterate over the dictionary to find two flowers that sum up to 't'
    for flower1 in flower_dict:
        for flower2 in flower_dict:
            if flower1 + flower2 == t:
                return (flower_dict[flower1][0], flower_dict[flower2][0])
            return (-1, -1)  # Return (-1, -1) if no such
        # If no such flowers are found, return (-1, -1)
        return (-1, -1)  # Return (-1, -1) if no such
    # Test the function with the provided test cases
    

    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    t = int(data[1])  # Second input is the integer t
    arr = list(map(int, data[2:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = find_flower_indices(n, t, arr)
    
    # Print the output in the required format
    print(result[0], result[1])

if __name__ == "__main__":
    main()