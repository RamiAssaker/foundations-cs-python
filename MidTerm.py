import requests #used for the "switch tab" case;install requests library on PC 
import json#used to have access and be able to read json files

def showMenu(): #Function to display the menu at the beginning
    print("1-\tOpen Tab\n" + "2-\tClose Tab\n" + "3-\tSwitch Tab\n" + "4-\tDisplay All Tabs\n" + "5-\tOpen Nested Tab\n" + "6-\tClear All Tabs\n" + "7-\tSave Tabs\n" + "8-\tImport Tabs\n" + "9-\tExit\n")

def openTab(open_dict): #Function to display that a tab is opened
    title = input("Enter the Title of the Website:\n")
    for i in title: #O(N)
        if title[0].islower():
            title1 = title[0].upper() + title[1:] #changing the first letter to capital incase it was lower case
    url = input("Enter the URL of the Website of the form 'https://website.com' :\n")
    url_string = 'https://'
    if url[0:8] != url_string:#Checking if the user input has "https://
        print("Please use the format 'https://'")
        openTab(open_dict)#Incase no "https://" format, then call the openTab function to start all over again until a correct user input is inserted
    else:
        open_dict[title] = [url] #add to the dict the "key" title with its value which is from the user input
        print("\n",title1,"tab opened\n")
        return open_dict
    #if we print the dictionary: {'google': ['google.com']} 

def closeTab(open_dict):
    close = input("Which tab would you like to close:\n")
    tabs_delete = [] #we need a list to insert the key we want to delete since we cannot delete from dictionary during iteration(error:dictionary changed size during iteration ) 
    for i in open_dict:#O(N)
        if close == i:
            tabs_delete.append(i) #append what is in index i to the list "tabs_delete"
        else:
          tabs_delete.append(list(open_dict.keys())[-1]) #transforming the dictionary into a list and appending to the list "tabs_delete" the last index of the dictionary
    for j in tabs_delete: #iterating through the list-O(N)
        if j in open_dict: #double verification of what must be deleted, (if it is in the dictionary -->delete)
            del open_dict[j]
        #else:
         #   print("No webpage found. Please insert an opened tab\n")
    print(open_dict)
    #O(N) is the final bigOnotation
    
def switchTab(open_dict):
    switch = input("Which tab do you want to display its content:")
    for key in open_dict:#O(N)
        if switch == key:
            url = open_dict[key][0]
            response = requests.get(url)#a GET request to get the url (syntax used to send HTTP requests)
            open_dict[key] = response.text #Adding the HTML to the dictionary in order to use when using "savetab"
        else:
            url = open_dict[key][-1]
            response = requests.get(url)
            open_dict[key] = response.text #Adding the HTML to the dictionary in order to use when using "savetab"
    if response.status_code == 200: #This condition (==200) ensures that a condition is OK or satisfied(Just like the "404" states for ERROR!)
        print(response.text,"\n")
    
def displayAll(open_dict):
    for key in open_dict.items():#O(N)
        print("Tabs opened:\n",key[0])

def clearTabs(open_dict):
    clear_tab = []#we need a list to insert the key we want to delete since we cannot delete from dictionary during iteration(error:dictionary changed size during iteration )
    for i in open_dict:#O(N)
        clear_tab.append(i)#append what is in index i to the list "clear_tab"
    for j in clear_tab:#O(N)
        if j in open_dict:
            del open_dict[j]
    print("All tabs cleared")
    #Concerning this feature, we can create a while loop incase after pressing "6" and after clearing all tabs, if the user presses "6" again, it will display that there are no tabs to clear
    #final Big O = O(N)

def saveTabs(open_dict):
    file_path = input("Enter file path of format '/<path>/<path>.json':")
    with open(file_path,'w') as json_file:#"with" statement ensures that the file is closed after operation
    #open a file specified in the file path('w' indicates the parameter to be in write mode)
    #This file is opened as JSON file in order to interact with the file
        json.dump(open_dict, json_file)
        #"json.dump" helps write the dictionary content to the "json_file"
    #Reference: university exercises
    
def importTabs():
    path_of_file = input("Enter file path: ")
    file = open(path_of_file)#Reference: medium.com; use open function to open a file
    content = file.read()#Read the content of the file
    print("Tabs content:\n",content)
    
def main():
    print("Hello User!\n")
    open_tab = {}
    choice = 0 
    while choice != 9:
        print("")
        showMenu()
        choice = eval(input("Select from the above:\t"))#User input
        if choice == 1:
            openTab(open_tab)
        elif choice == 2:
            closeTab(open_tab)
        elif choice == 3:
            switchTab(open_tab)
        elif choice ==4:
            displayAll(open_tab)
        elif choice == 6:
            clearTabs(open_tab)
        elif choice == 7:
            saveTabs(open_tab)
        elif choice == 8:
            importTabs()
        elif choice == 9:
            print("GoodBye !")

main()
