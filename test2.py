tuple1 = (1,8,5,10,9)
tuple2 = 1,3,5,6,88
print(type(tuple1))
print(type(tuple2))
lst = ["rami",2,(1,3,4,5)]
print(lst[2])

print(tuple1[2])
print(sorted(tuple1))
print(tuple1)


set1 = {4,"Bisi",10,24}
print(set1)

dict = {
    0: ["Hello", "world"],
    1: "whats up",
    2: 56,
    3: "whats up",
    4: (8, 7, 6)
}

for i, j in dict.items():
    print("The key is:",i)
    print("The value is:",j)
