print("Enter a list of elements")
a=[int(x) for x in input().split()]
print("Enter another list of elements")
b=[int(x) for x in input().split()]
c=set(a)
d=set(b)
print("Union:",c|d)
print("Intersection:",c&d)
print("Difference:",c-d)
print("Symmetric difference:",c^d)
