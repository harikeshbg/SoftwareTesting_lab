a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
if(a<=0 or b<=0 or c<=0 or a>10 or b>10 or c>10 or a+b<c or b+c<a or a+c<b):
    print("Invalid input\n")
else:
    if(a==c and b==c):
        print("Equilateral triangle\n")
    elif((a==c and a!=b) or (b==c and b!=a) or (a==b and a!=c)):
        print("Isosceles triangle\n")
    else:
        print("Scalene triangle\n")
