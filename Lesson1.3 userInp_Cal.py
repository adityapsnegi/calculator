def Add(X,Y):
    return X + Y
def Subtract(X,Y):
    return X - Y
def Multiply(X,Y):
    return X * Y
def Divide(X,Y):
    if Y == 0:
        return "Error! Division by zero."
    return X / Y

print("Select operation.")
print('1.Add')
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4):")
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter secound number:"))
        if choice == "1":
            print(num1, "+", num2, "=", Add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", Subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", Multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", Divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no):")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid Input")