print("Select an operation to perform")
print("1.ADD")
print("2. SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation=input()

if operation=="1":
    num1=input("input first digit::")
    num2=input("input second digit:")
    print(" TOTAL " + str((int(num1)+int(num2))))
elif operation=="2":
    num1=input("input first digit:")
    num2=input("input second digit:")
    print(" TOTAL " + str((int(num1)-int(num2))))
elif operation=="3":
    num1=input("input first digit:")
    num2=input("input second digit:")
    print(" TOTAL " + str((int(num1)*int(num2))))
elif operation=="4":
    num1=input("input first digit:")
    num2=input("input second digit:")
    print(" TOTAL " + str((int(num1)/int(num2))))
else:
    print("invalid input")