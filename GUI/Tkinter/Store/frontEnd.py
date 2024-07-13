from . import backEnd

from tkinter import *
import tkinter.messagebox


#==========================  function for Menu button  ===============================


def View_all_personnel():
    listbox_for_list_of_personnel.delete(0, END)
    all_personnel = backEnd.View_personnel()
    for num in all_personnel:
        listbox_for_list_of_personnel.insert(END, num)

####################################################################################################
####################################################################################################

def Serch_personnel():
    #==========================   Serch Menu settings  ===============================
    Serch_personnel = Tk()
    Serch_personnel.title("Serch personnel")
    Serch_personnel.geometry("350x130")
    #==========================  labels in Serch Menu  ===============================
    label_for_name_personnel_Entry = Label(Serch_personnel, text="Enter name of personnel")
    label_for_name_personnel_Entry.place(y=0, x=1)

    label_for_lastName_personnel_Entry = Label(Serch_personnel, text="Enter last name of personnel")
    label_for_lastName_personnel_Entry.place(y=30, x=1)

    label_for_nationalCode_personnel_Entry= Label(Serch_personnel, text="Enter national code of personnel")
    label_for_nationalCode_personnel_Entry.place(y=60, x=1)

    #==========================  Entry in Serch Menu  ===============================

    Name = StringVar()
    lastName = StringVar()
    nationalCode = StringVar()


    Entry_name_personnel = Entry(Serch_personnel, textvariable=Name)
    Entry_name_personnel.place(y=1, x=220)

    Entry_lastName_personnel = Entry(Serch_personnel, textvariable=lastName)
    Entry_lastName_personnel.place(y=30, x=220)

    Entry_nationalCode_personnel = Entry(Serch_personnel, textvariable=nationalCode)
    Entry_nationalCode_personnel.place(y=60, x=220)

    #==========================  function for button Serch Menu  ===============================

    def serch():
        listbox_for_list_of_personnel.delete(0, END)
        all_personnel = backEnd.serchPersonnel(Entry_name_personnel.get(), Entry_lastName_personnel.get(), Entry_nationalCode_personnel.get())
        for num in all_personnel:
           listbox_for_list_of_personnel.insert(END, num)

    #==========================  Button in Serch Menu  ===============================

    Send_information_personnel_Button = Button(Serch_personnel,text="OK", width=10, bg="gray", command=lambda : serch())
    Send_information_personnel_Button.place(y=100, x=135)


    Serch_personnel.mainloop()

####################################################################################################
####################################################################################################

def Add_new_personnel():
    #==========================   Add new personnel Menu settings  ===============================
    Add_new_personnel = Tk()
    Add_new_personnel.title("Add new personnel")
    Add_new_personnel.geometry("350x130")
    #==========================  labels in Add new personnel Menu  ===============================
    label_for_name_personnel_Entry = Label(Add_new_personnel, text="Enter name of personnel")
    label_for_name_personnel_Entry.place(y=0, x=1)

    label_for_lastName_personnel_Entry = Label(Add_new_personnel, text="Enter last name of personnel")
    label_for_lastName_personnel_Entry.place(y=30, x=1)

    label_for_nationalCode_personnel_Entry= Label(Add_new_personnel, text="Enter national code of personnel")
    label_for_nationalCode_personnel_Entry.place(y=60, x=1)

    #==========================  Entry in Add new personnel Menu  ===============================

    Name = StringVar()
    lastName = StringVar()
    nationalCode = StringVar()


    Entry_for_Enter_name_personnel = Entry(Add_new_personnel, textvariable=Name)
    Entry_for_Enter_name_personnel.place(y=1, x=220)

    Entry_for_Enter_lastName_personnel = Entry(Add_new_personnel, textvariable=lastName)
    Entry_for_Enter_lastName_personnel.place(y=30, x=220)

    Entry_for_Enter_nationalCode_personnel = Entry(Add_new_personnel, textvariable=nationalCode)
    Entry_for_Enter_nationalCode_personnel.place(y=60, x=220)

    #==========================  function for button Add new personnel Menu  ===============================

    def Add_personnel(Name, lastName ,nationalCode):
        new_personnel = backEnd.personnel(Entry_for_Enter_name_personnel.get(), Entry_for_Enter_lastName_personnel.get(), Entry_for_Enter_nationalCode_personnel.get())
        new_personnel.Add_new()
        Entry_for_Enter_name_personnel.delete(0, END)
        Entry_for_Enter_lastName_personnel.delete(0, END)
        Entry_for_Enter_nationalCode_personnel.delete(0, END)
        View_all_personnel()

    #==========================  Button in Add new personnel Menu  ===============================

    Send_information_personnel_Button = Button(Add_new_personnel,text="OK", width=10, bg="gray", command=lambda : Add_personnel(Name, lastName, nationalCode))
    Send_information_personnel_Button.place(y=100, x=135)


    Add_new_personnel.mainloop()

####################################################################################################
####################################################################################################

def editPersonnel():
    try:
        #==========================   Edit personnel Menu settings  ===============================
        Edit_personnel = Tk()
        Edit_personnel.title("Edit personnel")
        Edit_personnel.geometry("350x130")
        #==========================  labels in Edit personnel Menu  ===============================
        label_for_name_personnel_Entry = Label(Edit_personnel, text="Enter name of personnel")
        label_for_name_personnel_Entry.place(y=0, x=1)

        label_for_lastName_personnel_Entry = Label(Edit_personnel, text="Enter last name of personnel")
        label_for_lastName_personnel_Entry.place(y=30, x=1)

        label_for_nationalCode_personnel_Entry= Label(Edit_personnel, text="Enter national code of personnel")
        label_for_nationalCode_personnel_Entry.place(y=60, x=1)

        #==========================  Entry in Edit personnel Menu  ===============================

        Name = StringVar()
        lastName = StringVar()
        nationalCode = StringVar()


        Entry_for_Enter_name_personnel = Entry(Edit_personnel, textvariable=Name)
        Entry_for_Enter_name_personnel.place(y=1, x=220)

        Entry_for_Enter_lastName_personnel = Entry(Edit_personnel, textvariable=lastName)
        Entry_for_Enter_lastName_personnel.place(y=30, x=220)

        Entry_for_Enter_nationalCode_personnel = Entry(Edit_personnel, textvariable=nationalCode)
        Entry_for_Enter_nationalCode_personnel.place(y=60, x=220)

        Entry_for_Enter_name_personnel.insert(END, selected_row[1])
        Entry_for_Enter_lastName_personnel.insert(END, selected_row[2])
        Entry_for_Enter_nationalCode_personnel.insert(END, selected_row[3])


        #==========================  function for button Edit personnel Menu  ===============================

        def edit():
            personnel = backEnd.personnel(Entry_for_Enter_name_personnel.get(), Entry_for_Enter_lastName_personnel.get(), Entry_for_Enter_nationalCode_personnel.get())
            personnel.Edit_personnel(selected_row[0])
            listbox_for_list_of_personnel.delete(0, END)
            new_edit_personnel = backEnd.serchPersonnel(Entry_for_Enter_name_personnel.get(), Entry_for_Enter_lastName_personnel.get(), Entry_for_Enter_nationalCode_personnel.get())
            for num in new_edit_personnel:
                listbox_for_list_of_personnel.insert(0, num)
            Edit_personnel.destroy()


        #==========================  Button in Edit personnel Menu  ===============================

        Send_information_personnel_Button = Button(Edit_personnel,text="OK", width=10, bg="gray",command= lambda : edit())
        Send_information_personnel_Button.place(y=100, x=135)


        Edit_personnel.mainloop()
    except:
        Edit_personnel.destroy()
        tkinter.messagebox.showerror("Error", "Please first select item !")

####################################################################################################
####################################################################################################

def deletePersonnel():
    try:
        backEnd.delete(selected_row[0])
        View_all_personnel()
    except:
        tkinter.messagebox.showerror("Error", "Please first select item !")


####################################################################################################
####################################################################################################

def View_all_object():
    listbox_for_list_of_object.delete(0, END)
    all_object = backEnd.View_object()
    for num in all_object:
        listbox_for_list_of_object.insert(END, num)

####################################################################################################
####################################################################################################

def Serch_object():
    #==========================   Serch Menu settings  ===============================
    Serch_object = Tk()
    Serch_object.title("Serch object")
    Serch_object.geometry("350x150")
    #==========================  labels in Serch Menu  ===============================
    label_for_name_object_Entry = Label(Serch_object, text="Enter name of object")
    label_for_name_object_Entry.place(y=0, x=1)

    label_for_type_of_object_Entry = Label(Serch_object, text="Enter type of object")
    label_for_type_of_object_Entry.place(y=30, x=1)

    label_for_price_of_object_Entry= Label(Serch_object, text="Enter price of object")
    label_for_price_of_object_Entry.place(y=60, x=1)

    label_for_number_of_object_Entry= Label(Serch_object, text="Enter number of object")
    label_for_number_of_object_Entry.place(y=90, x=1)

    #==========================  Entry in Serch Menu  ===============================

    Name = StringVar()
    Type_of_object = StringVar()
    price = StringVar()
    number = StringVar()


    Entry_name_object = Entry(Serch_object, textvariable=Name)
    Entry_name_object.place(y=1, x=220)

    Entry_type_of_object = Entry(Serch_object, textvariable=Type_of_object)
    Entry_type_of_object.place(y=30, x=220)

    Entry_price_of_object = Entry(Serch_object, textvariable=price)
    Entry_price_of_object.place(y=60, x=220)

    Entry_number_of_object = Entry(Serch_object, textvariable=number)
    Entry_number_of_object.place(y=90, x=220)

    #==========================  function for button Serch Menu  ===============================

    def serch():
        listbox_for_list_of_object.delete(0, END)
        all_object = backEnd.serchObject(Entry_name_object.get(), Entry_type_of_object.get(), Entry_price_of_object.get(), Entry_number_of_object.get())
        for num in all_object:
           listbox_for_list_of_object.insert(END, num)

    #==========================  Button in Serch Menu  ===============================

    Send_information_object_Button = Button(Serch_object,text="OK", width=10, bg="gray", command=lambda : serch())
    Send_information_object_Button.place(y=120, x=135)


    Serch_object.mainloop()


####################################################################################################
####################################################################################################

def Add_object():
    #==========================   Add new object Menu settings  ===============================
    Add_object = Tk()
    Add_object.title("Add object")
    Add_object.geometry("350x150")
    #==========================  labels in Add new object Menu  ===============================
    label_for_name_object_Entry = Label(Add_object, text="Enter name of object")
    label_for_name_object_Entry.place(y=0, x=1)

    label_for_type_of_object_Entry = Label(Add_object, text="Enter type of object")
    label_for_type_of_object_Entry.place(y=30, x=1)

    label_for_price_of_object_Entry= Label(Add_object, text="Enter price of object")
    label_for_price_of_object_Entry.place(y=60, x=1)

    label_for_number_of_object_Entry= Label(Add_object, text="Enter number of object")
    label_for_number_of_object_Entry.place(y=90, x=1)

    #==========================  Entry in Add new object Menu  ===============================

    Name = StringVar()
    Type_of_object = StringVar()
    price = StringVar()
    number = StringVar()


    Entry_name_object = Entry(Add_object, textvariable=Name)
    Entry_name_object.place(y=1, x=220)

    Entry_type_of_object = Entry(Add_object, textvariable=Type_of_object)
    Entry_type_of_object.place(y=30, x=220)

    Entry_price_of_object = Entry(Add_object, textvariable=price)
    Entry_price_of_object.place(y=60, x=220)

    Entry_number_of_object = Entry(Add_object, textvariable=number)
    Entry_number_of_object.place(y=90, x=220)

    #==========================  function for button Add new object Menu  ===============================

    def Add_new_object():
        new_object = backEnd.object(Entry_name_object.get(), Entry_type_of_object.get(), Entry_price_of_object.get(), Entry_number_of_object.get())
        new_object.Add_new_object()
        Entry_name_object.delete(0, END)
        Entry_type_of_object.delete(0, END)
        Entry_price_of_object.delete(0, END)
        Entry_number_of_object.delete(0, END)
        View_all_object()

    #==========================  Button in Add new object Menu  ===============================

    Send_information_object_Button = Button(Add_object,text="OK", width=10, bg="gray", command=lambda : Add_new_object())
    Send_information_object_Button.place(y=120, x=135)


    Add_object.mainloop()

####################################################################################################
####################################################################################################

def Edit_object():
    try:
            
            #==========================   Edit Menu settings  ===============================
            Edit_object = Tk()
            Edit_object.title("Edit object")
            Edit_object.geometry("350x150")
            #==========================  labels in Edit Menu  ===============================
            label_for_name_object_Entry = Label(Edit_object, text="Enter name of object")
            label_for_name_object_Entry.place(y=0, x=1)

            label_for_type_of_object_Entry = Label(Edit_object, text="Enter type of object")
            label_for_type_of_object_Entry.place(y=30, x=1)

            label_for_price_of_object_Entry= Label(Edit_object, text="Enter price of object")
            label_for_price_of_object_Entry.place(y=60, x=1)

            label_for_number_of_object_Entry= Label(Edit_object, text="Enter number of object")
            label_for_number_of_object_Entry.place(y=90, x=1)

            #==========================  Entry in Edit Menu  ===============================

            Name = StringVar()
            Type_of_object = StringVar()
            price = StringVar()
            number = StringVar()


            Entry_name_object = Entry(Edit_object, textvariable=Name)
            Entry_name_object.place(y=1, x=220)
            Entry_name_object.insert(END, selected_object[1])

            Entry_type_of_object = Entry(Edit_object, textvariable=Type_of_object)
            Entry_type_of_object.place(y=30, x=220)
            Entry_type_of_object.insert(END, selected_object[2])

            Entry_price_of_object = Entry(Edit_object, textvariable=price)
            Entry_price_of_object.place(y=60, x=220)
            Entry_price_of_object.insert(END, selected_object[3])

            Entry_number_of_object = Entry(Edit_object, textvariable=number)
            Entry_number_of_object.place(y=90, x=220)
            Entry_number_of_object.insert(END, selected_object[4])

            #==========================  function for button Edit Menu  ===============================

            def editObject():
                objects = backEnd.object(Entry_name_object.get(), Entry_type_of_object.get(), Entry_price_of_object.get(), Entry_number_of_object.get())
                objects.Edit_object(selected_object[0])
                listbox_for_list_of_object.delete(0, END)
                new_edit_object = backEnd.serchObject(Entry_name_object.get(), Entry_type_of_object.get(), Entry_price_of_object.get(), Entry_number_of_object.get())
                for num in new_edit_object:
                    listbox_for_list_of_object.insert(0, num)
                Edit_object.destroy()

            #==========================  Edit in Serch Menu  ===============================

            Send_information_object_Button = Button(Edit_object,text="OK", width=10, bg="gray", command=lambda : editObject())
            Send_information_object_Button.place(y=120, x=135)


            Edit_object.mainloop()
    except:
            Edit_object.destroy()
            tkinter.messagebox.showerror("Error", "Please first select item !")

####################################################################################################
####################################################################################################

def deleteObject():
    try:
        backEnd.deleteObject(selected_object[0])
        View_all_object()
    except:
        tkinter.messagebox.showerror("Error", "Please first select item !")


####################################################################################################
####################################################################################################








#==========================  Menu settings  ===============================

mainMenu = Tk()
mainMenu.title("stock clerk")
mainMenu.geometry("1920x1080")
#mainMenu.resizable(width=False, height=False)

#==========================  labels in Menu  ===============================


label_for_personnel_listbox = Label(mainMenu, text="list of personnel")
label_for_personnel_listbox.place(y=1, x=260)

label_for_object_listbox = Label(mainMenu, text="list of object")
label_for_object_listbox.place(y=1 ,x=1085)

#==========================  listboxes in Menu  ===============================

listbox_for_list_of_personnel = Listbox(mainMenu, width=110, height=40)
listbox_for_list_of_personnel.place(y=25, x=1)

listbox_for_list_of_object = Listbox(mainMenu, width=110, height=40)
listbox_for_list_of_object.place(y=25, x=770)

#==========================  scrollbar in Menu  ===============================

scrollbar_for_personnel_listbox = Scrollbar(mainMenu)
scrollbar_for_personnel_listbox.place(y=320, x=710)

scrollbar_for_object_listbox = Scrollbar(mainMenu)
scrollbar_for_object_listbox.place(y=320, x=1475)

#==========================  set scrollbar for listbox   ===============================

listbox_for_list_of_personnel.configure(yscrollcommand=scrollbar_for_personnel_listbox.set)
scrollbar_for_personnel_listbox.configure(command=listbox_for_list_of_personnel.yview)
def get_selected_item(event):
    try:
        global selected_row
        index = listbox_for_list_of_personnel.curselection()[0]
        selected_row = listbox_for_list_of_personnel.get(index)
    except:
        pass

listbox_for_list_of_personnel.bind("<<ListboxSelect>>", get_selected_item)


listbox_for_list_of_object.configure(yscrollcommand=scrollbar_for_object_listbox.set)
scrollbar_for_object_listbox.configure(command=listbox_for_list_of_object.yview)
def get_selected_object(event):
    try:
        global selected_object
        index = listbox_for_list_of_object.curselection()[0]
        selected_object = listbox_for_list_of_object.get(index)
    except:
        pass

listbox_for_list_of_object.bind("<<ListboxSelect>>", get_selected_object)

#==========================  button in Menu  ===============================

View_all_personnel_button = Button(mainMenu,text="View all personnel", width=20, bg="gray", command=lambda : View_all_personnel())
View_all_personnel_button.place(y=700, x=130)

Serch_personnel_button = Button(mainMenu,text="Serch personnel", width=20, bg="gray", command=lambda : Serch_personnel())
Serch_personnel_button.place(y=700, x=385)

Add_new_personnel_button = Button(mainMenu,text="Add new personnel", width=20, bg="gray", command=lambda : Add_new_personnel())
Add_new_personnel_button.place(y=750, x=1)

Edit_personnel_button = Button(mainMenu,text="Edit personnel", width=20, bg="gray", command=lambda : editPersonnel())
Edit_personnel_button.place(y=750, x=255)

Delete_personnel_button = Button(mainMenu,text="Delete personnel", width=20, bg="gray", command= lambda : deletePersonnel())
Delete_personnel_button.place(y=750, x=515)

View_all_object_button = Button(mainMenu,text="View all object", width=20, bg="gray", command=lambda : View_all_object())
View_all_object_button.place(y=700, x=895)

Serch_object_button = Button(mainMenu,text="Serch object", width=20, bg="gray", command=lambda : Serch_object())
Serch_object_button.place(y=700, x=1150)

Add_new_object_button = Button(mainMenu,text="Add new object", width=20, bg="gray", command=lambda : Add_object())
Add_new_object_button.place(y=750, x=770)

Edit_object_button = Button(mainMenu,text="Edit object", width=20, bg="gray", command=lambda : Edit_object())
Edit_object_button.place(y=750, x=1020)

Delete_object_button = Button(mainMenu,text="Delete personnel", width=20, bg="gray", command=lambda : deleteObject())
Delete_object_button.place(y=750, x=1280)



View_all_personnel()
View_all_object()
mainMenu.mainloop()

x = 0
while(True):
    x+= 1
    print(x)