temp=int(input("Enter the temperature: "))
choice=input("type 1 for fahrenheit to centigrade and type 2 for centigrade to fahrenheit: ")
f = (9*temp + (32 * 5))/5
c = (5/9) * (temp - 32)
if choice == "1":
    print(str(temp)+"c")
elif choice == "2":
    print(str(temp)+"f")
else:
    print("Invalid Input")