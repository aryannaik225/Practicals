n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

choice = input("Enter your choice : \n+ \n- \n* \n/\n=> ")

if choice == '+':
    print(n1,"+",n2,"=",(n1+n2))
elif choice == '-':
    print(n1,"-",n2,"=",(n1-n2))
elif choice == '*':
    print(n1,"*",n2,"=",(n1*n2))
elif choice == '/':
    print(n1,"/",n2,"=",(n1/n2))
else:
    print("Enter Correct Input")