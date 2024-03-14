""" Lab#08 / Christian Gower / 3.23.2023 """

def factorial(n):
    if n == 1:
        print(n,"! is",n)
        return n
    else:
        print(n,"*", n-1,"!")
        r =  factorial(n-1)

        print(n,"! is",n * r)
        return n * r



num = int(input("Enter a number: "))
result =factorial(num)

"""print("The factorial of",num,"is",factorial(num))"""
'''
print(num, end="")
for i in range(num-1,0,-1):
    print("*",i,"!",end="")
print("1 ! is", factorial(num))

for i in range(i, num+1):
    print(i,"! is", factorial(i))

'''

