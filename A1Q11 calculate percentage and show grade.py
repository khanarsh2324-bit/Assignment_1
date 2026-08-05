n1=int(input("enter physics marks"))
n2=int(input("enter chemistry marks"))
n3=int(input("enter mathematics marks"))
n4=int(input("enter biology marks"))
n5=int(input("enter computer marks"))
percentage=int
percentage = (n1+n2+n3+n4+n5)/ 500 * 100
print(percentage)
if percentage >= 90:
    ptint("GRADE A")
else:
    if percentage>=80:
        print("GREDE B")
    else:
        if percentage>=70:
            print("GRADE C")
        else:
            if percentage>=60:
                print("GRADE D")
            else:
                if percentage >=50:
                    print("GRADE E")
                else:
                    if percentage < 50:
                        print("GRADE F")
                        


