print("Program to find the prime numbers in a give range")
l=int(input("Enter the number"))
u=int(input("Enter the number"))
for number in range(l,u+1):
        if number>1:
            for i in range(2,number):
                if(number%i)==0:
                    break
            else:
              print(number)
