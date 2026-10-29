
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
operator = input("enter operator (+, -, *, /):")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")
