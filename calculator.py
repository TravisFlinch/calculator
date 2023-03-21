print("select operation")
# a:add, b:subtract, c:multiply, d:divide
print("a for add")
print("b for subtraction")
print("c for multiplication")
print("d for division")

choice = input("Please enter choice(a,b,c,d):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if choice=="a":
    print(num1+num2)

elif choice=="b":
    print(num1-num2)

elif choice=="c":
    print(num1*num2)

elif choice=="d":
    print(num1/num2)

else:
    print("invalid choice")