print("A2.6")
n1 = int(input("Enter first number: "))           #takes input from user (only integer)
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))
if n1>n2 and n1>n3:                              #checks n1 is > than n2 and n3 
         print("Biggest number is:",n1)          #print , if yes, if no-->moves to the next condition
elif n2>n1 and n2>n3:                            #checks n2 is > than n1 and n3
    print("Biggest number is:",n2)               # prints , if yes, if no-->moves to the next condition
elif n3 > n1 and n3>n2:                          #checks n3 is > than n1 and n2
    print("Biggest number is:",n3)               # prints , if yes, if no-->moves to the next condition
