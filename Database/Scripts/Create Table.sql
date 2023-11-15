CREATE TABLE "Cadets" (
CadetID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
Rank integer NOT NULL,
First_Name TEXT NOT NULL,
Last_Name TEXT NOT NULL,
Email TEXT UNIQUE not NULL,
Join_Date DATE,
Leave_Date DATE);

CREATE TABLE Categories (
CategoryID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Category TEXT NOT NULL);

CREATE TABLE "Stores" (
StoreID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Name TEXT NOT NULL,
CategoryID INTEGER NOT NULL,
Size TEXT,
Qty INTEGER NOT NULL,
CONSTRAINT Stores_FK FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE "Log_Type" (
Log_TypeID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Name TEXT NOT NULL);

CREATE TABLE "Logs" (
LogID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
CadetID INTEGER NOT NULL,
StoreID INTEGER NOT NULL,
Qty_Taken INTEGER NOT NULL,
Date_Taken DATE NOT NULL DEFAULT (CURRENT_DATE),
Qty_Returned INTEGER,
Date_Returned DATE,
Log_TypeID INTEGER NOT NULL,
CONSTRAINT Logs_FK FOREIGN KEY (CadetID) REFERENCES Cadets(CadetID),
CONSTRAINT Logs_FK_1 FOREIGN KEY (StoreID) REFERENCES Stores(StoreID),
CONSTRAINT Logs_FK_2 FOREIGN KEY (Log_TypeID) REFERENCES Log_Type(Log_TypeID));

CREATE TABLE "Account_Type" (
Account_TypeID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Account_Type_Name TEXT NOT NULL);

CREATE TABLE "Accounts" (
AccountID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
CadetID INTEGER,
Username TEXT NOT NULL,
Password TEXT NOT NULL,
Account_TypeID INTEGER NOT NULL,
Secret_Question TEXT NOT NULL,
Secret_Question_Answer TEXT NOT NULL,
CONSTRAINT Accounts_FK_1 FOREIGN KEY (CadetID) REFERENCES Cadets(CadetID),
CONSTRAINT Accounts_FK_2 FOREIGN KEY (Account_TypeID) REFERENCES Account_Type(Account_TypeID));

CREATE TABLE "ActionsLogs" (
LogID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
AccountID INTEGER NOT NULL,
Date DATE NOT NULL,
Action TEXT NOT NULL,
CONSTRAINT ActionsLogs_FK_1 FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID));

