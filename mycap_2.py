n=int(input("Enter the number of elements to be printed : "))
a,b=0,1
print("The fibonacci numbers are:",end='')
print(a,b,end=' ')
sum=0
for i in range(n-2):
    sum=a+b
    a=b
    b=sum
    print(sum,end=' ')
