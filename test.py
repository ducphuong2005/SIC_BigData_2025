c=float(input("Nhap vao nhiet độ C: "))
print(f"Nhiet do K la: ={c+273} độ K")
print("Độ K= {0}". format(c+273))

a=int(input("Nhap vao so a: "))
if a>0:
    print("a>0")
elif a==0:
        print("a=0")
else:
    print("a<0")

a=3
b=10
print (b//a)

m=int(input("Nhap vao so nguyen duong m: "))
n=int(input("Nhap vao so nguyen duong n: "))
if m>n:
    print(m//n)
    print(m%n)

bk= float(input("Nhap vao ban kinh hinh tron: "))
print("Dien tich hinh tron la: ", 3.14*bk*bk)
print(math.pow(bk,2))

for i in range(0):
    print(i)

a=  [5, "a", 10.5, True, [5]]
print(a[0])
print(a[4])

b= a[1:4]
print(b)

x= int(input("Nhap vao so x: "))
n= float(input("Nhap vao so n: "))
f=0
t=0
if n<20:
     for i in range(1,n+1):
         t+=i
         f+=(x-i)/t
     print(f)
else : 
    f= n**0.5 +x 
    print(f)

x= float(input("Nhap vao so x: "))
y= float(input("Nhap vao so y: "))
a= float(input("Nhap vao so a: "))
b= float(input("Nhap vao so b: "))
r= float(input("Nhap vao ban kinh r: "))
if (x-a)**2 + (y-b)**2 <= r**2:
    print("True")
else: 
    print("False")

def  Function(a, b):
    c= a+b
    d= a-b
    return c,d
c,d = Function(5, 6)

import numpy as np
a= [[1,2,3],
    [4,5,6]]
b= np.array(a)
print(b)

import numpy as np
a= [[1,2,3],
    [4,5,6]]
b= np.array(a)

