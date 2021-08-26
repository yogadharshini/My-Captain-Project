print("Enter a list of elements")
l1=[int(x) for x in input().split()]
print("Positive numbers in a list are:",end='')
for i in l1:
    if(i>=0):
        print(i,end=' ')
