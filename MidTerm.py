def showMenu(): #Function to display the menu at the beginning
    print("Hello User!\n")
    print("1-\tOpen Tab\n" + "2-\tClose Tab\n" + "3-\tSwitch Tab\n" + "4-\tDisplay All Tabs\n" + "5-\tOpen Nested Tab\n" + "6-\tClear All Tabs\n" + "7-\tSave Tabs\n" + "8-\tImport Tabs\n" + "9-\tExit\n")

def openTab():
    open_tab = {}
    title = input("Enter the Title:\n")
    url = input("Enter the URL of the website:\n")
    open_tab["Title"] = [title]
    open_tab["URL"] = [url]
    print("\n",title,"Tab Opened")
    
    


def main():
    showMenu()
    choice = eval(input("Select from the above:\t"))#User input
    while choice != 7: 
        if choice == 1:
            openTab()
            
        
    
main()
