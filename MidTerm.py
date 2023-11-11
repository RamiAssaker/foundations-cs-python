import requests #used for the "switch tab" case

def showMenu(): #Function to display the menu at the beginning
    print("1-\tOpen Tab\n" + "2-\tClose Tab\n" + "3-\tSwitch Tab\n" + "4-\tDisplay All Tabs\n" + "5-\tOpen Nested Tab\n" + "6-\tClear All Tabs\n" + "7-\tSave Tabs\n" + "8-\tImport Tabs\n" + "9-\tExit\n")

def openTab(open_dict): #Function to display that a tab is opened
    title = input("Enter the Title of the Website:\n")
    for i in title: #O(n)
        if title[0].islower():
            title1 = title[0].upper() + title[1:] #changing the first letter to capital incase it was lower case
    url = input("Enter the URL of the Website:\n")
    open_dict[title] = [url] #add to the dict the "key" title with its value which is from the user input
    print("\n",title1,"tab opened\n")
    return open_dict
    #if we print the dictionary: {'google': ['google.com']} 

def closeTab(open_dict):
    close = input("Which tab would you like to close:")
    tabs_delete = [] #we need a list to insert the key we want to delete since we cannot delete from dictionary during iteration(error:dictionary changed size during iteration ) 
    for i in open_dict:
        if close == i:
            tabs_delete.append(i) #append what is in index i to the list "tabs_delete"
        else:
          tabs_delete.append(list(open_dict.keys())[-1]) #transforming the dictionary into a list and appending to the list "tabs_delete" the last index of the dictionary
    for j in tabs_delete: #iterating through the list
        if j in open_dict: #double verification of what must be deleted, (if it is in the dictionary -->delete)
            del open_dict[j]
        else:
            print("No webpage found. Please insert an opened tab\n")
    print(open_dict)
    
def switchTab(open_dict):
    switch = input("Which tab do you want to switch to:")
    tab_switched = []
    for i in open_dict:
        if switch == i:
            for value in open_dict.items():
                response = requests.get(value)
                print(response)
            
    
def main():
    print("Hello User!\n")
    open_tab = {}
    #showMenu()
    #choice = eval(input("Select from the above:\t"))#User input
    choice = 0 
    order_of_tabs = []
    while choice != 9:
        showMenu()
        choice = eval(input("Select from the above:\t"))#User input
        if choice == 1:
            openTab(open_tab)
            order_of_tabs.append(1)
            print(open_tab) #THIS MUST BE COMMENTED
            #print(order_of_tabs) shows the list and numbers of tabs opened
        elif choice == 2:
            closeTab(open_tab)
        elif choice == 3:
            switchTab(open_tab)
        
            
            
            
        
    
main()
