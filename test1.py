def displayMenu():
    choice =  int(input("Please choose from the following:\n"+"\t1- Add Matrices\n"+"\t2- Check Rotation\n" + "\t3- Invert Dictionary\n" + "\t4- Convert Matrix to Dictionary\n" + "\t5- Check Palindrome\n" + "\t6- Search for an Element & Merge Sort\n" + "\t7- Exit\n"))
    if choice > 7:
        print("Invalid input,\n" + "Please choose a number between 1 and 7")
    elif choice == 1:
        addMatrix()

def main():
    name = input("Please enter your name:")
    print("Welcome",name,"!\n")
    displayMenu()
 
def addMatrix(matrix1, matrix2):
    addition = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        addition.append(row)
    return addition

main()

