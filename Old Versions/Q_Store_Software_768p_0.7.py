# Finish by 13th of September

#Import addons to python language (WILL NOT WORK WITHOUT)
import customtkinter as ctk #Will need to install this via pip in comand prompt
from   tkinter import *
import datetime
import re
import sqlite3
from contextlib import closing



#Function that contains the Program
def Q_Store_Software_07():

    #Defining variables to make it easier to change size of everything
    standardHeight= 25
    standardWidth= 250
    standardFont= "", 14
    standardYPadding= 10

    #Defining colour mode for the program (light or dark)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    #Setting program main window
    root = ctk.CTk()
    root.title("505ACU Albany Q-Store Software Version: 0.7")
    screenWidth = 1280 #root.winfo_screenwidth()
    screenHeight = 768 #root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}")
    root.state('zoomed')

    connection = sqlite3.connect("505_ACU_Q-Store_Database.db")

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
                email = first+'.'+last_name+'@armycadets.gov.au'

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

                            cursor = connection.cursor()
                            cursor.execute(f"INSERT INTO Cadets (rank,first_name,last_name,email) VALUES ('{rank}', '{first}', '{last_name}', '{email}')")
                            connection.commit()

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

            #Creates frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Creates list box and puts names into listbox using SQL
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 20, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT rank,first_name,last_name FROM Cadets").fetchall()
            formatted_data = []
            for row in data:
                formatted_data.append(' '.join(row))
            for row in formatted_data:
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
                placeholder_text="Enter First Name",
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
                    #Deletes data from the database
                    cursor = connection.cursor()
                    cursor.execute(f'DELETE FROM Cadets WHERE CadetID={cadetID}')
                    connection.commit()
                    
                    removeAACMemberOptions()

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
                cadetID = stringAACMember.split()[0]

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

            #Create frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Creates list box and fills it with members names using SQL
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT CadetID,rank,first_name,last_name FROM Cadets").fetchall()
            formatted_data = []
            for row in data:
                formatted_data.append(' '.join(map(str, row)))
            for row in formatted_data:
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
                    #Gets all required information and turns it into usable variables
                    rowIndexRank = rowSelectionRank[0]
                    rowRank = formatted_data[rowIndexRank]
                    rowRankString= str(rowRank)
                    cadetID = rowRankString.split()[0]
                    cadeNewRank = newRankEntry.get()

                    #Updates rank in database using SQL
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Cadets SET rank='{cadeNewRank}' WHERE CadetID={cadetID}")
                    connection.commit()

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

            #Creating a label
            label = ctk.CTkLabel(rightFrame, text="Select The Person You Wish To Modify", fg_color="transparent", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creating list box frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Creating list box and inserting contents of database into it using SQL
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 20, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT CadetID,rank,first_name,last_name FROM Cadets").fetchall()
            formatted_data = []
            for row in data:
                formatted_data.append(' '.join(map(str, row)))
            for row in formatted_data:
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

            #Creates listbox frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = 50)

            #Creates listbox and inserts contents of database into it
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT CadetID,rank,first_name,last_name FROM Cadets").fetchall()
            formatted_data = []
            for row in data:
                formatted_data.append(' '.join(map(str, row)))
            for row in formatted_data:
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()



                #Call the function
                SlouchHatAndRelatedItemsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=11").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                JumpersAndRainjacketsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=8").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                PatchesAndRankslidesList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Qty FROM Stores WHERE CategoryID=10").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                qty = item[2]
                formatted_data.append(f"{store_id}, {name}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                OtherUniformList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=9").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                UndershirtsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=12").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                BootsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into itt
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=7").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                AMCUBushHatList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=1").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                AMCUShirtsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and wrightse the contents of the file opened into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=3").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                AMCUPantsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=2").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                DPCUBushHatList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=4").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                DPCUShirtsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=6").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                DPCUPantsList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Size, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=5").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                size = item[2] if item[2] is not None else 'N/A'
                qty = item[3]
                formatted_data.append(f"{store_id}, {name} {size}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    #Getting all information required and gets quantity and ID using SQL
                    rowIndex = rowSelection[0]
                    row = formatted_data[rowIndex]
                    newQuantity = newQuantityEntry.get()
                    storeID= str(row).split(',')
                    storeID = storeID[0].strip()
                    cursor = connection.cursor()
                    cursor.execute(f"UPDATE Stores SET Qty='{newQuantity}' WHERE StoreID={storeID}")
                    connection.commit()

                #Call the function
                EquipmentList()


            #Clear all widgits in right frame
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates a label
            label= ctk.CTkLabel(rightFrame, text="Select the item you wish to modify \n FORMAT = StoreID, Name, Qty", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates a frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = standardYPadding)

            #Create list box and writes the contents of the database into it
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=25, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT StoreID,Name,Qty FROM Stores WHERE CategoryID=13").fetchall()
            formatted_data = []
            for item in data:
                store_id = item[0]
                name = item[1]
                qty = item[2]
                formatted_data.append(f"{store_id}, {name}, {qty}")
            for row in formatted_data:
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
                width= 175,
                height= standardHeight,
                )
            newQuantityEntry.pack(side= "left", padx = 10)

            #Creates a button
            changeQuantityButton = ctk.CTkButton(
                frameOne,
                text= "Update Quantity",
                font= standardFont,
                width= 175,
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
                    itemID = itemString.split(',')[0].strip().replace("'","").replace(")","")
                    itemQuantity = itemString.split(',')[2].strip().replace("'","").replace(")","")
                    itemQuantityInt = int(itemQuantity)
                    item = itemString.split(',')[1].strip().replace("'","").replace(")","")
                    item = itemID+', '+item
                    qty_sale = "1" 

                    if itemQuantityInt < int(qty_sale):
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
                        ordersListbox.insert(END, f"{item}")
                        #Makes variable global
                        global saveOrdersListbox
                        #saving contents of the listbox
                        saveOrdersListbox = ordersListbox.get(0, END)
                        #subtracts 1 from the current quantity
                        newItemQuantity = str(itemQuantityInt - 1)
                        #Updates the database using SQL
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE Stores SET Qty='{newItemQuantity}' WHERE StoreID={itemID}")
                        connection.commit()

                        #Retrieves data from database to be inserted into listbox
                        cursor = connection.cursor()
                        data = cursor.execute(SQLCommand).fetchall()
                        formatted_data = []
                        for item in data:
                            store_id = item[0]
                            name = item[1]
                            size = item[2] if item[2] is not None else 'N/A'
                            qty = item[3]
                            formatted_data.append(f"{store_id}, {name} {size}, {qty}")

                        #Clears all information in listbox
                        storesListListbox.delete(0, END)
                            #Inserts database data into listbox
                        for row in formatted_data:
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
                #If there is a selection it gets selected value in the listbox and turns it into a string and splits it into useful values saved as variables
                if selection:
                    itemListBox = storesListListbox.get(selection[0]) 
                    itemString = str(itemListBox)
                    itemID = itemString.split(',')[0].strip().replace("'","").replace(")","")
                    itemQuantity = itemString.split(',')[2].strip().replace("'","").replace(")","")
                    itemQuantityInt = int(itemQuantity)
                    item = itemString.split(',')[1].strip().replace("'","").replace(")","")
                    item = itemID+', '+item
                    qty_sale = "1" 
                        
                    if itemQuantityInt < int(qty_sale):
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
                        newItemQuantity = str(itemQuantityInt + 1)
                        
                        #Updates database using SQL
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE Stores SET Qty='{newItemQuantity}' WHERE StoreID={itemID}")
                        connection.commit()

                        #Retrieves data from database to be inserted into listbox
                        cursor = connection.cursor()
                        data = cursor.execute(SQLCommand).fetchall()
                        formatted_data = []
                        for item in data:
                            store_id = item[0]
                            name = item[1]
                            size = item[2] if item[2] is not None else 'N/A'
                            qty = item[3]
                            formatted_data.append(f"{store_id}, {name} {size}, {qty}")

                        #Deletes all contents in listbox and inserts contents of database into the now empty listbox
                        storesListListbox.delete(0, END)
                        for row in formatted_data:
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
                Data_Taken = datetime.datetime.now().strftime("%d/%m/%Y")
                Log_TypeID='2'
                

                #Setting a variable
                ordersListboxString = ""
                ordersListboxList = ""

                #Saves listbox to a variable
                for i in range(ordersListbox.size()):
                    ordersListboxString += str(ordersListbox.get(i)) + "\n"
                    ordersListboxList += ordersListbox.get(i)
                saveOrdersListbox = ordersListbox.get(0, END)

                #Sets an empty array
                wordCounts = {}

                #Iterating through lines in a file    
                for row in saveOrdersListbox:
                    #Striping words and splitting words into collumns

                    if row != '':
                        #Checks if word is in wordcounts, if it is it adds 1 to total
                        if row in wordCounts:
                            wordCounts[row] += 1

                        #Adds word to word count    
                        else:
                            wordCounts[row] = 1

                #Removes unwanted puncuation
                ItemsClean= (str(wordCounts)).replace("{", "").replace("'", "").replace(",", "|").replace(":", ",").replace("}", "").replace(",", "|")

                #Splits the variable every 3 '|'
                ItemsClean = (ItemsClean)
                ItemsClean = ItemsClean.split('|')
                ItemsClean = [ItemsClean[i:i+3] for i in range(0, len(ItemsClean), 3)]
                #Saves data to variables
                for item in ItemsClean:
                    StoreID= str(item).split(',')[0].replace("[","").replace("'","").replace("]","").replace(" ","")
                    Qty_Taken= str(item).split(',')[2].replace("[","").replace("'","").replace("]","").replace(" ","")

                    #Inserts new data into database
                    cursor = connection.cursor()
                    cursor.execute(f"INSERT INTO Logs (CadetID,StoreID,Qty_Taken,Date_Taken,Log_TypeID) VALUES ('{CadetID}', '{StoreID}', '{Qty_Taken}', '{Data_Taken}', '{Log_TypeID}')")
                    connection.commit()
                        
                #Clears all widgits in middle frame and right frame
                for widgets in middleFrame.winfo_children():
                    widgets.destroy()
                for widgets in rightFrame.winfo_children():
                    widgets.destroy()


            #Defines the function that run when a checkbox is selected
            def longTermCheckboxEvent():

                #Gets the date and time     
                Data_Taken = datetime.datetime.now().strftime("%d/%m/%Y")
                Log_TypeID='1'
                

                #Setting a variable
                ordersListboxString = ""
                ordersListboxList = ""

                #Saves listbox to a variable
                for i in range(ordersListbox.size()):
                    ordersListboxString += str(ordersListbox.get(i)) + "\n"
                    ordersListboxList += ordersListbox.get(i)
                saveOrdersListbox = ordersListbox.get(0, END)

                #Sets an empty array
                wordCounts = {}

                #Iterating through lines in a file    
                for row in saveOrdersListbox:
                    #Striping words and splitting words into collumns

                    if row != '':
                        #Checks if word is in wordcounts, if it is it adds 1 to total
                        if row in wordCounts:
                            wordCounts[row] += 1

                        #Adds word to word count    
                        else:
                            wordCounts[row] = 1

                #Removes unwanted puncuation
                ItemsClean= (str(wordCounts)).replace("{", "").replace("'", "").replace(",", "|").replace(":", ",").replace("}", "").replace(",", "|")

                #Splits the variable every 3 '|'
                ItemsClean = (ItemsClean)
                ItemsClean = ItemsClean.split('|')
                ItemsClean = [ItemsClean[i:i+3] for i in range(0, len(ItemsClean), 3)]
                #Saves data to variables
                for item in ItemsClean:
                    StoreID= str(item).split(',')[0].replace("[","").replace("'","").replace("]","").replace(" ","")
                    Qty_Taken= str(item).split(',')[2].replace("[","").replace("'","").replace("]","").replace(" ","")

                    #Inserts new data into database
                    cursor = connection.cursor()
                    cursor.execute(f"INSERT INTO Logs (CadetID,StoreID,Qty_Taken,Date_Taken,Log_TypeID) VALUES ('{CadetID}', '{StoreID}', '{Qty_Taken}', '{Data_Taken}', '{Log_TypeID}')")
                    connection.commit()
                        
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


            #Deletes contents in list box and rewrites the new contents into it
            storesListListbox.delete(0, END)
            for row in formatted_data:
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

                #Makes global variable
                global CadetID
                CadetID= rankNameClean.split('_')[0]

                #Calls the function
                storesList()


        #Defines function where all stores are listed
        def storesList():

            #Defines function that sets file path
            def SlouchHatAndRelatedItemsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=11"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=11").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")

                #Calls the function
                ordering()


            #Defines function that sets file path 
            def JumpersAndRainjacketsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=8"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=8").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def PatchesAndRankslidesList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=10"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=10").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def OtherUniformList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=9"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=9").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")

                #Calls the function
                ordering()


            #Defines function that sets file path
            def UndershirtsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=12"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=12").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def BootsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=7"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=7").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def AMCUBushHatList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=1"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=1").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()
            

            #Defines function that sets file path
            def AMCUShirtsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=3"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=3").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def AMCUPantsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=2"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=2").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()
            

            #Defines function that sets file path
            def DPCUBushHatList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=4"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=4").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def DPCUShirtsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=6"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=6").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def DPCUPantsList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=5"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=5").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
                #Calls the function
                ordering()


            #Defines function that sets file path
            def EquipmentList():

                #Makes variables global
                global SQLCommand
                #Saves the command to a variable
                SQLCommand = "SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID=13"
                #Makes variables global
                global formatted_data
                #Selects data from database using SQL
                cursor = connection.cursor()
                data = cursor.execute("SELECT StoreID,Name,Qty FROM Stores WHERE CategoryID=13").fetchall()
                formatted_data = []
                for item in data:
                    store_id = item[0]
                    name = item[1]
                    size = item[2] if item[2] is not None else 'N/A'
                    qty = item[3]
                    formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                
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
            label = ctk.CTkLabel(rightFrame, text="Select An Item Then Click The Button Bellow \nThe Box To Add/Remove It From The Order \n\nFORMAT = StoreID, Name Size, QTY", fg_color="transparent", font= standardFont)
            label.pack(pady = 0)

            #Creates ctk frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack()

            #Makes variable global
            global storesListListbox
            #Creates a ctk list box
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 38, height= 12, font=('', 10))
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
            ordersListbox = Listbox(listboxFrameTwo, bg= "#292929", fg= "Silver", width= 38, height= 12, font=('', 10))
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




        #Creates a ctk label
        label = ctk.CTkLabel(leftBottomFrame, text="Select The Person Ordering", fg_color="transparent", font= standardFont)
        label.pack(pady = standardYPadding)

        #Creates a ctk frame
        listboxFrame= ctk.CTkFrame(leftBottomFrame, fg_color= "#292929")
        listboxFrame.pack()

        #Creates a listbox and inserts the contents of the file into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 15, font= standardFont)
        cursor = connection.cursor()
        data = cursor.execute("SELECT CadetID,rank,first_name,last_name FROM Cadets").fetchall()
        formattedDataName = []
        for row in data:
            formattedDataName.append(' '.join(map(str, row)))
        for row in formattedDataName:
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
                global CadetID
                CadetID = rankNameClean.split('_')[0]

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
                    row= longTermLogListbox.get(rowSelection[0])
                    rowClean= str(row).replace('[','').replace(']',',').split(',')
                    LogID= rowClean[0]
                    StoreID= rowClean[1]
                    rowLong = rowClean[3]
                    oldValueLong= int(rowLong[1])
                    quantityReturnLong = int(quantityReturnEntryLong.get())
                    newQuantity= oldValueLong - quantityReturnLong

                    #Checks if new quantity is equal to 0
                    if newQuantity == 0:

                        #Updates the qty in logs while deleating it from the logs on the database using SQL
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE Stores SET Qty= Qty + {quantityReturnLong} WHERE StoreID= {StoreID}")
                        cursor.execute(f"DELETE FROM Logs WHERE LogID= {LogID}").fetchall()
                        connection.commit()
                        viewLogs()

                    #Checks if new quantity is bigger than 0
                    elif newQuantity > 0:

                        #Updates the qty in logs while updating it from the logs on the database using SQL
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE Stores SET Qty= Qty + {quantityReturnLong} WHERE StoreID= {StoreID}")
                        cursor.execute(f"UPDATE Logs SET Qty_Taken= Qty_Taken - {quantityReturnLong} WHERE LogID= {LogID}").fetchall()
                        connection.commit()
                        viewLogs()

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
                    row= shortTermLogListbox.get(rowSelection[0])
                    rowClean= str(row).replace('[','').replace(']',',').split(',')
                    LogID= rowClean[0]
                    StoreID= rowClean[1]
                    rowShort = rowClean[3]
                    oldValueShort= int(rowShort[1])
                    quantityReturnShort = int(quantityReturnEntryShort.get())
                    newQuantity= oldValueShort - quantityReturnShort

                    #Checks if new quantity is equal to 0
                    if newQuantity == 0:
                        
                        #Updates the qty in logs while deleating it from the logs on the database using SQL
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE Stores SET Qty= Qty + {quantityReturnShort} WHERE StoreID= {StoreID}")
                        cursor.execute(f"DELETE FROM Logs WHERE LogID= {LogID}").fetchall()
                        connection.commit()
                        viewLogs()
                        
                    #Checks if new quantity is bigger than 0
                    elif newQuantity > 0:

                        #Updates the qty in logs while updating it from the logs on the database using SQL
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE Stores SET Qty= Qty + {quantityReturnShort} WHERE StoreID= {StoreID}")
                        cursor.execute(f"UPDATE Logs SET Qty_Taken= Qty_Taken - {quantityReturnShort} WHERE LogID= {LogID}").fetchall()
                        connection.commit()
                        viewLogs()

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
            

            #Creates a ctk label
            longTermLoglabel = ctk.CTkLabel(middleFrame, text="Long Term Log \nFORMAT = LogID, [StoreID] Name Size, QTY, Date", fg_color="transparent", font= standardFont)
            longTermLoglabel.pack(pady = standardYPadding)

            #Creates a ctk frame
            listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
            listboxFrame.pack()

            #Makes global variable
            global formatted_dataLong         

            #Creates a listbox and insert contents from file into it
            longTermLogListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 45, height= 30, font=('', 10))
            #Gets all required data from database using SQL and formats it into desired format
            cursor = connection.cursor()
            dataLogsLong = cursor.execute(f"SELECT Logs.LogID,Logs.StoreID,Logs.Qty_Taken,Logs.Date_Taken FROM Logs WHERE Logs.Log_TypeID = 1 AND Logs.CadetID = {CadetID};").fetchall()
            dataInnerJoinLong = cursor.execute("SELECT Stores.Name, Logs.StoreID FROM Logs INNER JOIN Stores ON Logs.StoreID = Stores.StoreID WHERE Logs.Log_TypeID = 2 AND Logs.CadetID = 7;").fetchall()
            formatted_dataLong = []
            for itemLogsLong in dataLogsLong:

                LogIDLong = itemLogsLong[0]
                cursor = connection.cursor()
                dataInnerJoinLong = cursor.execute(f"SELECT Stores.Name, Logs.StoreID FROM Logs INNER JOIN Stores ON Logs.StoreID = Stores.StoreID WHERE Logs.LogID = {LogIDLong};").fetchall()
                
                for ItemInnerJoinLong in dataInnerJoinLong:

                    StoreID = ItemInnerJoinLong[1]
                    cursor = connection.cursor()
                    storesDataLong= cursor.execute(f"SELECT Size FROM Stores WHERE StoreID= {StoreID}")

                    for itemStoresLong in storesDataLong:
                        NameLong = ItemInnerJoinLong[0]
                        SizeLong = itemStoresLong[0] if itemStoresLong[0] is not None else 'N/A'
                        Qty_TakenLong = itemLogsLong[2]
                        Date_TakenLong = itemLogsLong[3]
                        formatted_dataLong.append(f"{LogIDLong}, [{StoreID}] {NameLong} {SizeLong}, {Qty_TakenLong}, {Date_TakenLong}")
            
            #Inserts formated data into listbox
            for rowLong in formatted_dataLong:
                longTermLogListbox.insert(END, rowLong)
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

            #Creates a ctk label
            shortTermLogLabel = ctk.CTkLabel(rightFrame, text="Short Term Log \nFORMAT = LogID, [StoreID] Name Size, QTY, Date", fg_color="transparent", font= standardFont)
            shortTermLogLabel.pack(pady = standardYPadding)

            #Creates a ctk frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack()

            #Makes global variable
            global formatted_dataShort 

            #Creates a listbox and insert contents from file into it
            shortTermLogListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 45, height= 30, font=('', 10))
            #Gets all required data from database using SQL and formats it into desired format
            cursor = connection.cursor()
            dataLogsShort = cursor.execute(f"SELECT Logs.LogID,Logs.StoreID,Logs.Qty_Taken,Logs.Date_Taken FROM Logs WHERE Logs.Log_TypeID = 2 AND Logs.CadetID = {CadetID};").fetchall()
            formatted_dataShort = []
            for itemLogsShort in dataLogsShort:

                LogIDShort= itemLogsShort[0]
                cursor = connection.cursor()
                dataInnerJoinShort = cursor.execute(f"SELECT Stores.Name, Logs.StoreID FROM Logs INNER JOIN Stores ON Logs.StoreID = Stores.StoreID WHERE Logs.LogID = {LogIDShort};").fetchall()
                for ItemInnerJoinShort in dataInnerJoinShort:
  
                    StoreID = ItemInnerJoinShort[1]
                    cursor = connection.cursor()
                    storesDataShort= cursor.execute(f"SELECT Size FROM Stores WHERE StoreID= {StoreID}")

                    for itemStoresShort in storesDataShort:
                        NameShort = ItemInnerJoinShort[0]
                        SizeShort = itemStoresShort[0] if itemStoresShort[0] is not None else 'N/A'
                        Qty_TakenShort = itemLogsShort[2]
                        Date_TakenShort = itemLogsShort[3]
                        formatted_dataShort.append(f"{LogIDShort}, [{StoreID}] {NameShort} {SizeShort}, {Qty_TakenShort}, {Date_TakenShort}")

            #Inserts formated data into listbox
            for rowShort in formatted_dataShort:
                shortTermLogListbox.insert(END, rowShort)
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

        #Creates a ctk label
        label = ctk.CTkLabel(leftBottomFrame, text="Select The Person Returning", fg_color="transparent", font= standardFont)
        label.pack(pady = standardYPadding)

        #Creats a ctk frame
        listboxFrame= ctk.CTkFrame(leftBottomFrame, fg_color= "#292929")
        listboxFrame.pack()

        #Creates a listbox and insert contents from file into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 15, font= standardFont)
        cursor = connection.cursor()
        data = cursor.execute("SELECT CadetID,rank,first_name,last_name FROM Cadets").fetchall()
        formatted_data = []
        for row in data:
            formatted_data.append(' '.join(map(str, row)))
        for row in formatted_data:
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




    #Defines the function to close the program
    def closeProgram():
        #Closes database connection and the program
        with closing(sqlite3.connect("505_ACU_Q-Store_Database.db")) as connection:
            root.destroy()




    #Creates a label
    startLabel = ctk.CTkLabel(leftTopFrame, text="MADE BY CDTWO2 Alec McDonald \nFOR USE ONLY BY 505ACU Albany", font = standardFont)
    startLabel.pack(pady = standardYPadding)

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
        command= closeProgram
        )
    closeWindow.pack(pady = standardYPadding)

    #Loops through the program
    root.mainloop()

#Calls the function
Q_Store_Software_07()