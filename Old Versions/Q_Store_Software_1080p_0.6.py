# Finish by 13th of September

#Import addons to python language (WILL NOT WORK WITHOUT)
import customtkinter as ctk #Will need to install this via pip in comand prompt
from   tkinter import *
import csv
import os
import datetime
import glob
import re



#Function that contains the Program
def Q_Store_Software_06():

    #Defining variables to make it easier to change size of everything
    standardHeight= 50
    standardWidth= 250
    standardFont= "", 18
    standardYPadding= 10

    #Defining colour mode for the program (light or dark)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    #Setting program main window
    root = ctk.CTk()
    root.title("505ACU Albany Q-Store Software Version: 0.6")
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}")
    root.state('zoomed')
    
    #Defining the directory path
    path= os.getcwd()

    #Creating the frames the widgits sit in
    mainFrame = ctk.CTkFrame(root)
    mainFrame.pack(fill="both",expand=True)

    leftFrame = ctk.CTkFrame(mainFrame)
    leftFrame.pack(side='left', fill="both",expand=True)

    leftTopFrame = ctk.CTkFrame(leftFrame, fg_color= "#1f1f1f")
    leftTopFrame.pack(fill="both",expand=True)

    leftBottomFrame = ctk.CTkFrame(leftFrame, fg_color= "#292929")
    leftBottomFrame.pack(fill="both",expand=True)

    middleFrame = ctk.CTkFrame(mainFrame)
    middleFrame.pack(side='left', fill="both",expand=True)

    rightFrame = ctk.CTkFrame(mainFrame)
    rightFrame.pack(side='left', fill="both",expand=True)

    


    #Creating the function that contains options for AAC Members
    def AACMemberOptions():

        #Creating the function that allows users to add members to the list
        def addAACMemberOptions():

            #Adds person to the names list and adds the stores-out files for the member
            def addPerson():
                #Getting the entry from the entry boxes and turning them into string
                rank = str(rankEntry.get())
                first = str(first_inital.get())
                last_name = str(nameEntry.get())

                #Checks if the contain letters or numbers
                hasLettersRank = bool(re.search(r'[a-zA-Z]', rank))
                hasNumbersRank = bool(re.search(r'\d', rank))
                hasLettersFirst = bool(re.search(r'[a-zA-Z]', first))
                hasNumbersFirst = bool(re.search(r'\d', first))
                hasLetterslast_name = bool(re.search(r'[a-zA-Z]', last_name))
                hasNumberslast_name = bool(re.search(r'\d', last_name))

                #Checks if has no letters
                if not hasLettersRank:
                    #Creates error window
                    errorWindow= ctk.CTkToplevel(root)
                    errorWindow.title("Error Window")
                    errorWindow.geometry("1200x500")
                    errorWindow.transient(root)
                    errorWindow.lift()

                    #Creates label
                    errorLabel= ctk.CTkLabel(
                        errorWindow,
                        text= "Invalid Characters Entered For Abreviated Rank",
                        font= standardFont
                        )
                    errorLabel.pack(pady= standardYPadding)

                    #Creates button to close window
                    errorButton= ctk.CTkButton(
                        errorWindow,
                        text= "Close Window",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= errorWindow.destroy
                        )
                    errorButton.pack(pady= standardYPadding)

                    #Runs function
                    addAACMemberOptions()
                
                #Checking if has letters and numbers or just numbers
                elif hasLettersRank and hasNumbersRank or hasLettersRank:
                    
                    #Checks if only numbers
                    if hasNumbersFirst:
                        #Creates error window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "Invalid Characters Entered For First Initial",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates button to close window
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)

                        #Runs function
                        addAACMemberOptions()

                    #Checks if only has leters        
                    elif hasLettersFirst:

                        #Checks if only numbers
                        if hasNumberslast_name:
                            #Creates error window
                            errorWindow= ctk.CTkToplevel(root)
                            errorWindow.title("Error Window")
                            errorWindow.geometry("1200x500")
                            errorWindow.transient(root)
                            errorWindow.lift()

                            #Creates label
                            errorLabel= ctk.CTkLabel(
                                errorWindow,
                                text= "Invalid Characters Entered For Last Name",
                                font= standardFont
                                )
                            errorLabel.pack(pady= standardYPadding)

                            #Creates button to close window
                            errorButton= ctk.CTkButton(
                                errorWindow,
                                text= "Close Window",
                                font= standardFont,
                                width= standardWidth,
                                height= standardHeight,
                                command= errorWindow.destroy
                                )
                            errorButton.pack(pady= standardYPadding)

                            #Runs function
                            addAACMemberOptions()


                        #Checks if only has leters    
                        elif hasLetterslast_name:
                            with open(path+"/namesList.csv", 'a', newline= "") as namesListFile:
                                writer = csv.writer(namesListFile)
                                writer.writerow([rank, first+"."+last_name])

                                #Creating folder for person
                                newPersonFolder = r""+path+"/People_And_Logs/"+rank+"_"+first+"."+last_name
                                if not os.path.exists(newPersonFolder):
                                    os.makedirs(newPersonFolder)              
                                    
                                #Creating file for person
                                newShortTermLog= open(path+"/People_And_Logs/"+rank+"_"+first+"."+last_name+"/"+rank+"_"+first+"."+last_name+"_Short_Term_Log.csv", "w")
                                newShortTermLog.close()

                                #Creating file for new person
                                newLongTermLog= open(path+"/People_And_Logs/"+rank+"_"+first+"."+last_name+"/"+rank+"_"+first+"."+last_name+"_Long_Term_Log.csv", "w") 
                                newLongTermLog.close()
                            
                            #Runs function
                            addAACMemberOptions()

                        #Checks if contians stuff other than letters or numbers  
                        else:
                            #Creates error window
                            errorWindow= ctk.CTkToplevel(root)
                            errorWindow.title("Error Window")
                            errorWindow.geometry("1200x500")
                            errorWindow.transient(root)
                            errorWindow.lift()

                            #Creates label
                            errorLabel= ctk.CTkLabel(
                                errorWindow,
                                text= "Invalid Characters Entered For Last Name",
                                font= standardFont
                                )
                            errorLabel.pack(pady= standardYPadding)

                            #Creates button to close window
                            errorButton= ctk.CTkButton(
                                errorWindow,
                                text= "Close Window",
                                font= standardFont,
                                width= standardWidth,
                                height= standardHeight,
                                command= errorWindow.destroy
                                )
                            errorButton.pack(pady= standardYPadding)

                            #Runs function
                            addAACMemberOptions()


                    #Checks if contians stuff other than letters or numbers    
                    else:
                        #Creates error window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "Invalid Characters Entered For First Initial",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates button to close window
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)

                        #Runs function
                        addAACMemberOptions()

                #Checks if contians stuff other than letters or numbers   
                else:
                    #Creates error window
                    errorWindow= ctk.CTkToplevel(root)
                    errorWindow.title("Error Window")
                    errorWindow.geometry("1200x500")
                    errorWindow.transient(root)
                    errorWindow.lift()

                    #Creates label
                    errorLabel= ctk.CTkLabel(
                        errorWindow,
                        text= "Invalid Characters Entered For Abreviated Rank",
                        font= standardFont
                        )
                    errorLabel.pack(pady= standardYPadding)

                    #Creates button to close window
                    errorButton= ctk.CTkButton(
                        errorWindow,
                        text= "Close Window",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= errorWindow.destroy
                        )
                    errorButton.pack(pady= standardYPadding)

                    #Runs function
                    addAACMemberOptions()


            #Deletes all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Reads names file
            with open(path+"/namesList.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Creates list box and puts names into listbox
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standardFont)
            for row in contents:
                namesListListbox.insert(END, row)
            namesListListbox.pack(side=LEFT)

            #Creates scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            namesListListbox.config(yscrollcommand=listboxScrollbar.set)        

            #User entry
            rankEntry = ctk.CTkEntry(
                rightFrame, 
                placeholder_text="Enter Abreviated Rank",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                )
            rankEntry.pack(pady = standardYPadding)

            #User entry
            first_inital = ctk.CTkEntry(
                rightFrame, 
                placeholder_text="Enter first initial",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                )
            first_inital.pack(pady = standardYPadding)

            #User Entry
            nameEntry = ctk.CTkEntry(
                rightFrame, 
                placeholder_text="Enter Last Name",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                )
            nameEntry.pack(pady = standardYPadding)

            #Button to call 'addPerson' function
            addPersonButton = ctk.CTkButton(
                rightFrame,
                text= "Add An AAC Member\nTo The List",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= addPerson,
                )
            addPersonButton.pack(pady = standardYPadding)



        #Creating the function to remove members from the names list and delete there files
        def removeAACMemberOptions():

            #Defines function that checks if user is sure they want to delete person
            def AACMember():

                #Defines function that deletes member from list and there files
                def yes():
                    
                    #Deletes member from listbox
                    namesListListbox.delete(selection[0])

                    #Opens names file in wright mode and wrights updated names list to file
                    with open(path+"/namesList.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(namesListListbox.get(0, END))

                    #Deletes members files and folder
                    for filename in os.listdir(folder):
                        filePath = os.path.join(folder, filename)
                        if os.path.isfile(filePath):
                            os.remove(filePath)
                    os.rmdir(folder)

                    #Closes window  
                    areYouSureWindow.destroy()

                #Defines function to continue the program
                def no():
                    #Closes window
                    areYouSureWindow.destroy()

                #Gets userse selection
                selection = namesListListbox.curselection()

                #Gets members name and folder location
                AACMember= namesListListbox.get(selection)
                stringAACMember= str(AACMember)
                cleanStringAACMember= stringAACMember.replace("(", "").replace("'", "").replace(",", "").replace(" ", "_").replace(")", "")
                folder= path+"/People_And_Logs/"+cleanStringAACMember

                #Creates new window
                areYouSureWindow= ctk.CTkToplevel(root, fg_color= "#1f1f1f")
                areYouSureWindow.title("Are You Sure")
                areYouSureWindow.geometry("1200x500")
                areYouSureWindow.transient(root)
                areYouSureWindow.lift()
                
                #Creates label
                areYouSureLabel= ctk.CTkLabel(
                    areYouSureWindow,
                    text= f"Are You Sure You Want To Remove {cleanStringAACMember}\n\n This Will Permanently Remove All Information For This Person",
                    font= standardFont
                    )
                areYouSureLabel.pack(pady= standardYPadding)

                #Creates a frame
                buttonFrame= ctk.CTkFrame(areYouSureWindow, fg_color= "#1f1f1f")
                buttonFrame.pack()

                #Creates a buttonto call a function
                yesButton= ctk.CTkButton(
                    buttonFrame,
                    text= "Yes",
                    font= standardFont,
                    width= standardWidth,
                    height= standardHeight,
                    command= yes
                    )
                yesButton.pack(pady= standardYPadding, padx= 10, side='left')

                #Creates a buttonto call a function
                noButton= ctk.CTkButton(
                    buttonFrame,
                    text= "No",
                    font= standardFont,
                    width= standardWidth,
                    height= standardHeight,
                    command= no
                    )
                noButton.pack(pady= standardYPadding, padx= 10, side='left')

            #Checks if they select a person
            def selectionChecker():
                #Gets user selection
                rankNameSelection= namesListListbox.curselection()
                #Checks if there is not a selection
                if not rankNameSelection:
                    #Creates error widnow
                    errorWindow= ctk.CTkToplevel(root)
                    errorWindow.title("Error Window")
                    errorWindow.geometry("1200x500")
                    errorWindow.transient(root)
                    errorWindow.lift()
                    
                    #Creates a label
                    errorLabel= ctk.CTkLabel(
                        errorWindow,
                        text= "You have not selected a person, Please try again.",
                        font= standardFont
                        )
                    errorLabel.pack(pady= standardYPadding)

                    #Creates a button
                    errorButton= ctk.CTkButton(
                        errorWindow,
                        text= "Close Window",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= errorWindow.destroy
                        )
                    errorButton.pack(pady= standardYPadding)

                    #Runs if the user did select a name and calls a function
                else:
                    AACMember()

            #Deletes all widgits in the right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the person you wish to remove", font= standardFont)
            label.pack(pady = standardYPadding)

            #Opens names file in read mode
            with open(path+"/namesList.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Create frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Creates list box and fills it with members names
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standardFont)
            for row in contents:
                namesListListbox.insert(END, row)
            namesListListbox.pack(side=LEFT)

            #Creates scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            namesListListbox.config(yscrollcommand=listboxScrollbar.set)        

            #Creates button to call a function
            removeAACMemberButton = ctk.CTkButton(
                rightFrame,
                text= "Remove AAC Member From List",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= selectionChecker,
                )
            removeAACMemberButton.pack(pady = standardYPadding)



        #Defines function to change members rank
        def changeRankOptions():

            #Defines function to update members rank
            def updateRank():

                #Gets user selection
                rowSelectionRank = namesListListbox.curselection()

                #Checks if user selected an option
                if rowSelectionRank:
                    #Gets al required information and turns it into usable variables
                    rowIndexRank = rowSelectionRank[0]
                    rowRank = contentsRank[rowIndexRank]
                    rowIndexName = rowSelectionRank[0]
                    rowName = contentsRank[rowIndexName]
                    newRank = newRankEntry.get()
                    rank= rowRank[0]
                    name= rowName[1]
                    rowRank[0] = newRank

                    #Gets location of all files
                    currentFileNameLong= path+"/People_And_Logs/"+rank+"_"+name+"/"+rank+"_"+name+"_Long_Term_Log.csv"
                    currentFileNameShort= path+"/People_And_Logs/"+rank+"_"+name+"/"+rank+"_"+name+"_Short_Term_Log.csv"
                    currentFolderName= path+"/People_And_Logs/"+rank+"_"+name
                    newFileNameLong= path+"/People_And_Logs/"+rank+"_"+name+"/"+newRank+"_"+name+"_Long_Term_Log.csv"
                    newFileNameShort= path+"/People_And_Logs/"+rank+"_"+name+"/"+newRank+"_"+name+"_Short_Term_Log.csv"
                    newFolderName= path+"/People_And_Logs/"+newRank+"_"+name

                    #Renames files to updated rank
                    os.rename(currentFileNameLong, newFileNameLong)
                    os.rename(currentFileNameShort, newFileNameShort)
                    os.rename(currentFolderName, newFolderName)

                    #Opens names list in wright mode and wrights the new contents in
                    with open(path+"/namesList.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contentsRank)

                #Calls the function
                changeRankOptions()

            #Defining function to check if a user selected a person
            def selectionChecker():
                #Getting user listbox selection
                rankNameSelection= namesListListbox.curselection()
                #Looking if there was no selection
                if not rankNameSelection:
                    #Creating an error window
                    errorWindow= ctk.CTkToplevel(root)
                    errorWindow.title("Error Window")
                    errorWindow.geometry("1200x500")
                    errorWindow.transient(root)
                    errorWindow.lift()
                    
                    #Creating a label
                    errorLabel= ctk.CTkLabel(
                        errorWindow,
                        text= "You have not selected a person, Please try again.",
                        font= standardFont
                        )
                    errorLabel.pack(pady= standardYPadding)

                    #Creating a button
                    errorButton= ctk.CTkButton(
                        errorWindow,
                        text= "Close Window",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= errorWindow.destroy
                        )
                    errorButton.pack(pady= standardYPadding)
                #Looking if there was a selection
                else:
                    #Calling the function
                    updateRank()

            #Clea all widgets on right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Oppens names list file in read mode and read file
            with open(path+"/namesList.csv", 'r') as file:
                reader = csv.reader(file)
                contentsRank = [row for row in reader]

            #Creating a label
            label = ctk.CTkLabel(rightFrame, text="Select The Person You Wish To Modify", fg_color="transparent", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creating list box frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Creating list box and inserting contents of names list file into it
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 15, font= standardFont)
            for row in contentsRank:
                namesListListbox.insert(END, row)
            namesListListbox.pack(side=LEFT)

            #Creating a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            namesListListbox.config(yscrollcommand=listboxScrollbar.set)        

            #Creating an entry box
            newRankEntry = ctk.CTkEntry(
                rightFrame, 
                placeholder_text="Enter Abreviated Rank",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                )
            newRankEntry.pack(pady = standardYPadding)

            #Creating a button
            changeRankButton = ctk.CTkButton(
                rightFrame,
                text= "Update Rank",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= selectionChecker,
                )
            changeRankButton.pack(pady = standardYPadding)



        #Defining function to show list of AAC Members
        def listOfAACMembers():
            #Clearing all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens a names list in read mode and reads file
            with open(path+"/namesList.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates listbox frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = 50)

            #Creates listbox and inserts contents of names list file into the listbox
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
            for row in contents:
                namesListListbox.insert(END, row)
            namesListListbox.pack(side=LEFT)

            #Creates scrollbar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            namesListListbox.config(yscrollcommand=listboxScrollbar.set)


        #Clears widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates a button
        addPersonOptionsButton = ctk.CTkButton(
            middleFrame,
            text= "Add An AAC Member",
            font= (standardFont),
            width= standardWidth,
            height= standardHeight,
            command= addAACMemberOptions,
            )
        addPersonOptionsButton.pack(pady = standardYPadding)

        #Creats a button
        removePersonButton = ctk.CTkButton(
            middleFrame,
            text= "Remove An AAC Member",
            font= (standardFont),
            width= standardWidth,
            height= standardHeight,
            command=removeAACMemberOptions,
            )
        removePersonButton.pack(pady = standardYPadding)

        #Creates a button
        changeRankButton = ctk.CTkButton(
            middleFrame,
            text= "Change An AAC\nMembers Rank",
            font= (standardFont),
            width= standardWidth,
            height= standardHeight,
            command= changeRankOptions,
            )
        changeRankButton.pack(pady = standardYPadding)

        #Creates a button
        listPeopleButton = ctk.CTkButton(
            middleFrame,
            text= "List Of AAC Members",
            font= (standardFont),
            width= standardWidth,
            height= standardHeight,
            command= listOfAACMembers,
            )
        listPeopleButton.pack(pady = standardYPadding)




    #Defining function that shows list of all stores
    def listStores():

        #Defines function that allows user to view and update quantities of stores   
        def SlouchHatAndRelatedItemsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/Slouch_Hats_Puggarees_Chinstrap.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                SlouchHatAndRelatedItemsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/Slouch_Hats_Puggarees_Chinstrap.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)

        
        #Defines function that allows user to view and update quantities of stores   
        def JumpersAndRainjacketsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/Jumpers_and_Rainjackets.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                JumpersAndRainjacketsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/Jumpers_and_Rainjackets.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def PatchesAndRankslidesList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/Patches_and_Rankslides.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                PatchesAndRankslidesList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/Patches_and_Rankslides.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def OtherUniformList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/Other_Uniform.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                OtherUniformList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/Other_Uniform.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def UndershirtsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/Undershirts.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                UndershirtsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/Undershirts.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def BootsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/Boots.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                BootsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/Boots.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def AMCUBushHatList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/AMCU_Bush_Hats.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                AMCUBushHatList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/AMCU_Bush_Hats.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def AMCUShirtsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/AMCU_Shirts.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                AMCUShirtsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/AMCU_Shirts.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def AMCUPantsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/AMCU_Pants.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                AMCUPantsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/AMCU_Pants.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def DPCUBushHatList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/DPCU_Bush_Hats.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                DPCUBushHatList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/DPCU_Bush_Hats.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def DPCUShirtsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/DPCU_Shirts.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                DPCUShirtsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/DPCU_Shirts.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def DPCUPantsList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/DPCU_Pants.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                DPCUPantsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/DPCU_Pants.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Defines function that allows user to view and update quantities of stores   
        def EquipmentList():

            #Defining function to update stores
            def updateQuantity():

                #Gets lsit box selection
                rowSelection = storesListListbox.curselection()

                #Checks if there was a selection
                if rowSelection:
                    #Getting all information required
                    rowIndex = rowSelection[0]
                    row = contents[rowIndex]
                    newRank = newQuantityEntry.get()
                    row[0] = newRank

                    #Opens file in wright mode to update new quntity
                    with open(path+"/stores/Equipment.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(contents)

                #Call the function
                EquipmentList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Opens file in read mode and reads the file
            with open(path+"/stores/Equipment.csv", 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            for row in contents:
                storesListListbox.insert(END, row)
            storesListListbox.pack(side=LEFT)

            #Creates a scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a frame
            frameOne= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates an entry box
            newQuantityEntry = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter New Quantity",
                font= standardFont,
                width= 200,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 150,
                height= standardHeight,
                command= updateQuantity,
                )
            changeQuantityButton.pack(side= "right", padx = 10)


        #Clear all widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates a canvas
        canvas = ctk.CTkCanvas(middleFrame, bg= "#292929", highlightthickness=0)
        canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        #Creats scroll bar
        buttonScrollbar= ctk.CTkScrollbar(middleFrame, orientation=VERTICAL, command=canvas.yview)
        buttonScrollbar.pack(side="right", fill=Y)

        #Assigns scroll bar to the canvas
        canvas.configure(yscrollcommand=buttonScrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))

        #Creates a frame
        buttonFrame= ctk.CTkFrame(canvas, fg_color= "#292929")
        buttonFrame.pack(pady = standardYPadding)

        #Creats widnow within the canvas
        canvas.create_window((0,0), window=buttonFrame, anchor= "nw")

        #Creates a button
        SlouchHatAndRelatedItems = ctk.CTkButton(
            buttonFrame,
            text= "Slouch Hats & Related Items",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=SlouchHatAndRelatedItemsList,
            )
        SlouchHatAndRelatedItems.pack(pady = 5)

        #Creates a button
        JumpersAndRainjackets = ctk.CTkButton(
            buttonFrame,
            text= "Jumpers and Rainjackets",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=JumpersAndRainjacketsList,
            )
        JumpersAndRainjackets.pack(pady = 5)

        #Creates a button
        PatchesAndRankslides = ctk.CTkButton(
            buttonFrame,
            text= "Patches and Rankslides",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=PatchesAndRankslidesList,
            )
        PatchesAndRankslides.pack(pady = 5)

        #Creates a button
        OtherUniform = ctk.CTkButton(
            buttonFrame,
            text= "Other Uniform",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= OtherUniformList,
            )
        OtherUniform.pack(pady = 5)

        #Creates a button
        Undershirts = ctk.CTkButton(
            buttonFrame,
            text= "Undershirts",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= UndershirtsList,
            )
        Undershirts.pack(pady = 5)

        #Creates a button
        Boots = ctk.CTkButton(
            buttonFrame,
            text= "Boots",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=BootsList,
            )
        Boots.pack(pady = 5)

        #Creates a button
        AMCUBushHat = ctk.CTkButton(
            buttonFrame,
            text= "AMCU Bush Hats",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= AMCUBushHatList,
            )
        AMCUBushHat.pack(pady = 5)

        #Creates a button
        AMCUShirts = ctk.CTkButton(
            buttonFrame,
            text= "AMCU Shirts",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= AMCUShirtsList,
            )
        AMCUShirts.pack(pady = 5)

        #Creates a button
        AMCUPants = ctk.CTkButton(
            buttonFrame,
            text= "AMCU Pants",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=AMCUPantsList,
            )
        AMCUPants.pack(pady = 5)

        #Creates a button
        DPCUBushHat = ctk.CTkButton(
            buttonFrame,
            text= "DPCU Bush Hats",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= DPCUBushHatList,
            )
        DPCUBushHat.pack(pady = 5)

        #Creates a button
        DPCUShirts = ctk.CTkButton(
            buttonFrame,
            text= "DPCU Shirts",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=DPCUShirtsList,
            )
        DPCUShirts.pack(pady = 5)

        #Creates a button
        DPCUPants = ctk.CTkButton(
            buttonFrame,
            text= "DPCU Pants",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=DPCUPantsList,
            )
        DPCUPants.pack(pady = 5)

        #Creates a button
        Equipment = ctk.CTkButton(
            buttonFrame,
            text= "Equipment",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command=EquipmentList,
            )
        Equipment.pack(pady = 5)
        




    #Defining function to take stores out
    def orderingOptions():

        #Clear widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()


        #Defining function to make an order
        def ordering():


            #Defining function to add items to the order
            def addToOrder():
                #Gets list box selection
                selection = storesListListbox.curselection()

                #Make sure there is a selection
                if selection:
                    #Gets value that was selected in listbox, turns it into a string and cleans it up
                    itemListBox = storesListListbox.get(selection[0]) 
                    itemString = str(itemListBox)
                    item_sale = itemString.split(',')[1].strip().replace("'","").replace(")","")
                    qty_sale = "1" 
                        
                    #Find all CSV files in the folder
                    csv_folder = path+"/Stores"
                    csv_files = glob.glob(csv_folder + "/*.csv")

                    #Iterate through each CSV file
                    for csv_file in csv_files:
                        with open(csv_file, 'r') as file:
                            contents = csv.reader(file)
                            rows = list(contents)
                            #Iterate over each row in the CSV
                            for i, row in enumerate(rows):
                                #If it is less than 2 values it skips over it
                                if len(row) < 2:
                                    continue
                                #Checking if item selected is in the csv
                                if row[1] == item_sale:
                                    current_qty = int(row[0])
                                    #Checks if quantity required is higher than current quantity
                                    if current_qty < int(qty_sale):
                                        #Creates error window
                                        errorWindow= ctk.CTkToplevel(root)
                                        errorWindow.title("Error Window")
                                        errorWindow.geometry("1200x500")
                                        errorWindow.transient(root)
                                        errorWindow.lift()

                                        #Creates a label
                                        errorLabel= ctk.CTkLabel(
                                            errorWindow,
                                            text= "Not enough items in stock",
                                            font= standardFont
                                            )
                                        errorLabel.pack(pady= standardYPadding)

                                        #Creates a button
                                        errorButton= ctk.CTkButton(
                                            errorWindow,
                                            text= "Close Window",
                                            font= standardFont,
                                            width= standardWidth,
                                            height= standardHeight,
                                            command= errorWindow.destroy
                                            )
                                        errorButton.pack(pady= standardYPadding)
                                    #If quantity required is less/same than current quantity
                                    else:
                                        #Adds item to listbox
                                        ordersListbox.insert(END, f"{item_sale}")
                                        #Makes variable global
                                        global saveOrdersListbox
                                        #saving contents of the listbox
                                        saveOrdersListbox = ordersListbox.get(0, END)
                                        #subtracts 1 from the current quantity
                                        rows[i][0] = str(current_qty - 1)
                                        #Opens csv file in write mode and writes the new value into the file
                                        with open(csv_file, 'w', newline='') as outfile:
                                            writer = csv.writer(outfile)
                                            writer.writerows(rows)
                                        #Opens csv file in read mode and reads the file
                                        with open(csv_file, "r") as file:
                                            contents= csv.reader(file)
                                            #Clears all information in listbox
                                            storesListListbox.delete(0, END)
                                            #Inserts the new contents of the csv file into the listbox
                                            for row in contents:
                                                storesListListbox.insert(END, row)


                                        #Defines variable to disable buttons
                                        def disable_buttons_except_one(button_list):     
                                            #Disables all buttons in button list 
                                            for button in button_list:
                                                button.configure(state= DISABLED)


                                        #Defines variable to enable buttons
                                        def enable_all_buttons(button_list):
                                            #Enables all buttons in button list 
                                            for button in button_list:
                                                button.configure(state= NORMAL)


                                        #Defines variable to disable buttons
                                        def check_listbox_empty(listbox, button_list):
                                            #Checks if listbox has more than 0 items in it and calls the function
                                            if listbox.size() > 0:
                                                disable_buttons_except_one(button_list)
                                            #Checks if has 0 or less items in it and calls the function
                                            else:
                                                enable_all_buttons(button_list)
                                        
                                        #Creates button list and calls the variable
                                        button_list = [AACMemberOptionsButton,listOfStoresButton,orderingOptionsButton,storesReturnsButton,selectPersonOrderingButton,closeWindow]
                                        check_listbox_empty(ordersListbox, button_list)


            #Defines funtion to remove items from the order
            def removeFromOrder():
                
                #Gets celection from the listbox
                selection = ordersListbox.curselection()
                #If there is a selection it gets selected value in the listbox and turns it into a string
                if selection:
                    itemListBox = ordersListbox.get(selection[0])
                    itemString = str(itemListBox)
                    item_sale = itemString
                    qty_sale = "1"
                        
                    #Find all CSV files in the folder
                    csv_folder = path+"/Stores"
                    csv_files = glob.glob(csv_folder + "/*.csv")

                    #Iterate through each CSV file
                    for csv_file in csv_files:
                        with open(csv_file, 'r') as file:
                            contents = csv.reader(file)
                            rows = list(contents)
                            #Iterate over each row in the CSV
                            for i, row in enumerate(rows):
                                #If it has less than 2 values it skips over it
                                if len(row) < 2:
                                    continue
                                #Checking if item selected is in the csv
                                if row[1] == item_sale:
                                    current_qty = int(row[0])
                                    #Checks if quantity required is higher than current quantity
                                    if current_qty < int(qty_sale):
                                        #Creates error window
                                        errorWindow= ctk.CTkToplevel(root)
                                        errorWindow.title("Error Window")
                                        errorWindow.geometry("1200x500")
                                        errorWindow.transient(root)
                                        errorWindow.lift()

                                        #Creates a label
                                        errorLabel= ctk.CTkLabel(
                                            errorWindow,
                                            text= "Not enough items in stock",
                                            font= standardFont
                                            )
                                        errorLabel.pack(pady= standardYPadding)

                                        #Creates a button
                                        errorButton= ctk.CTkButton(
                                            errorWindow,
                                            text= "Close Window",
                                            font= standardFont,
                                            width= standardWidth,
                                            height= standardHeight,
                                            command= errorWindow.destroy
                                            )
                                        errorButton.pack(pady= standardYPadding)
                                    #If quantity required is less/same than current quantity
                                    else:
                                        #Deletes selected item from listbox
                                        ordersListbox.delete(selection[0])
                                        #Makes variable global
                                        global saveOrdersListbox
                                        #Gets item selected in listbox
                                        saveOrdersListbox = ordersListbox.get(0, END)
                                        #Adds 1 to current value
                                        rows[i][0] = str(current_qty + 1)
                                        #Opens csv file in write mode and writes new contents into the file 
                                        with open(csv_file, 'w', newline='') as outfile:
                                            writer = csv.writer(outfile)
                                            writer.writerows(rows)
                                        #Opens csv file in read mode and reads the file
                                        with open(csv_file, "r") as file:
                                            contents= csv.reader(file)

                                            #Deletes all contents in listbox and inserts contents of csv file into the now empty listbox
                                            storesListListbox.delete(0, END)
                                            for row in contents:
                                                storesListListbox.insert(END, row)
                                        
                                        #Defines variable to disable buttons
                                        def disable_buttons_except_one(button_list):     
                                            #Disables all buttons in button list 
                                            for button in button_list:
                                                button.configure(state= DISABLED)


                                        #Defines variable to enable buttons
                                        def enable_all_buttons(button_list):
                                            #Enables all buttons in button list 
                                            for button in button_list:
                                                button.configure(state= NORMAL)


                                        #Defines variable to disable buttons
                                        def check_listbox_empty(listbox, button_list):
                                            #Checks if listbox has more than 0 items in it and calls the function
                                            if listbox.size() > 0:
                                                disable_buttons_except_one(button_list)
                                            #Checks if has 0 or less items in it and calls the function
                                            else:
                                                enable_all_buttons(button_list)
                                        
                                        #Creates button list and calls the variable
                                        button_list = [AACMemberOptionsButton,listOfStoresButton,orderingOptionsButton,storesReturnsButton,selectPersonOrderingButton,closeWindow]
                                        check_listbox_empty(ordersListbox, button_list)


            #Defines the function that run when a checkbox is selected
            def shortTermCheckboxEvent():

                #Gets the date and time     
                currentDateTime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                #Setting a variable
                ordersListboxString = ""

                #Saves listbox to a variable
                for i in range(ordersListbox.size()):
                    ordersListboxString += str(ordersListbox.get(i)) + "\n"

                #Opens file in write mode and writes the orderslistboxstring to the file after replacing some punctuation    
                with open(path+"/organiseTwo.txt", "w") as organiseOne:
                    organiseOne.write(str(ordersListboxString.replace("'", "").replace(",", "").replace("(", "").replace(" ", "").replace(")", "")))
                #Saves file locations to variables
                input_file = path+"/organiseTwo.txt"
                output_file = path+"/organiseOne.txt"

                #Read the input file
                with open(input_file, 'r') as file:
                    content = file.read()

                #Write the updated content to the output file
                with open(output_file, 'w') as file:
                    file.write(content)

                #Sets an empty array
                wordCounts = {}

                #Opens a file in read mode and another in write mode
                with open(path+"/organiseOne.txt", "r") as organiseOne, open(path+"/organiseTwo.txt", "w") as organiseTwo:

                    #Iterating through lines in a file    
                    for line in organiseOne:
                        #Striping words and splitting words into collumns
                        words = line.strip().split("|")
                        #Iterates through all words in an array
                        for word in words:
                            #If word does not equal nothing
                            if word != '':
                                #Checks if word is in wordcounts, if it is it adds 1 to total
                                if word in wordCounts:
                                    wordCounts[word] += 1

                                #Adds word to word count    
                                else:
                                    wordCounts[word] = 1

                    #Writes array to text file
                    organiseTwo.write(str(wordCounts))

                #Opens a file in read mode and another in write mode and formats the contents
                with open(path+"/organiseTwo.txt", "r") as organiseTwo, open(path+"/organiseOne.txt", "w") as organiseOne:
                    itemsUprocessed= organiseTwo.read()
                    organiseOne.write(str(itemsUprocessed).replace("{", "").replace("'", "").replace(",", "\n").replace(":", "|").replace(" ", "").replace("}", ""))
                
                #Opens a file in read mode and another in write mode and splits contents into collumns
                with open(path+"/organiseOne.txt", "r") as organiseOne, open(path+"/organiseTwo.txt", "w") as organiseTwo:
                    for line in organiseOne:
                        collumns = line.strip().split("|")
                        collumnOne = collumns[0]
                        collumnTwo = collumns[1]   

                        #Creating new line format
                        newLine = currentDateTime + ", " + collumnTwo + ", " + collumnOne + "\n"

                        #Writing new line format to the file
                        organiseTwo.write(newLine)

                #Opens a file in read mode and another in write mode
                with open(path+"/organiseTwo.txt", "r") as organiseTwo, open(path+"/organiseOne.txt", "w") as organiseOne:
                    items= organiseTwo.read()
                    organiseOne.write(items)

                #Saving file locations to variables
                csv_file = path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Short_Term_Log.csv"
                txt_file = path+"/organiseOne.txt"

                #Sets empty lists
                column_one = []
                column_two = []
                column_three = []

                #Opens file in read mode and saves file to a list
                with open(txt_file, 'r') as file:
                    for line in file:
                        values = line.strip().split(',')
                        #Checks if amount of values in this list is equal to or greator than 2
                        if len(values) >= 2:
                            column_one.append(values[0])
                            column_two.append(values[1])
                            column_three.append(values[2])

                #Write to CSV file
                with open(csv_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(zip(column_one, column_two, column_three))
                
                #Deletes the files
                os.remove(f"{path}/organiseOne.txt")
                os.remove(f"{path}/organiseTwo.txt")

                #Clears all widgits in middle frame and right frame
                for widgets in middleFrame.winfo_children():
                    widgets.destroy()
                for widgets in rightFrame.winfo_children():
                    widgets.destroy()


            #Defines the function that run when a checkbox is selected                
            def longTermCheckboxEvent():

                #Gets the date and time                       
                currentDateTime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                
                #Setting a variable
                ordersListboxString = ""

                #Saves listbox to a variable
                for i in range(ordersListbox.size()):
                    ordersListboxString += str(ordersListbox.get(i)) + "\n"

                #Opens file in write mode and writes the orderslistboxstring to the file after replacing some punctuation    
                with open(path+"/organiseTwo.txt", "w") as organiseOne:
                    organiseOne.write(str(ordersListboxString.replace("'", "").replace(",", "").replace("(", "").replace(" ", "").replace(")", "")))
                #Saves file locations to variables
                input_file = path+"/organiseTwo.txt"
                output_file = path+"/organiseOne.txt"

                #Read the input file
                with open(input_file, 'r') as file:
                    content = file.read()

                #Write the updated content to the output file
                with open(output_file, 'w') as file:
                    file.write(content)

                #Sets an empty array
                wordCounts = {}

                #Opens a file in read mode and another in write mode
                with open(path+"/organiseOne.txt", "r") as organiseOne, open(path+"/organiseTwo.txt", "w") as organiseTwo:

                    #Iterating through lines in a file     
                    for line in organiseOne:
                        #Striping words and splitting words into collumns
                        words = line.strip().split("|")
                        #Iterates through all words in an array
                        for word in words:
                            #If word does not equal nothing
                            if word != '':
                                #Checks if word is in wordcounts, if it is it adds 1 to total
                                if word in wordCounts:
                                    wordCounts[word] += 1

                                #Adds word to word count     
                                else:
                                    wordCounts[word] = 1

                    #Writes array to text file
                    organiseTwo.write(str(wordCounts))

                #Opens a file in read mode and another in write mode and formats the contents
                with open(path+"/organiseTwo.txt", "r") as organiseTwo, open(path+"/organiseOne.txt", "w") as organiseOne:
                    itemsUprocessed= organiseTwo.read()
                    organiseOne.write(str(itemsUprocessed).replace("{", "").replace("'", "").replace(",", "\n").replace(":", "|").replace(" ", "").replace("}", ""))

                #Opens a file in read mode and another in write mode and splits contents into collumns
                with open(path+"/organiseOne.txt", "r") as organiseOne, open(path+"/organiseTwo.txt", "w") as organiseTwo:
                    for line in organiseOne:
                        collumns = line.strip().split("|")
                        collumnOne = collumns[0]
                        collumnTwo = collumns[1]   

                        #Creating new line format
                        newLine = currentDateTime + ", " + collumnTwo + ", " + collumnOne + "\n"

                        #Writing new line format to the file
                        organiseTwo.write(newLine)

                #Opens a file in read mode and another in write mode
                with open(path+"/organiseTwo.txt", "r") as organiseTwo, open(path+"/organiseOne.txt", "w") as organiseOne:
                    items= organiseTwo.read()
                    organiseOne.write(items)

                #Saving file locations to variables
                csv_file = path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Long_Term_Log.csv"
                txt_file = path+"/organiseOne.txt"

                #Sets empty lists
                column_one = []
                column_two = []
                column_three = []

                #Opens file in read mode and saves file to a list
                with open(txt_file, 'r') as file:
                    for line in file:
                        values = line.strip().split(',')
                        #Checks if amount of values in this list is equal to or greator than 2
                        if len(values) >= 2:
                            column_one.append(values[0])
                            column_two.append(values[1])
                            column_three.append(values[2])

                #Write to CSV file
                with open(csv_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(zip(column_one, column_two, column_three))

                #Deletes the files
                os.remove(f"{path}/organiseOne.txt")
                os.remove(f"{path}/organiseTwo.txt")

                #Clears all widgits in middle frame and right frame
                for widgets in middleFrame.winfo_children():
                    widgets.destroy()
                for widgets in rightFrame.winfo_children():
                    widgets.destroy()


            #Defines function to confirm the order
            def confirmedOrder():
                #Gets selection from the listboxs
                resultShort= shortTermCheckbox.get()
                resultLong= longTermCheckbox.get()

                #Checks if short term checkbox was selected 
                if resultShort == 1:
                    #Checks if long term checkbox was selected
                    if resultLong == 1:
                        #Creates a ctk window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates a ctk label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "You have selected more than one box, Please try again",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates a ctk button
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)
                            
                    #Checks if long term checkbox was not selected
                    elif resultLong == 0:
                        #Defines the list
                        button_list = [AACMemberOptionsButton,listOfStoresButton,orderingOptionsButton,storesReturnsButton,selectPersonOrderingButton,closeWindow]
                        #Goes through the list and enables the buttons
                        for button in button_list:
                            button.configure(state= NORMAL)
                        #Calls the function
                        shortTermCheckboxEvent()

                    #Checks if anything else was done to checkbox
                    else:
                        #Creates ctk window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates a ctk label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "We have encounted an error, Please try again",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates ctk button
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)
                        
                #Checks if long term checkbox was selected
                elif resultLong == 1:
                    #Checks if short term checkbox was selected
                    if resultShort == 1:
                        #Creates a ctk window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates a ctk label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "You have selected more than one box, Please try again",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates a ctk button
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)

                    #Checks if short term checkbox was not selected
                    elif resultShort == 0:
                        #Defines a list
                        button_list = [AACMemberOptionsButton,listOfStoresButton,orderingOptionsButton,storesReturnsButton,selectPersonOrderingButton,closeWindow]
                        #Enables all buttons in the list
                        for button in button_list:
                            button.configure(state= NORMAL)
                        #Calls the function
                        longTermCheckboxEvent()

                    #Checks if anything else was done to checkbox
                    else:
                        #Creates ctk window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates ctk label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "We have encounted an error, Please try again",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates ctk button
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)
                
                #Checks if short term and long term checkboxs are not selected
                elif resultShort == 0 and resultLong == 0:
                    #Creates a ctk window
                    errorWindow= ctk.CTkToplevel(root)
                    errorWindow.title("Error Window")
                    errorWindow.geometry("1200x500")
                    errorWindow.transient(root)
                    errorWindow.lift()
                    
                    #Creates a ctk label
                    errorLabel= ctk.CTkLabel(
                        errorWindow,
                        text= "You have not selected a box, Please try again.",
                        font= standardFont
                        )
                    errorLabel.pack(pady= standardYPadding)

                    #Creates a ctk button
                    errorButton= ctk.CTkButton(
                        errorWindow,
                        text= "Close Window",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= errorWindow.destroy
                        )
                    errorButton.pack(pady= standardYPadding)

                #Checks if anything else was done to checkbox
                else:
                    #Creates a ctk Window
                    errorWindow= ctk.CTkToplevel(root)
                    errorWindow.title("Error Window")
                    errorWindow.geometry("1200x500")
                    errorWindow.transient(root)
                    errorWindow.lift()

                    #Creates a ctk label
                    errorLabel= ctk.CTkLabel(
                        errorWindow,
                        text= "We have encounted an error, Please try again",
                        font= standardFont
                        )
                    errorLabel.pack(pady= standardYPadding)

                    #Creates a ctk button
                    errorButton= ctk.CTkButton(
                        errorWindow,
                        text= "Close Window",
                        font= standardFont,
                        width= standardHeight,
                        height= standardHeight,
                        command= errorWindow.destroy
                        )
                    errorButton.pack(pady= standardYPadding)

            #Opens file in read mode and reads the contents
            with open(filePath, 'r') as file:
                reader = csv.reader(file)
                contents = [row for row in reader]

            #Deletes contents in list box and rewrites the new contents into it
            storesListListbox.delete(0, END)
            for row in contents:
                storesListListbox.insert(END, row)

            #Adds the command prompt the button functions
            addToOrderBotton.configure(command=addToOrder)
            removeFromOrderBotton.configure(command=removeFromOrder)
            confirmOrderBotton.configure(command=confirmedOrder)


        #Checks that there is a selection
        def selectedPersonOrdering():
            #Makes a global variable
            global rankNameClean
            #Gets curser selectin
            rankNameSelection= namesListListbox.curselection()
            #Checks if there was no selection
            if not rankNameSelection:
                #Creates ctk window
                errorWindow= ctk.CTkToplevel(root)
                errorWindow.title("Error Window")
                errorWindow.geometry("1200x500")
                errorWindow.transient(root)
                errorWindow.lift()

                #Creates ctk label    
                errorLabel= ctk.CTkLabel(
                    errorWindow,
                    text= "You have not selected a person, Please try again.",
                    font= standardFont
                    )
                errorLabel.pack(pady= standardYPadding)

                #Creates ctk button
                errorButton= ctk.CTkButton(
                    errorWindow,
                    text= "Close Window",
                    font= standardFont,
                    width= standardWidth,
                    height= standardHeight,
                    command= errorWindow.destroy
                    )
                errorButton.pack(pady= standardYPadding)

            #Checks if there was a selection
            else:
                #Gets value in the selection
                rankName= namesListListbox.get(rankNameSelection[0])
                #Cleans the string up removing any unwanted character
                rankNameClean= str(rankName).replace("(", "").replace("'", "").replace(",", "").replace(" ", "_").replace(")", "")
                #Calls the function
                storesList()


        #Defines function where all stores are listed
        def storesList():

            #Defines function that sets file path
            def SlouchHatAndRelatedItemsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/Slouch_Hats_Puggarees_Chinstrap.csv"

                #Calls the function
                ordering()


            #Defines function that sets file path 
            def JumpersAndRainjacketsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/Jumpers_and_Rainjackets.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def PatchesAndRankslidesList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/Patches_and_Rankslides.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def OtherUniformList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/Other_Uniform.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def UndershirtsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/Undershirts.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def BootsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/Boots.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def AMCUBushHatList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/AMCU_Bush_Hats.csv"
                
                #Calls the function
                ordering()
            

            #Defines function that sets file path
            def AMCUShirtsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/AMCU_Shirts.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def AMCUPantsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/AMCU_Pants.csv"
                
                #Calls the function
                ordering()
            

            #Defines function that sets file path
            def DPCUBushHatList():


                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/DPCU_Bush_Hats.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def DPCUShirtsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/DPCU_Shirts.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def DPCUPantsList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/DPCU_Pants.csv"
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def EquipmentList():

                #Makes variable global and sets file path as a variable
                global filePath
                filePath = path+"/stores/Equipment.csv"
                
                #Calls the function
                ordering()


            #Clear all widgits in a frame
            for widgets in middleFrame.winfo_children():
                widgets.destroy()
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a ctk canvas
            canvas = ctk.CTkCanvas(middleFrame, bg= "#292929", highlightthickness=0)
            canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

            #Creates a scroll bar
            buttonScrollbar= ctk.CTkScrollbar(middleFrame, orientation=VERTICAL, command=canvas.yview)
            buttonScrollbar.pack(side="right", fill=Y)
            canvas.configure(yscrollcommand=buttonScrollbar.set)
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))

            #Creates a ctk frame
            buttonFrame= ctk.CTkFrame(canvas, fg_color= "#292929")
            buttonFrame.pack(pady = standardYPadding)

            #Creats canvas window?
            canvas.create_window((0,0), window=buttonFrame, anchor= "nw")

            #Creates ctk button
            SlouchHatAndRelatedItems = ctk.CTkButton(
                buttonFrame,
                text= "Slouch Hats & Related Items",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=SlouchHatAndRelatedItemsList,
                )
            SlouchHatAndRelatedItems.pack(pady = 5)

            #Creates ctk button
            JumpersAndRainjackets = ctk.CTkButton(
                buttonFrame,
                text= "Jumpers and Rainjackets",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=JumpersAndRainjacketsList,
                )
            JumpersAndRainjackets.pack(pady = 5)

            #Creates ctk button
            PatchesAndRankslides = ctk.CTkButton(
                buttonFrame,
                text= "Patches and Rankslides",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=PatchesAndRankslidesList,
                )
            PatchesAndRankslides.pack(pady = 5)

            #Creates ctk button
            OtherUniform = ctk.CTkButton(
                buttonFrame,
                text= "Other Uniform",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= OtherUniformList,
                )
            OtherUniform.pack(pady = 5)

            #Creates ctk button
            Undershirts = ctk.CTkButton(
                buttonFrame,
                text= "Undershirts",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= UndershirtsList,
                )
            Undershirts.pack(pady = 5)

            #Creates ctk button
            Boots = ctk.CTkButton(
                buttonFrame,
                text= "Boots",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=BootsList,
                )
            Boots.pack(pady = 5)

            #Creates ctk button
            AMCUBushHat = ctk.CTkButton(
                buttonFrame,
                text= "AMCU Bush Hats",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= AMCUBushHatList,
                )
            AMCUBushHat.pack(pady = 5)

            #Creates ctk button
            AMCUShirts = ctk.CTkButton(
                buttonFrame,
                text= "AMCU Shirts",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= AMCUShirtsList,
                )
            AMCUShirts.pack(pady = 5)

            #Creates ctk button
            AMCUPants = ctk.CTkButton(
                buttonFrame,
                text= "AMCU Pants",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=AMCUPantsList,
                )
            AMCUPants.pack(pady = 5)

            #Creates ctk button
            DPCUBushHat = ctk.CTkButton(
                buttonFrame,
                text= "DPCU Bush Hats",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command= DPCUBushHatList,
                )
            DPCUBushHat.pack(pady = 5)

            #Creates ctk button
            DPCUShirts = ctk.CTkButton(
                buttonFrame,
                text= "DPCU Shirts",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=DPCUShirtsList,
                )
            DPCUShirts.pack(pady = 5)

            #Creates ctk button
            DPCUPants = ctk.CTkButton(
                buttonFrame,
                text= "DPCU Pants",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=DPCUPantsList,
                )
            DPCUPants.pack(pady = 5)

            #Creates ctk button
            Equipment = ctk.CTkButton(
                buttonFrame,
                text= "Equipment",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                command=EquipmentList,
                )
            Equipment.pack(pady = 5)

            #Creates a ctk label
            label = ctk.CTkLabel(rightFrame, text="Select An Item Then Click The Button Bellow \nThe Box To Add/Remove It From The Order ", fg_color="transparent", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates ctk frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack()

            #Makes variable global
            global storesListListbox
            #Creates a ctk list box
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 11, font= standardFont)
            storesListListbox.pack(side=LEFT)

            #Creates a ctk scroll bar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            storesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Makes the variable global
            global addToOrderBotton
            #Creates a ctk button
            addToOrderBotton = ctk.CTkButton(
                rightFrame,
                text= "Add Item To Order",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                )
            addToOrderBotton.pack(pady = standardYPadding)

            #Creates a ctk Label
            warningLabel= ctk.CTkLabel(rightFrame, text="IF THE BOX  BELLOW IS NOT EMPTY YOU WILL \n NOT BE ABLE TO LEAVE THIS PAGE", fg_color="transparent", font= standardFont)
            warningLabel.pack(pady= standardYPadding)

            #Creates a ctk frame
            listboxFrameTwo= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrameTwo.pack()

            #Makes variable global
            global ordersListbox
            #Creates a listbox
            ordersListbox = Listbox(listboxFrameTwo, bg= "#292929", fg= "Silver", width= 30, height= 11, font= standardFont)
            ordersListbox.pack(side=LEFT)

            #Creates a ctk scrollbar
            listboxScrollbarTwo= ctk.CTkScrollbar(listboxFrameTwo, command=ordersListbox.yview)
            listboxScrollbarTwo.pack(side="right", fill=Y)
            ordersListbox.config(yscrollcommand=listboxScrollbarTwo.set)        

            #Makes the variable global
            global removeFromOrderBotton
            #Creates a ctk button
            removeFromOrderBotton = ctk.CTkButton(
                rightFrame,
                text= "Remove Item From Order",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                )
            removeFromOrderBotton.pack(pady = standardYPadding)

            #Creates a ctk frame
            checkboxFrame= ctk.CTkFrame(rightFrame, width= 20, height= 20, fg_color= "#292929")
            checkboxFrame.pack()

            #Makes the variable global
            global shortTermCheckbox
            #Creates a ctk checkbox
            shortTermCheckbox= ctk.CTkCheckBox(
                checkboxFrame, 
                text="Short Term",
                font= ("", 15),
                checkbox_width= 20,
                checkbox_height= 20,
                onvalue= 1, 
                offvalue= 0,
                )
            shortTermCheckbox.pack(side= "left",padx= 25)

            #Makes the variable global
            global longTermCheckbox
            #Creates a ctk checkbox
            longTermCheckbox= ctk.CTkCheckBox(
                checkboxFrame, 
                text="Long Term",
                font= ("", 15), 
                checkbox_width= 20,
                checkbox_height= 20,
                onvalue= 1, 
                offvalue= 0,
                )
            longTermCheckbox.pack(side= "right", padx= 25)

            #Makes the variable global
            global confirmOrderBotton
            #Creates a ctk Button
            confirmOrderBotton = ctk.CTkButton(
                rightFrame,
                text= "Confirm Order",
                font= standardFont,
                width= standardWidth,
                height= standardHeight,
                )
            confirmOrderBotton.pack(pady = standardYPadding)



        #Opens file in read mode and reads the contents
        with open(path+"/namesList.csv", 'r') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]

        #Creates a ctk label
        label = ctk.CTkLabel(leftBottomFrame, text="Select The Person Ordering", fg_color="transparent", font= standardFont)
        label.pack(pady = standardYPadding)

        #Creates a ctk frame
        listboxFrame= ctk.CTkFrame(leftBottomFrame, fg_color= "#292929")
        listboxFrame.pack()

        #Creates a listbox and inserts the contents of the file into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 17, font= standardFont)
        for row in contents:
            namesListListbox.insert(END, row)
        namesListListbox.pack(side=LEFT)

        #Creates a ctk scrollbar
        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
        listboxScrollbar.pack(side="right", fill=Y)
        namesListListbox.config(yscrollcommand=listboxScrollbar.set)        

        #Creates a ctk button
        selectPersonOrderingButton = ctk.CTkButton(
            leftBottomFrame,
            text= "Select Person Ordering",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= selectedPersonOrdering,
            )
        selectPersonOrderingButton.pack(pady = standardYPadding)




    #Defines the function that handles store returns
    def storesReturns():

        #Defines the function to check if person was selected
        def selectedPersonReturning():
            #Makes variable global
            global rankNameClean
            #Gets users selection of the listbox
            rankNameSelection= namesListListbox.curselection()
            #Checks if there was no selection
            if not rankNameSelection:
                #Creates a ctk window
                errorWindow= ctk.CTkToplevel(root)
                errorWindow.title("Error Window")
                errorWindow.geometry("1200x500")
                errorWindow.transient(root)
                errorWindow.lift()
                
                #Creates a ctk label
                errorLabel= ctk.CTkLabel(
                    errorWindow,
                    text= "You have not selected a person, Please try again.",
                    font= standardFont
                    )
                errorLabel.pack(pady= standardYPadding)

                #Creates a ctk button
                errorButton= ctk.CTkButton(
                    errorWindow,
                    text= "Close Window",
                    font= standardFont,
                    width= standardWidth,
                    height= standardHeight,
                    command= errorWindow.destroy
                    )
                errorButton.pack(pady= standardYPadding)

            #Runs if there was a seletion
            else:
                #Gets the name from the seelection and gets rid of unwanted charactors and turns it into a string
                rankName= namesListListbox.get(rankNameSelection[0])
                rankNameClean= str(rankName).replace("(", "").replace("'", "").replace(",", "").replace(" ", "_").replace(")", "")
                #Calls the function
                viewLogs()

        #Defines the function that allows you to view logs
        def viewLogs():

            #Defines function to deal with long term logs
            def longTermLogReturn():
                #Gets listbox selection
                rowSelection = longTermLogListbox.curselection()

                #Runs if there was a selection
                if rowSelection:
                    #Sets all important information into the variables
                    rowIndex = rowSelection[0]
                    rowLong = contentsLong[rowIndex]
                    oldValueLong= int(rowLong[1])
                    quantityReturnLong = int(quantityReturnEntryLong.get())
                    newQuantity= oldValueLong - quantityReturnLong
                    rowLong[1] = newQuantity

                    #Checks if new quantity is equal to 0
                    if newQuantity == 0:
                        
                        #Runs if there was a selection
                        if rowSelection:
                            #Gets the selection
                            longTermLogList= longTermLogListbox.get(rowSelection[0])
                            #Getting values from column 1
                            item= longTermLogList[2]

                            #Find all CSV files in the folder
                            csv_folder = path+"/Stores"
                            csv_files = glob.glob(csv_folder + "/*.csv")

                            #Iterate through each CSV file
                            for csv_file in csv_files:
                                with open(csv_file, 'r') as file:
                                    contents = csv.reader(file)
                                    rows = list(contents)
                                    #Iterate over each row in the CSV
                                    for i, row in enumerate(rows):
                                        #If it has less than 2 values it skips over it
                                        if len(row) != 2:
                                            continue
                                        #If has more than 2 values it runs
                                        else:
                                            #Checking if item selected is in the csv
                                            if row[1] == item:
                                                current_qty = int(row[0])
                                                #Deletes selected item from listbox
                                                longTermLogListbox.delete(rowSelection[0])
                                                #Makes variable global
                                                global saveLongTermListbox
                                                #Gets item selected in listbox
                                                saveLongTermListbox = longTermLogListbox.get(0, END)
                                                #Adds the 2 quantity together and turns the int so str
                                                rows[i][0] = str(current_qty + quantityReturnLong)
                                                #Opens file in write mode and writes the new data to the file  
                                                with open(csv_file, 'w', newline='') as outfile: 
                                                    writer = csv.writer(outfile)
                                                    writer.writerows(rows)  
                                                    #Opens file in write mode and writes the new data to the file
                                                    with open(path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Long_Term_Log.csv", 'w', newline='') as longTermfile:
                                                        writer = csv.writer(longTermfile)
                                                        writer.writerows(longTermLogListbox.get(0, END))
                                                #Breaks the loop
                                                break                     

                    #Checks if new quantity is bigger than 0
                    elif newQuantity > 0:

                        #Formating the variable
                        newQuantity= " "+str(newQuantity)
                        rowLong[1] = newQuantity
                        
                        #Checks if there was selection
                        if rowSelection:
                            #Gets the selected value
                            longTermLogList= longTermLogListbox.get(rowSelection[0])

                            #Getting data from column 1
                            item= longTermLogList[2]

                            #Find all CSV files in the folder
                            csv_folder = path+"/Stores"
                            csv_files = glob.glob(csv_folder + "/*.csv")

                            #Iterate through each CSV file
                            for csv_file in csv_files:
                                with open(csv_file, 'r') as file:
                                    contents = csv.reader(file)
                                    rows = list(contents)
                                    #Iterate over each row in the CSV
                                    for i, row in enumerate(rows):
                                        #If it has less than 2 values it skips over it
                                        if len(row) != 2:
                                            continue
                                        #If has more than 2 values it runs
                                        else:
                                            #Checking if item selected is in the csv
                                            if row[1] == item:
                                                current_qty = int(row[0])
                                                #Gets item selected in listbox
                                                saveLongTermListbox = longTermLogListbox.get(0, END)
                                                #Adds the 2 quantity together and turns the int so str
                                                rows[i][0] = str(current_qty + quantityReturnLong)  
                                                #Opens file in write mode and writes the new data to the file  
                                                with open(csv_file, 'w', newline='') as outfile: 
                                                    writer = csv.writer(outfile)
                                                    writer.writerows(rows)  
                                                #Clears list box    
                                                longTermLogListbox.delete(0, END)
                                                #Every row in contentsLong is inserted into listbox
                                                for row in contentsLong:
                                                    longTermLogListbox.insert(END, row)
                                                #Opens file in write mode and writes the new data to the file
                                                with open(path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Long_Term_Log.csv", 'w', newline='') as longTermfile:
                                                    writer = csv.writer(longTermfile)
                                                    writer.writerows(contentsLong)

                    #Checks if new quantity is smaller than 0
                    elif newQuantity < 0:

                        #Creates a ctk window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates a ctk label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "Trying To Return More Than They Have Taken Out",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates a ctk button
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)
                            

            #Defines function to deal with short term logs
            def shortTermLogReturn():
                #Gets listbox selection
                rowSelection = shortTermLogListbox.curselection()

                #Runs if there was a selection
                if rowSelection:
                    #Sets all important information into the variables
                    rowIndex = rowSelection[0]
                    rowShort = contentsShort[rowIndex]
                    oldValueShort= int(rowShort[1])
                    quantityReturnShort = int(quantityReturnEntryShort.get())
                    newQuantity= oldValueShort - quantityReturnShort
                    rowShort[1] = newQuantity

                    #Checks if new quantity is equal to 0
                    if newQuantity == 0:

                        #Runs if there was a selection
                        if rowSelection:    
                            #Gets the selection
                            shortTermLogList= shortTermLogListbox.get(rowSelection[0]) 
                            #Getting values from column 1
                            item= shortTermLogList[2]
                                
                            #Find all CSV files in the folder
                            csv_folder = path+"/Stores"
                            csv_files = glob.glob(csv_folder + "/*.csv")

                            #Iterate through each CSV file
                            for csv_file in csv_files:
                                with open(csv_file, 'r') as file:
                                    contents = csv.reader(file)
                                    rows = list(contents)
                                    #Iterate over each row in the CSV
                                    for i, row in enumerate(rows):
                                        #If it has less than 2 values it skips over it
                                        if len(row) != 2:
                                            continue
                                        #If has more than 2 values it runs
                                        else:
                                            #Checking if item selected is in the csv
                                            if row[1] == item:
                                                current_qty = int(row[0])
                                                #Deletes selected item from listbox
                                                shortTermLogListbox.delete(rowSelection[0]) 
                                                #Makes variable global
                                                global saveShortTermListbox
                                                #Gets item selected in listbox
                                                saveShortTermListbox = shortTermLogListbox.get(0, END)
                                                #Adds the 2 quantity together and turns the int so str
                                                rows[i][0] = str(current_qty + quantityReturnShort)
                                                #Opens file in write mode and writes the new data to the file  
                                                with open(csv_file, 'w', newline='') as outfile: 
                                                    writer = csv.writer(outfile)
                                                    writer.writerows(rows) 
                                                    #Opens file in write mode and writes the new data to the file
                                                    with open(path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Short_Term_Log.csv", 'w', newline='') as shortTermfile:
                                                        writer = csv.writer(shortTermfile)
                                                        writer.writerows(shortTermLogListbox.get(0, END))
                                                #Breaks the loop
                                                break
                    #Checks if new quantity is bigger than 0
                    elif newQuantity > 0:

                        #Formating the variable
                        newQuantity= " "+str(newQuantity)
                        rowShort[1] = newQuantity

                        #Checks if there was selection
                        if rowSelection:   
                            #Gets the selected value 
                            shortTermLogList= shortTermLogListbox.get(rowSelection[0]) 

                            #Getting data from column 1
                            item= shortTermLogList[2]
                                
                            #Find all CSV files in the folder
                            csv_folder = path+"/Stores"
                            csv_files = glob.glob(csv_folder + "/*.csv")

                            #Iterate through each CSV file
                            for csv_file in csv_files:
                                with open(csv_file, 'r') as file:
                                    contents = csv.reader(file)
                                    rows = list(contents)
                                    #Iterate over each row in the CSV
                                    for i, row in enumerate(rows):
                                        #If it has less than 2 values it skips over it
                                        if len(row) != 2:
                                            continue
                                        #If has more than 2 values it runs
                                        else:
                                            #Checking if item selected is in the csv
                                            if row[1] == item:
                                                current_qty = int(row[0])
                                                #Gets item selected in listbo
                                                saveShortTermListbox = shortTermLogListbox.get(0, END)
                                                #Adds the 2 quantity together and turns the int so str
                                                rows[i][0] = str(current_qty + quantityReturnShort) 
                                                #Opens file in write mode and writes the new data to the file  
                                                with open(csv_file, 'w', newline='') as outfile: 
                                                    writer = csv.writer(outfile)
                                                    writer.writerows(rows)  
                                                #Clears list box    
                                                shortTermLogListbox.delete(0, END)
                                                #Every row in contentsLong is inserted into listbox
                                                for row in contentsShort:
                                                    shortTermLogListbox.insert(END, row)
                                                #Opens file in write mode and writes the new data to the file
                                                with open(path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Short_Term_Log.csv", 'w', newline='') as shortTermfile:
                                                    writer = csv.writer(shortTermfile)
                                                    writer.writerows(contentsShort)

                    #Checks if new quantity is smaller than 0
                    elif newQuantity < 0:

                        #Creates a ctk window
                        errorWindow= ctk.CTkToplevel(root)
                        errorWindow.title("Error Window")
                        errorWindow.geometry("1200x500")
                        errorWindow.transient(root)
                        errorWindow.lift()

                        #Creates a ctk label
                        errorLabel= ctk.CTkLabel(
                            errorWindow,
                            text= "Trying To Return More Than They Have Taken Out",
                            font= standardFont
                            )
                        errorLabel.pack(pady= standardYPadding)

                        #Creates a ctk button
                        errorButton= ctk.CTkButton(
                            errorWindow,
                            text= "Close Window",
                            font= standardFont,
                            width= standardWidth,
                            height= standardHeight,
                            command= errorWindow.destroy
                            )
                        errorButton.pack(pady= standardYPadding)



            #Clears all widgits from window
            for widgets in middleFrame.winfo_children():
                widgets.destroy()
            for widgets in rightFrame.winfo_children():
                widgets.destroy()
            
            #Opens a file in read mode and reads the file
            with open(path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Long_Term_Log.csv", 'r') as longTermFile:
                reader = csv.reader(longTermFile)
                #Makes global variable
                global contentsLong
                contentsLong = [row for row in reader]

            #Creates a ctk label
            longTermLoglabel = ctk.CTkLabel(middleFrame, text="Long Term Log", fg_color="transparent", font= standardFont)
            longTermLoglabel.pack(pady = standardYPadding)

            #Creates a ctk frame
            listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
            listboxFrame.pack()

            #Creates a listbox and insert contents from file into it
            longTermLogListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height= 28, font= standardFont)
            for row in contentsLong:
                longTermLogListbox.insert(END, row)
            longTermLogListbox.pack(side=LEFT)

            #Creates a ctk scrollbar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=longTermLogListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            longTermLogListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a ctk frame
            frameOne= ctk.CTkFrame(middleFrame, fg_color= "#292929")
            frameOne.pack()

            #Creates a ctk entry box
            quantityReturnEntryLong = ctk.CTkEntry(
                frameOne, 
                placeholder_text="Enter Quantity Returned",
                font= standardFont,
                width= 210,
                height= standardHeight,
                )
            quantityReturnEntryLong.pack(side= "left", padx = 10, pady = 20)

            #Creates a ctk button 
            changeQuantityButtonLong = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 100,
                height= standardHeight,
                command= longTermLogReturn,
                )
            changeQuantityButtonLong.pack(side= "right", padx = 10, pady = 20)

            #Opens a file in read mode and reads the file
            with open(path+"/People_And_Logs/"+rankNameClean+"/"+rankNameClean+"_Short_Term_Log.csv", 'r') as shortTermFile:
                reader = csv.reader(shortTermFile)
                contentsShort = [row for row in reader]

            #Creates a ctk label
            shortTermLogLabel = ctk.CTkLabel(rightFrame, text="Short Term Log", fg_color="transparent", font= standardFont)
            shortTermLogLabel.pack(pady = standardYPadding)

            #Creates a ctk frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack()

            #Creates a listbox and insert contents from file into it
            shortTermLogListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height= 28, font= standardFont)
            for row in contentsShort:
                shortTermLogListbox.insert(END, row)
            shortTermLogListbox.pack(side=LEFT)

            #Creates a ctk scrollbar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=shortTermLogListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            shortTermLogListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a ctk frame
            frameTwo= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            frameTwo.pack()

            #Creates a ctk entry box
            quantityReturnEntryShort = ctk.CTkEntry(
                frameTwo, 
                placeholder_text="Enter Quantity Returned",
                font= standardFont,
                width= 210,
                height= standardHeight,
                )
            quantityReturnEntryShort.pack(side= "left", padx = 10, pady = 20)

            #Creates a ctk button 
            changeQuantityButtonShort = ctk.CTkButton(
                frameTwo,
                text= "Update Quantity",
                font= standardFont,
                width= 100,
                height= standardHeight,
                command= shortTermLogReturn,
                )
            changeQuantityButtonShort.pack(side= "right", padx = 10, pady = 20)
    

        #Clears all widgets
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Opens a file in read mode and reads it
        with open(path+"/namesList.csv", 'r') as file:
            reader = csv.reader(file)
            contentsNames = [row for row in reader]

        #Creates a ctk label
        label = ctk.CTkLabel(leftBottomFrame, text="Select The Person Returning", fg_color="transparent", font= standardFont)
        label.pack(pady = standardYPadding)

        #Creats a ctk frame
        listboxFrame= ctk.CTkFrame(leftBottomFrame, fg_color= "#292929")
        listboxFrame.pack()

        #Creates a listbox and insert contents from file into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 17, font= standardFont)
        for row in contentsNames:
            namesListListbox.insert(END, row)
        namesListListbox.pack(side=LEFT)

        #Creates a ctk scrollbar
        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
        listboxScrollbar.pack(side="right", fill=Y)
        namesListListbox.config(yscrollcommand=listboxScrollbar.set)

        #Creates a ctk button 
        selectPersonOrderingButton = ctk.CTkButton(
            leftBottomFrame,
            text= "Select Person Returning",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= selectedPersonReturning,
            )
        selectPersonOrderingButton.pack(pady = standardYPadding)




    #Creates a button
    AACMemberOptionsButton = ctk.CTkButton(
        leftTopFrame,
        text= "AAC Member Options",
        font= standardFont,
        width= standardWidth,
        height= standardHeight,
        command=AACMemberOptions,
        )
    AACMemberOptionsButton.pack(pady = standardYPadding)

    #Creates a button
    listOfStoresButton = ctk.CTkButton(
        leftTopFrame,
        text= "List Of Stores",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= listStores,
        )
    listOfStoresButton.pack(pady = standardYPadding)

    #Creates a button
    orderingOptionsButton = ctk.CTkButton(
        leftTopFrame,
        text= "Ordering Options",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= orderingOptions,
        )
    orderingOptionsButton.pack(pady = standardYPadding)

    #Creates a button
    storesReturnsButton = ctk.CTkButton(
        leftTopFrame,
        text= "Stores Returns",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= storesReturns,
        )
    storesReturnsButton.pack(pady = standardYPadding)
   
    #Creates a button 
    closeWindow = ctk.CTkButton(
        leftTopFrame, 
        text="Close Window", 
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command=root.destroy
        )
    closeWindow.pack(pady = standardYPadding)

    #Loops through the program
    root.mainloop()

#Calls the function
Q_Store_Software_06()