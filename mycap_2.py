n=int(input("Enter the number : "))
a,b=0,1
print(a,b,end=' ')
sum=0
for i in range(n-2):
    sum=a+b
    a=b
    b=sum
    print(sum,end=' ')
