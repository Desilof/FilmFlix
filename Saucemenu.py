from sauce import *
from readSauce import readSauce
from amendSauce import amendSauce
from addSauce import addSauce
from deleteSauce import deleteSauce

def menu():
    choice = 0
    while choice not in ["1","2","3","4","5"]:
        print(
            "Film Menu \nEnter:\n1) Print\n2) Add\n3) Update\n4) Delete\n5) Exit"
        )
    
        choice = input("Enter one of the options above: ")

        if choice not in ["1","2","3","4","5"]:
            print(f"{choice} is invalid")
    
    return choice

mainProgram = True
while mainProgram:
    mainmenu = menu()
    if mainmenu == "1":
        readSauce()
    if mainmenu == "2":
        addSauce()
    if mainmenu == "3":
        amendSauce()
    if mainmenu == "4":
        deleteSauce()
    else:
        mainProgram = False

input("Press enter to Exit")