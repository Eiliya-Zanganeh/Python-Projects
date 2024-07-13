import sqlite3




def connect_to_dataBace():
    connect = sqlite3.connect("stock clerk.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS personnel (id INTEGER PRIMARY KEY, Name text, lastName text, nationalCode INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS object (id INTEGER PRIMARY KEY, Name_of_object text, Type_of_object text, Price_of_object INTEGER, Number_of_object INTEGER)")
    connect.commit()
    connect.close()

#=============================  Function of table personnel in dataBace  =======================================

def View_all_personnel():
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("SELECT * FROM personnel")
    row_of_personnel = cursor.fetchall()
    connent.close()
    return row_of_personnel

def Serch_personnel(Name="", lastName="", nationalCode=""):
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("SELECT * FROM personnel WHERE Name=? OR lastName=? OR nationalCode=?", (Name, lastName, nationalCode))
    row_of_personnel = cursor.fetchall()
    connent.close()
    return row_of_personnel

def Add_new_personnel(Name, lastName, nationalCode):
    connent = sqlite3.connect("stock clerk.db")
    cursor =  connent.cursor()
    cursor.execute("INSERT INTO personnel VALUES (NULL, ?, ?, ?) ", (Name, lastName, nationalCode))
    connent.commit()
    connent.close()

def Edit_personnel(id, Name, lastName, nationalCode):
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("UPDATE personnel SET Name=?, lastName=?, nationalCode=?  WHERE id=?", (Name, lastName, nationalCode, id))
    connent.commit()
    connent.close()

def Delete_personnel(id):
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("DELETE FROM personnel WHERE id=?", (id,))
    connent.commit()
    connent.close()

#=============================  Function of table object in dataBace  =======================================

def View_all_object():
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("SELECT * FROM object")
    row_of_object = cursor.fetchall()
    connent.close()
    return row_of_object

def Serch_object(Name_of_object ="", Type_of_object="", Price_of_object="", Number_of_object=""):
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("SELECT * FROM object WHERE Name_of_object=? OR Type_of_object=? OR Price_of_object=? OR Number_of_object=?", (Name_of_object, Type_of_object, Price_of_object, Number_of_object))
    row_of_object = cursor.fetchall()
    connent.close()
    return row_of_object

def Add_new_object(Name_of_object, Type_of_object, Price_of_object, Number_of_object):
    connent = sqlite3.connect("stock clerk.db")
    cursor =  connent.cursor()
    cursor.execute("INSERT INTO object VALUES (NULL, ?, ?, ?, ?) ", (Name_of_object, Type_of_object, Price_of_object, Number_of_object))
    connent.commit()
    connent.close()

def Edit_object(id ,Name_of_object, Type_of_object, Price_of_object, Number_of_object):
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("UPDATE object SET Name_of_object=?, Type_of_object=?, Price_of_object=?, Number_of_object=?  WHERE id=?", (Name_of_object, Type_of_object, Price_of_object, Number_of_object, id))
    connent.commit()
    connent.close()

def Delete_object(id):
    connent = sqlite3.connect("stock clerk.db")
    cursor = connent.cursor()
    cursor.execute("DELETE FROM object WHERE id=?", (id,))
    connent.commit()
    connent.close()




connect_to_dataBace()