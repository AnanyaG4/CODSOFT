#Python program for a calculator 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("1) is addition\n2) is subtraction\n 3) is multiplication\n4) is division\n5)is modulus")
choice= int(input("Enter your choice: "))
if choice==1:
    print("The sum of the two numbers is ", a+b)
elif choice==2:
    print("The difference between the two numbers is ",abs(a-b))
elif choice==3:
    print("The product of the two number is ",a*b)
elif choice==4:
    print("The quotient if the two numbers are divided is ",a//b)
elif choice==5:
    print("The remainder if the two numbers are divided is ",a%b)    
else:
    print("Enter a valid choice")
    
