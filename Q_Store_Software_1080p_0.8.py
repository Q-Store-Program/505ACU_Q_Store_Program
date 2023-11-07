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
    standardHeight= 30
    standardWidth= 250
    standardFont= "", 18
    standardYPadding= 10

    #Defining colour mode for the program (light or dark)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    #Setting program main window
    root = ctk.CTk()
    root.title("505ACU Albany Q-Store Software Version: 0.7")
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
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
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standardFont)
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
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 15, font= standardFont)
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

        def text_updation(categoryName):

            def viewStores():

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
                    viewStores()


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
                data = cursor.execute(f"SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID={categoryID}").fetchall()
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
            
            categoryID = categoryName[0]
            viewStores()


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

        cursor = connection.cursor()
        buttonDict = {}
        data = cursor.execute("SELECT CategoryID,Category FROM Categories").fetchall()
        for item in data:
                    
            def action(x = item): 
                return text_updation(x)

            category = item[1]

            buttonDict[item] = ctk.CTkButton(
            buttonFrame,
            text= category,
            font= standardFont,
            width= 300,
            height= standardHeight,
            command=action,
            )
            buttonDict[item].pack(pady = 5)
        



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

            def text_updation(categoryName):

                def selcetedCategory():

                    #Makes variables global
                    global SQLCommand
                    #Saves the command to a variable
                    SQLCommand = f"SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID={categoryID}"
                    #Makes variables global
                    global formatted_data
                    formatted_data=""
                    cursor = connection.cursor()
                    data = cursor.execute(f"SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID={categoryID}").fetchall()
                    formatted_data = []
                    for item in data:
                        store_id = item[0]
                        name = item[1]
                        size = item[2] if item[2] is not None else 'N/A'
                        qty = item[3]
                        formatted_data.append(f"{store_id}, {name} {size}, {qty}")
                    ordering()

                categoryID = categoryName[0]
                selcetedCategory()

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

            cursor = connection.cursor()
            buttonDict = {}
            data = cursor.execute("SELECT CategoryID,Category FROM Categories").fetchall()
            for item in data:
                
                def action(x = item): 
                    return text_updation(x)

                category = item[1]

                buttonDict[item] = ctk.CTkButton(
                buttonFrame,
                text= category,
                font= standardFont,
                width= 300,
                height= standardHeight,
                command=action,
                )
                buttonDict[item].pack(pady = 5)
                


            #Creates a ctk label
            label = ctk.CTkLabel(rightFrame, text="Select An Item Then Click The Button Bellow \nThe Box To Add/Remove It From The Order \n\nFORMAT = StoreID, Name Size, QTY", fg_color="transparent", font= standardFont)
            label.pack(pady = 0)

            #Creates ctk frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack()

            #Makes variable global
            global storesListListbox
            #Creates a ctk list box
            storesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height= 11, font= standardFont)
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
            warningLabel= ctk.CTkLabel(rightFrame, text="IF THE BOX BELLOW IS NOT EMPTY YOU WILL \n NOT BE ABLE TO LEAVE THIS PAGE", fg_color="transparent", font= standardFont)
            warningLabel.pack(pady= standardYPadding)

            #Creates a ctk frame
            listboxFrameTwo= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrameTwo.pack()

            #Makes variable global
            global ordersListbox
            #Creates a listbox
            ordersListbox = Listbox(listboxFrameTwo, bg= "#292929", fg= "Silver", width= 40, height= 11, font= standardFont)
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
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 17, font= standardFont)
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
            longTermLogListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height= 28, font= standardFont)
            #Gets all required data from database using SQL and formats it into desired format
            cursor = connection.cursor()
            dataLogsLong = cursor.execute(f"SELECT Logs.LogID,Logs.StoreID,Logs.Qty_Taken,Logs.Date_Taken FROM Logs WHERE Logs.Log_TypeID = 1 AND Logs.CadetID = {CadetID};").fetchall()
            dataInnerJoinLong = cursor.execute(f"SELECT Stores.Name, Logs.StoreID FROM Logs INNER JOIN Stores ON Logs.StoreID = Stores.StoreID WHERE Logs.Log_TypeID = 2 AND Logs.CadetID = {CadetID};").fetchall()
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
            shortTermLogListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height= 28, font= standardFont)
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
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 17, font= standardFont)
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




    #Defines the admin function
    def adminOptions():

        #Defines log in function
        def logIn():

            #Defines function that runs when user sucessfully logs in
            def succesfulLogIn():
                
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

                    #Deletes all widgits
                    for widgets in middleFrame.winfo_children():
                        widgets.destroy()
                    for widgets in rightFrame.winfo_children():
                        widgets.destroy()

                    #Creates a label
                    label= ctk.CTkLabel(middleFrame, text="Select the person you wish to remove", font= standardFont)
                    label.pack(pady = standardYPadding)

                    #Create frame
                    listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
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
                        middleFrame,
                        text= "Remove AAC Member From List",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= selectionChecker,
                        )
                    removeAACMemberButton.pack(pady = standardYPadding)

                #Defines function to change members rank
                def changeIDOptions():

                    #Defines function to update members rank
                    def updateID():

                        #Gets user selection
                        rowSelectionRank = namesListListbox.curselection()

                        #Checks if user selected an option
                        if rowSelectionRank:
                            #Gets all required information and turns it into usable variables
                            rowIndexRank = rowSelectionRank[0]
                            rowRank = formatted_data[rowIndexRank]
                            rowRankString= str(rowRank)
                            cadetID = rowRankString.split()[0]
                            cadeNewID = newIDEntry.get()

                            #Updates rank in database using SQL
                            cursor = connection.cursor()
                            cursor.execute(f"UPDATE Cadets SET CadetID='{cadeNewID}' WHERE CadetID={cadetID}")
                            connection.commit()

                        #Calls the function
                        changeIDOptions()

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
                            updateID()

                    for widgets in middleFrame.winfo_children():
                        widgets.destroy()
                    for widgets in rightFrame.winfo_children():
                        widgets.destroy()

                    #Creating a label
                    label = ctk.CTkLabel(middleFrame, text="Select The Person You Wish To Modify", fg_color="transparent", font= standardFont)
                    label.pack(pady = standardYPadding)

                    #Creating list box frame
                    listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
                    listboxFrame.pack(pady = standardYPadding)

                    #Creating list box and inserting contents of database into it using SQL
                    namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 25, height= 15, font= standardFont)
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
                    newIDEntry = ctk.CTkEntry(
                        middleFrame, 
                        placeholder_text="Enter New Cadet ID",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        )
                    newIDEntry.pack(pady = standardYPadding)

                    #Creating a button
                    changeRankButton = ctk.CTkButton(
                        middleFrame,
                        text= "Update Rank",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= selectionChecker,
                        )
                    changeRankButton.pack(pady = standardYPadding)

                #Creating the function to remove members from the names list and delete there files
                def removeStoreOptions():

                    


                    def text_updation(categoryName):

                        def viewStores():

                            def rightFrameWidgits():
                                
                                #Checks if they select a person
                                def selectionChecker():

                                    def removeItem():

                                        #Defines function that deletes member from list and there files
                                        def yes():
                                            #Deletes data from the database
                                            cursor = connection.cursor()
                                            cursor.execute(f'DELETE FROM Stores WHERE StoreID={StoreID}')
                                            connection.commit()
                                    
                                            areYouSureWindow.destroy()
                                            for widgets in rightFrame.winfo_children():
                                                widgets.destroy()
                                            viewStores()

                                        #Defines function to continue the program
                                        def no():
                                            #Closes window
                                            areYouSureWindow.destroy()

                                        item= storesListbox.get(itemSelection)
                                        stringItem= str(item)
                                        cleanStringItem= stringItem.replace("(", "").replace("'", "").replace(",", "").replace(" ", "_").replace(")", "")
                                        StoreID = stringItem.split()[0].replace(",", "")

                                        #Creates new window
                                        areYouSureWindow= ctk.CTkToplevel(root, fg_color= "#1f1f1f")
                                        areYouSureWindow.title("Are You Sure")
                                        areYouSureWindow.geometry("1200x500")
                                        areYouSureWindow.transient(root)
                                        areYouSureWindow.lift()
                                        
                                        #Creates label
                                        areYouSureLabel= ctk.CTkLabel(
                                            areYouSureWindow,
                                            text= f"Are You Sure You Want To Remove {cleanStringItem}\n\n This Will Permanently Remove All Information For This Item",
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

                                    #Gets user selection
                                    itemSelection= storesListbox.curselection()
                                    #Checks if there is not a selection
                                    if not itemSelection:
                                        #Creates error widnow
                                        errorWindow= ctk.CTkToplevel(root)
                                        errorWindow.title("Error Window")
                                        errorWindow.geometry("1200x500")
                                        errorWindow.transient(root)
                                        errorWindow.lift()
                                        
                                        #Creates a label
                                        errorLabel= ctk.CTkLabel(
                                            errorWindow,
                                            text= "You have not selected an item, Please try again.",
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
                                        removeItem()

                                for widgets in rightFrame.winfo_children():
                                    widgets.destroy()

                                #Creates a label
                                label= ctk.CTkLabel(rightFrame, text="Select the person you wish to remove", font= standardFont)
                                label.pack(pady = standardYPadding)

                                #Create frame
                                listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
                                listboxFrame.pack(pady = standardYPadding)

                                #Creates list box and fills it with members names using SQL
                                storesListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standardFont)
                                for row in formatted_data:
                                    storesListbox.insert(END, row)
                                storesListbox.pack(side=LEFT)

                                #Creates scroll bar
                                listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=storesListbox.yview)
                                listboxScrollbar.pack(side="right", fill=Y)
                                storesListbox.config(yscrollcommand=listboxScrollbar.set)        

                                #Creates button to call a function
                                removeAACMemberButton = ctk.CTkButton(
                                    rightFrame,
                                    text= "Remove item from stores",
                                    font= standardFont,
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= selectionChecker,
                                    )
                                removeAACMemberButton.pack(pady = standardYPadding)

                            #Makes variables global
                            global SQLCommand
                            #Saves the command to a variable
                            SQLCommand = f"SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID={CategoryID}"
                            #Makes variables global
                            global formatted_data
                            #Selects data from database using SQL
                            cursor = connection.cursor()
                            data = cursor.execute(f"SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID={CategoryID}").fetchall()
                            formatted_data = []
                            for item in data:
                                store_id = item[0]
                                name = item[1]
                                size = item[2] if item[2] is not None else 'N/A'
                                qty = item[3]
                                formatted_data.append(f"{store_id}, {name} {size}, {qty}")

                            #Calls the function
                            rightFrameWidgits()

                        CategoryID= categoryName[0]
                        viewStores()


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

                    cursor = connection.cursor()
                    buttonDict = {}
                    data = cursor.execute("SELECT CategoryID,Category FROM Categories").fetchall()
                    for item in data:
                                
                        def action(x = item): 
                            return text_updation(x)

                        category = item[1]

                        buttonDict[item] = ctk.CTkButton(
                        buttonFrame,
                        text= category,
                        font= standardFont,
                        width= 300,
                        height= standardHeight,
                        command=action,
                        )
                        buttonDict[item].pack(pady = 5)


                def addStoresOptions():

                    def text_updation(categoryName):

                        def viewStores():

                            #Defining function to update stores
                            def addItem():
                                itemName = itemNameEntry.get()
                                itemName = itemName.replace(' ','_')
                                itemSize = itemSizeEntry.get()
                                itemQuantity = itemQuantityEntry.get()
                                
                                if itemName == '':
                                    #Creates error window
                                    errorWindow= ctk.CTkToplevel(root)
                                    errorWindow.title("Error Window")
                                    errorWindow.geometry("500x100")
                                    errorWindow.transient(root)
                                    errorWindow.lift()

                                    #Creates a label
                                    errorLabel= ctk.CTkLabel(
                                        errorWindow,
                                        text= "You have not entered an item name",
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
                                
                                else:
                                    if itemSize != '':
                                        itemSize = itemSize
                                        cursor = connection.cursor()
                                        cursor.execute(f"INSERT INTO Stores (Name, CategoryID, Size, Qty) VALUES ('{itemName}','{categoryID}','{itemSize}','{itemQuantity}')")
                                        connection.commit()
                                    else:
                                        cursor = connection.cursor()
                                        cursor.execute(f"INSERT INTO Stores (Name, CategoryID, Qty) VALUES ('{itemName}','{categoryID}','{itemQuantity}')")
                                        connection.commit()
                                    
                                
                                

                                #Call the function
                                viewStores()


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
                            data = cursor.execute(f"SELECT StoreID,Name,Size,Qty FROM Stores WHERE CategoryID={categoryID}").fetchall()
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

                            #Creates an entry box
                            itemNameEntry = ctk.CTkEntry(
                                rightFrame, 
                                placeholder_text="Enter Item Name",
                                font= standardFont,
                                width= standardWidth,
                                height= standardHeight,
                                )
                            itemNameEntry.pack(pady = standardYPadding)

                            #Creates an entry box
                            itemSizeEntry = ctk.CTkEntry(
                                rightFrame, 
                                placeholder_text="Enter Item Size",
                                font= standardFont,
                                width= standardWidth,
                                height= standardHeight,
                                )
                            itemSizeEntry.pack(pady = standardYPadding)

                            #Creates an entry box
                            itemQuantityEntry = ctk.CTkEntry(
                                rightFrame, 
                                placeholder_text="Enter Item Quantity",
                                font= standardFont,
                                width= standardWidth,
                                height= standardHeight,
                                )
                            itemQuantityEntry.pack(pady = standardYPadding)

                            #Creates a button
                            addItemButton = ctk.CTkButton(
                                rightFrame,
                                text= "Add Item",
                                font= standardFont,
                                width= standardWidth,
                                height= standardHeight,
                                command= addItem,
                                )
                            addItemButton.pack(pady = standardYPadding)
                        
                        categoryID = categoryName[0]
                        viewStores()


                    #Clear all widgits in left bottom frame, middle frame and right frame
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

                    cursor = connection.cursor()
                    buttonDict = {}
                    data = cursor.execute("SELECT CategoryID,Category FROM Categories").fetchall()
                    for item in data:
                                
                        def action(x = item): 
                            return text_updation(x)

                        category = item[1]

                        buttonDict[item] = ctk.CTkButton(
                        buttonFrame,
                        text= category,
                        font= standardFont,
                        width= 300,
                        height= standardHeight,
                        command=action,
                        )
                        buttonDict[item].pack(pady = 5)


                def adminAccountOptions():

                    def changeSecretQuestionOptions():

                        def updateQuestion():
                            replacementQuestion= questionEntry.get()
                            replacementAnswer= questionAnswerEntry.get()
                            adminAccountSelection= adminAccountsListbox.curselection()
                            if adminAccountSelection:

                                AccountID= adminAccountsListbox.get(adminAccountSelection[0])
                                AccountID= str(AccountID).split(',')[0]

                                if replacementQuestion == '':

                                    if replacementAnswer == '':

                                        #Creates error window
                                        errorWindow= ctk.CTkToplevel(root)
                                        errorWindow.title("Error Window")
                                        errorWindow.geometry("1200x500")
                                        errorWindow.transient(root)
                                        errorWindow.lift()

                                        #Creates a label
                                        errorLabel= ctk.CTkLabel(
                                            errorWindow,
                                            text= "You have not entered the question or the answer",
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
                                    
                                    else:
                                        cursor = connection.cursor()
                                        cursor.execute(f"UPDATE Accounts SET Secret_Question_Answer='{replacementAnswer}' WHERE Admin_AccountID={AccountID}")
                                        connection.commit()
                                        changeSecretQuestionOptions()

                                else:

                                    if replacementAnswer == '':
                                        #Creates error window
                                        errorWindow= ctk.CTkToplevel(root)
                                        errorWindow.title("Error Window")
                                        errorWindow.geometry("1200x500")
                                        errorWindow.transient(root)
                                        errorWindow.lift()

                                        #Creates a label
                                        errorLabel= ctk.CTkLabel(
                                            errorWindow,
                                            text= "You have not entered the answer",
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

                                    else:
                                        cursor = connection.cursor()
                                        cursor.execute(f"UPDATE Accounts SET Secret_Question='{replacementQuestion}' WHERE AccountID={AccountID}")
                                        cursor.execute(f"UPDATE Accounts SET Secret_Question_Answer='{replacementAnswer}' WHERE AccountID={AccountID}")
                                        connection.commit()
                                        changeSecretQuestionOptions()

                            else:
                                #Creates error window
                                errorWindow= ctk.CTkToplevel(root)
                                errorWindow.title("Error Window")
                                errorWindow.geometry("1200x500")
                                errorWindow.transient(root)
                                errorWindow.lift()

                                #Creates a label
                                errorLabel= ctk.CTkLabel(
                                    errorWindow,
                                    text= "You have not selected an account",
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



                        #Clear all widgits in right frame
                        for widgets in rightFrame.winfo_children():
                            widgets.destroy()

                        #Creates a label
                        label= ctk.CTkLabel(rightFrame, text="Select the account you wish to modify \n FORMAT = Admin Account ID, Secret Question, Secret Question Answer", font= standardFont)
                        label.pack(pady = standardYPadding)

                        #Creates a frame
                        listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
                        listboxFrame.pack(pady = standardYPadding)

                        #Create list box and writes the contents of the database into it
                        adminAccountsListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 40, height=10, font= standardFont)
                        cursor = connection.cursor()
                        data = cursor.execute(f"SELECT AccountID,Secret_Question,Secret_Question_Answer FROM Accounts WHERE Account_TypeID = 1").fetchall()
                        formatted_data = []
                        for item in data:
                            AccountID = item[0]
                            secret_Question = item[1]
                            secret_Question_Answer = item[2]
                            formatted_data.append(f"{AccountID}, {secret_Question}, {secret_Question_Answer}")
                        for row in formatted_data:
                            adminAccountsListbox.insert(END, row)
                        adminAccountsListbox.pack(side=LEFT)

                        #Creates a scroll bar
                        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=adminAccountsListbox.yview)
                        listboxScrollbar.pack(side="right", fill=Y)
                        adminAccountsListbox.config(yscrollcommand=listboxScrollbar.set)

                        #Creates an entry box
                        questionEntry = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Enter Replacement Question",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            )
                        questionEntry.pack(pady = standardYPadding)

                        #Creates an entry box
                        questionAnswerEntry = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Enter Replacement Question Answer",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            )
                        questionAnswerEntry.pack(pady = standardYPadding)

                        #Creates a button
                        changeQuantityButton = ctk.CTkButton(
                            rightFrame,
                            text= "Update Quantity",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            command= updateQuestion,
                            )
                        changeQuantityButton.pack(pady = standardYPadding)

                    def changePasswordOptions():

                        def passwordChecker():
                            adminOldPassword= adminAccountOldPassword.get()
                            adminNewPassword= adminAccountNewPassword.get()
                            adminNewPasswordConfirm= adminAccountNewPasswordConfirm.get()

                            if adminOldPassword != adminAccountPassword:
                                #Creates error window
                                errorWindow= ctk.CTkToplevel(root)
                                errorWindow.title("Error Window")
                                errorWindow.geometry("1200x500")
                                errorWindow.transient(root)
                                errorWindow.lift()

                                #Creates a label
                                errorLabel= ctk.CTkLabel(
                                    errorWindow,
                                    text= "The old account password does not much currant password",
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
                                changePasswordOptions

                            else:
                                if adminNewPassword != adminNewPasswordConfirm:
                                    #Creates error window
                                    errorWindow= ctk.CTkToplevel(root)
                                    errorWindow.title("Error Window")
                                    errorWindow.geometry("1200x500")
                                    errorWindow.transient(root)
                                    errorWindow.lift()

                                    #Creates a label
                                    errorLabel= ctk.CTkLabel(
                                        errorWindow,
                                        text= "The new passwords do not match",
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
                                    changePasswordOptions

                                else:
                                    cursor = connection.cursor()
                                    cursor.execute(f"UPDATE Accounts SET Password='{adminNewPasswordConfirm}' WHERE AccountID={AccountID}")
                                    connection.commit()
                                    changePasswordOptions()
                            
                        for widgets in rightFrame.winfo_children():
                            widgets.destroy()

                        #Creates a label
                        label= ctk.CTkLabel(rightFrame, text="Follow the prompts to change the password", font= standardFont)
                        label.pack(pady = standardYPadding)

                        cursor = connection.cursor()
                        data = cursor.execute(f"SELECT AccountID, Password FROM Accounts WHERE Account_TypeID = 1").fetchall()
                        formatted_data = []
                        for item in data:
                            AccountID = item[0]
                            adminAccountPassword = item[1]
                            formatted_data.append(f"{AccountID}, {adminAccountPassword}")

                        #Creates an entry box
                        adminAccountOldPassword = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Enter Old Password",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            show= '*'
                            )
                        adminAccountOldPassword.pack(pady = standardYPadding)

                        #Creates an entry box
                        adminAccountNewPassword = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Enter New Password",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            show= '*'
                            )
                        adminAccountNewPassword.pack(pady = standardYPadding)

                        #Creates an entry box
                        adminAccountNewPasswordConfirm = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Enter New Password Again",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            show= '*'
                            )
                        adminAccountNewPasswordConfirm.pack(pady = standardYPadding)

                        #Creates a button
                        changeQuantityButton = ctk.CTkButton(
                            rightFrame,
                            text= "Update Password",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            command= passwordChecker,
                            )
                        changeQuantityButton.pack(pady = standardYPadding)

                        
                    for widgets in middleFrame.winfo_children():
                        widgets.destroy()
                    for widgets in rightFrame.winfo_children():
                        widgets.destroy()

                    changeSecretQuestion = ctk.CTkButton(
                        middleFrame,
                        text= "Change Secret Question",
                        font= (standardFont),
                        width= standardWidth,
                        height= standardHeight,
                        command=changeSecretQuestionOptions,
                    )
                    changeSecretQuestion.pack(pady = standardYPadding) 

                    changePassword = ctk.CTkButton(
                        middleFrame,
                        text= "Change Password",
                        font= (standardFont),
                        width= standardWidth,
                        height= standardHeight,
                        command=changePasswordOptions,
                    )
                    changePassword.pack(pady = standardYPadding)


                def userAccountOptions():
                    
                    def addUserAccount():
                        
                        def addAccount():
                            rowSelection = namesListListbox.curselection()
                            if rowSelection:
                                rowIndex = rowSelection[0]
                                row = formatted_data[rowIndex]
                                cadetID= str(row).split(" ")[0]
                                firstName= str(row).split(" ")[2]
                                lastName= str(row).split(" ")[3]
                                username= firstName+'_'+lastName
                                accountType= "2"
                                password= passwordEntry.get()
                                confirmedPassword= confirmedPasswordEntry.get()
                                secretQuestion= secretQuestionEntry.get()
                                secretQuestionAnswer= secretQuestionAnswerEntry.get()

                                if confirmedPassword != password:

                                    #Creating an error window
                                    errorWindow= ctk.CTkToplevel(root)
                                    errorWindow.title("Error Window")
                                    errorWindow.geometry("1200x500")
                                    errorWindow.transient(root)
                                    errorWindow.lift()
                                    
                                    #Creating a label
                                    errorLabel= ctk.CTkLabel(
                                        errorWindow,
                                        text= "Passwords do not match",
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

                                else:
                                    if password == "":
                                        if confirmedPassword == "":
                                            if secretQuestion == "":
                                                if secretQuestionAnswer == "":
                                                    #Creating an error window
                                                    errorWindow= ctk.CTkToplevel(root)
                                                    errorWindow.title("Error Window")
                                                    errorWindow.geometry("1200x500")
                                                    errorWindow.transient(root)
                                                    errorWindow.lift()
                                                    
                                                    #Creating a label
                                                    errorLabel= ctk.CTkLabel(
                                                        errorWindow,
                                                        text= "You have left a field empty",
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

                                                else:
                                                    cursor = connection.cursor()
                                                    cursor.execute(f"INSERT INTO Accounts (CadetID, Username, Password, Account_TypeID, Secret_Question, Secret_Question_Answer) VALUES ('{cadetID}','{username}','{password}','{accountType}','{secretQuestion}','{secretQuestionAnswer}')")
                                                    connection.commit()
                                            else:
                                                #Creating an error window
                                                errorWindow= ctk.CTkToplevel(root)
                                                errorWindow.title("Error Window")
                                                errorWindow.geometry("1200x500")
                                                errorWindow.transient(root)
                                                errorWindow.lift()
                                                
                                                #Creating a label
                                                errorLabel= ctk.CTkLabel(
                                                    errorWindow,
                                                    text= "You have left a field empty",
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
                                        else:
                                            #Creating an error window
                                            errorWindow= ctk.CTkToplevel(root)
                                            errorWindow.title("Error Window")
                                            errorWindow.geometry("1200x500")
                                            errorWindow.transient(root)
                                            errorWindow.lift()
                                            
                                            #Creating a label
                                            errorLabel= ctk.CTkLabel(
                                                errorWindow,
                                                text= "You have left a field empty",
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
                                    else:
                                        #Creating an error window
                                        errorWindow= ctk.CTkToplevel(root)
                                        errorWindow.title("Error Window")
                                        errorWindow.geometry("1200x500")
                                        errorWindow.transient(root)
                                        errorWindow.lift()
                                        
                                        #Creating a label
                                        errorLabel= ctk.CTkLabel(
                                            errorWindow,
                                            text= "You have left a field empty",
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

                            else:
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

                        #Creates an entry box
                        passwordEntry = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Please Enter a Password",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            show= '*',
                            )
                        passwordEntry.pack(pady = standardYPadding)

                        #Creates an entry box
                        confirmedPasswordEntry = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Please Enter the Password Again",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            show= '*',
                            )
                        confirmedPasswordEntry.pack(pady = standardYPadding)

                        #Creates an entry box
                        secretQuestionEntry = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Enter A Secret Question",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            )
                        secretQuestionEntry.pack(pady = standardYPadding)

                        #Creates an entry box
                        secretQuestionAnswerEntry = ctk.CTkEntry(
                            rightFrame, 
                            placeholder_text="Enter Secret Question Answer",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            )
                        secretQuestionAnswerEntry.pack(pady = standardYPadding)

                        #Creates a button
                        addAccountButton = ctk.CTkButton(
                            rightFrame,
                            text= "Add Account",
                            font= standardFont,
                            width= 500,
                            height= standardHeight,
                            command= addAccount,
                            )
                        addAccountButton.pack(pady = standardYPadding)

                    def deleteUserAccount():
                        1

                    def changeSecretQuestion():
                        1

                    def changeUsername():
                        1

                    def changePassword():
                        1


                    addUserAccountButton = ctk.CTkButton(
                        middleFrame,
                        text= "Add User Account",
                        font= (standardFont),
                        width= standardWidth,
                        height= standardHeight,
                        command=addUserAccount,
                        )
                    addUserAccountButton.pack(pady = standardYPadding)

                    removeUserAccountButton = ctk.CTkButton(
                        middleFrame,
                        text= "Remove User Account",
                        font= (standardFont),
                        width= standardWidth,
                        height= standardHeight,
                        command=deleteUserAccount,
                        )
                    removeUserAccountButton.pack(pady = standardYPadding)

                    changeSecretQuestionButton = ctk.CTkButton(
                        middleFrame,
                        text= "Change Secret Question",
                        font= (standardFont),
                        width= standardWidth,
                        height= standardHeight,
                        command=changeSecretQuestion,
                        )
                    changeSecretQuestionButton.pack(pady = standardYPadding)

                    changeUsernameButton = ctk.CTkButton(
                        middleFrame,
                        text= "Change Username",
                        font= (standardFont),
                        width= standardWidth,
                        height= standardHeight,
                        command=changeUsername,
                        )
                    changeUsernameButton.pack(pady = standardYPadding)

                    changePasswordButton = ctk.CTkButton(
                        middleFrame,
                        text= "Change Password",
                        font= (standardFont),
                        width= standardWidth,
                        height= standardHeight,
                        command=changePassword,
                        )
                    changePasswordButton.pack(pady = standardYPadding)


                #Creats a ctk button
                removePersonButton = ctk.CTkButton(
                    leftBottomFrame,
                    text= "Remove An AAC Member",
                    font= (standardFont),
                    width= standardWidth,
                    height= standardHeight,
                    command=removeAACMemberOptions,
                    )
                removePersonButton.pack(pady = standardYPadding)

                #Creats a ctk button
                changeIDButton = ctk.CTkButton(
                    leftBottomFrame,
                    text= "Change AAC Member ID",
                    font= (standardFont),
                    width= standardWidth,
                    height= standardHeight,
                    command=changeIDOptions,
                    )
                changeIDButton.pack(pady = standardYPadding)

                #Creats a ctk button
                removeStoresButton = ctk.CTkButton(
                    leftBottomFrame,
                    text= "Remove Stores",
                    font= (standardFont),
                    width= standardWidth,
                    height= standardHeight,
                    command=removeStoreOptions,
                    )
                removeStoresButton.pack(pady = standardYPadding)

                #Creats a ctk button
                addStoresButton = ctk.CTkButton(
                    leftBottomFrame,
                    text= "Add Stores",
                    font= (standardFont),
                    width= standardWidth,
                    height= standardHeight,
                    command=addStoresOptions,
                    )
                addStoresButton.pack(pady = standardYPadding)

                #Creats a ctk button
                adminAcountButton = ctk.CTkButton(
                    leftBottomFrame,
                    text= "Admin Account Options",
                    font= (standardFont),
                    width= standardWidth,
                    height= standardHeight,
                    command=adminAccountOptions,
                    )
                adminAcountButton.pack(pady = standardYPadding)

                #Creats a ctk button
                userAcountButton = ctk.CTkButton(
                    leftBottomFrame,
                    text= "User Account Options",
                    font= (standardFont),
                    width= standardWidth,
                    height= standardHeight,
                    command=userAccountOptions,
                    )
                userAcountButton.pack(pady = standardYPadding)

            def returnToLogin():
                passwordWindow.destroy()
                adminOptions()


            passwords= []
            cursor = connection.cursor()
            data= cursor.execute(f"SELECT Password FROM Accounts WHERE Account_TypeID = 1").fetchall()
            data= str(data).replace('(','').replace(')','').replace(',','').replace("'",'').replace(" ",',').replace("[",'').replace("]",'')
            data=data.split(',')
            for password in data:
                passwords.append(password)
            userEntry= passwordEntry.get()

            if userEntry not in passwords:

                for widgets in passwordWindow.winfo_children():
                    widgets.destroy()

                #Creates a ctk label
                passwordErrorLabel= ctk.CTkLabel(
                    passwordWindow,
                    text= "Incorect password. Return to log in page and try again.",
                    font= standardFont
                    )
                passwordErrorLabel.pack(pady= standardYPadding)

                #Creates a ctk button
                passwordErrorButton= ctk.CTkButton(
                    passwordWindow,
                    text= "Return to Log In Page",
                    font= standardFont,
                    width= standardWidth,
                    height= standardHeight,
                    command= returnToLogin
                    )
                passwordErrorButton.pack(pady= standardYPadding)

            elif userEntry in passwords:
                passwordWindow.destroy()
                succesfulLogIn()

        def forgotPassword():

            def returnToLogin():
                    passwordWindow.destroy()
                    adminOptions()

            def questionChecker():

                def returnToLogin():
                    passwordWindow.destroy()
                    adminOptions()

                adminQuestionAnswer= adminAccountQuestionAnswer.get()

                if adminQuestionAnswer != adminAccountSecretQuestionAnswer:
                    for widgets in passwordWindow.winfo_children():
                        widgets.destroy()

                    #Creates a label
                    errorLabel= ctk.CTkLabel(
                        passwordWindow,
                        text= "Your answer does not match the correct answer",
                        font= standardFont
                        )
                    errorLabel.pack(pady= standardYPadding)

                    #Creates a button
                    errorButton= ctk.CTkButton(
                        passwordWindow,
                        text= "Return to Previous Page",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= forgotPassword
                        )
                    errorButton.pack(pady= standardYPadding)

                else:
                    for widgets in passwordWindow.winfo_children():
                        widgets.destroy()

                    #Creates a ctk label
                    label = ctk.CTkLabel(passwordWindow, text=f"The Password is: \n{adminAccountPassword}", fg_color="transparent", font= standardFont)
                    label.pack(pady = standardYPadding)

                    #Creates a button
                    returnToLoginButton= ctk.CTkButton(
                        passwordWindow,
                        text= "Return to Log In Page",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command= returnToLogin
                        )
                    returnToLoginButton.pack(pady= standardYPadding)
                    


            for widgets in passwordWindow.winfo_children():
                widgets.destroy()

            cursor = connection.cursor()
            data = cursor.execute("SELECT Secret_Question,Secret_Question_Answer,Password FROM Accounts WHERE Account_TypeID = 1").fetchall()
            formatted_data = []
            for item in data:
                adminAccountSecretQuestion = item[0]
                adminAccountSecretQuestionAnswer = item[1]
                adminAccountPassword = item[2]
                formatted_data.append(f"{adminAccountSecretQuestion}, {adminAccountSecretQuestionAnswer}, {adminAccountPassword}")

            #Creates a ctk label
            label = ctk.CTkLabel(passwordWindow, text=f"The secret question is: \n{adminAccountSecretQuestion}", fg_color="transparent", font= standardFont)
            label.pack(pady = standardYPadding)

            #Creates an entry box
            adminAccountQuestionAnswer = ctk.CTkEntry(
                passwordWindow, 
                placeholder_text="Enter the Answer to the Question",
                font= standardFont,
                width= 400,
                height= standardHeight,
                show= '*'
                )
            adminAccountQuestionAnswer.pack(pady = standardYPadding)

            #Creates a button
            questionCheckerButton = ctk.CTkButton(
                passwordWindow,
                text= "Submit Answer",
                font= standardFont,
                width= 400,
                height= standardHeight,
                command= questionChecker,
                )
            questionCheckerButton.pack(pady = standardYPadding)

            #Creates a button
            questionCheckerButton = ctk.CTkButton(
                passwordWindow,
                text= "Return to Log In Page",
                font= standardFont,
                width= 400,
                height= standardHeight,
                command= returnToLogin,
                )
            questionCheckerButton.pack(pady = standardYPadding)

        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates a ctk window
        passwordWindow= ctk.CTkToplevel(root)
        passwordWindow.title("Log In Window")
        passwordWindow.geometry("500x300")
        passwordWindow.transient(root)
        passwordWindow.lift()

        for widgets in passwordWindow.winfo_children():
            widgets.destroy()

        #Creates a ctk label
        passwordLabel= ctk.CTkLabel(
            passwordWindow,
            text= "Please Enter the Admin Pasword",
            font= standardFont
            )
        passwordLabel.pack(pady= standardYPadding)

        #Creates a ctk entry box
        passwordEntry= ctk.CTkEntry(
            passwordWindow,
            placeholder_text="Enter Pasword",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            show= '*'
            )
        passwordEntry.pack(pady= standardYPadding)

        #Creates a ctk button
        passwordButton= ctk.CTkButton(
            passwordWindow,
            text= "Log In",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= logIn
            )
        passwordButton.pack(pady= standardYPadding)

        #Creates a ctk button
        passwordButton= ctk.CTkButton(
            passwordWindow,
            text= "Forgot the Password",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= forgotPassword
            )
        passwordButton.pack(pady= standardYPadding)

        #Creates a ctk button
        passwordButton= ctk.CTkButton(
            passwordWindow,
            text= "Close Window",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= passwordWindow.destroy
            )
        passwordButton.pack(pady= standardYPadding)




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
    adminButton = ctk.CTkButton(
        leftTopFrame,
        text= "Admin Options",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= adminOptions,
        )
    adminButton.pack(pady = standardYPadding)
   
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