def showMenu(): #Function to display the menu at the beginning
    print("Hello User!\n")
    print("1-\tOpen Tab\n" + "2-\tClose Tab\n" + "3-\tSwitch Tab\n" + "4-\tDisplay All Tabs\n" + "5-\tOpen Nested Tab\n" + "6-\tClear All Tabs\n" + "7-\tSave Tabs\n" + "8-\tImport Tabs\n" + "9-\tExit\n")

def openTab(): #Function to display that a tab is opened
    open_tab = {}
    title = input("Enter the Title of the Website:\n")
    for i in title: 
        if title[0].islower():
            title1 = title[0].upper() + title[1:] #changing the first letter to capital incase it was lower case
    url = input("Enter the URL of the website:\n")
    open_tab[title] = [url] #to add to the dict the "key" title with its value which is from the user input
    print("\n",title1,"tab opened")
    print(open_tab)
    #if we print the dictionary it will be: {'Title': ['google', 'google.com']} 

#def closeTab():
#    close = int(input("Which tab would you like to close:"))
 #   if close == key in open_tab:
  #      del open_tab[key]
        

def main():
    showMenu()
    choice = eval(input("Select from the above:\t"))#User input
    order_of_tabs = []
    while choice != 7: 
        if choice == 1:
            openTab()
            order_of_tabs.append(1)
            #print(order_of_tabs) shows the list and numbers of tabs opened
            
       # elif choice == 2:
        #    closeTab()
            
            
        
    
main()
