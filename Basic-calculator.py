number =[]
for i in range(2):
    number.append(int(input(f"Enter number {i+1}: ")))
operation=input("Enter arithmetic operators such as '+','-','*', and '/': ")
if operation =='+':
    print(f"{number[0]}+{number[1]}={number[0]+number[1]}")
elif operation =='-':
        print(f"{number[0]}-{number[1]}={number[0]-number[1]}")
elif operation == '*':
    print(f"{number[0]}*{number[1]}={number[0]*number[1]}")
elif operation == '/':
    if(number[1]==0):
        print("Can't divide by zero")
    else:
        print(f"{number[0]}/{number[1]}={number[0]/number[1]}")
else:
    print("Invalid operator")
