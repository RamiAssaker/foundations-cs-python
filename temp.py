#def calculateSum(num):
# if num == 1:
#   return 1
# result = num + calculateSum(num - 1)
#   return result

#def main():
#   number = eval(input("Enter a number to sum from 1 to N:"))
#   print("The sum from 1 to",number,"is:",calculateSum(number))
    
#main()

#def calculateFactorial(num):
#    if num == 0 or num == 1:
#        return 1
#    result = num * calculateFactorial(num - 1)
#    return result

#def main():
#    number = int(input("Please enter a number to calculate the factorial from 1 to N:"))
#    print(number,"factorial is:",calculateFactorial(number))
#    
#main()

#list = [10,23,17,5,7,155]
#sorted_list = list.sort()

#list = [[1,2,3],[1],[4,5,6]]
#print(list[0][1],list[2][0])

classroom=[]
num_students = int(input("Enter the number of students: "))
num_features = int(input("Enter the number of features of the studnets: "))
for row in range(num_students):
  print("Student", row)

  classroom.append([])
  # Empty list to represent a student, we will fill this list in the nested for loop below.
  for col in range(num_features):
    print("Feature number:", col)
    feature = input("Enter feature of student: ")
    classroom[row].append(feature)

print("Your classroom is:", classroom)
