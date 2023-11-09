dict = {
        "12110":["Rami",25,"177cm"],
        "12120":["Bisi",23,"155cm"],
        "12130":["Bobi",24,"180cm"],
        }
print(dict)
for key, value in dict.items():
    print("Student ID:",key)
    print("Information:",value)
dict["12140"] = ["Alphonse",36,"182cm"]
print(dict)

del dict["12140"]
print(dict)
print(dict["12120"][2])

print()

classroom = {}
list = []
num_students = int(input("Please enter number of students:"))
num_attributes = int(input("Please enter number of attributes:"))

for i in range (num_students):
    attribute = input("Enter the attribute for the student:")     
    list.append(attribute)
print(list)



