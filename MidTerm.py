def showMenu(): #Function to display the menu at the beginning
    print("Hello User!\n")
    print("1-\tOpen Tab\n" + "2-\tClose Tab\n" + "3-\tSwitch Tab\n" + "4-\tDisplay All Tabs\n" + "5-\tOpen Nested Tab\n" + "6-\tClear All Tabs\n" + "7-\tSave Tabs\n" + "8-\tImport Tabs\n" + "9-\tExit\n")

def openTab(): #Function to display that a tab is opened
    open_tab = {}
    title = input("Enter the Title of the Website:\n")
    for i in title:
        if title[0].islower():
            title1 = title[0].upper() + title[1:]
    url = input("Enter the URL of the website:\n")
    open_tab["Title"] = [title] #to add to the dict the "key" title with its value which is from the user input
    open_tab["URL"] = [url] #to add to the dict the "key" URL with its value which is also from the user input
    print("\n",title1,"Tab Opened")
    #if we print the dictionary it will be like: {'Title': ['google'], 'URL': ['www.google.com']} 
    
    


def main():
    showMenu()
    choice = eval(input("Select from the above:\t"))#User input
    while choice != 7: 
        if choice == 1:
            openTab()
            
        
    
main()
