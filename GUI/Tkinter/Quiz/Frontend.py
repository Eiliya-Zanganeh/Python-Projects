from tkinter import *
import tkinter.messagebox
import random
import Backend

window = Tk()
window.title("Quiz Word")
window.resizable(width=False, height=False)
#============================= Values ===========================================
word = StringVar()
main = StringVar()
#============================= Label and Entry ==================================

label1 = Label(window, text="Word")
label1.grid(row=0, column=0)
entry1 = Entry(window, textvariable=word)
entry1.grid(row=0 , column=1)

label2 = Label(window, text="Main")
label2.grid(row=0, column=2)
entry2 = Entry(window, textvariable=main)
entry2.grid(row=0 , column=3)

label3 = Label(window, text="***Eiliya Zanganeh***", foreground="red")
label3.grid(row=6, column=3)

label4 = Label(window, text="Question")
label4.grid(row=1, column=4)

label5 = Label(window, text="Dictionary setting ")
label5.grid(row=1, column=0)

listbox = Listbox(window, width=35, height=8)
listbox.grid(row=1, column=0, rowspan=5, columnspan=5)
scrollbar = Scrollbar(window)
scrollbar.grid(row=1, column=3, rowspan=5,  columnspan=1)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

def get_selected_item(event):
    try:
        global select_listbox
        index = listbox.curselection()[0]
        select_listbox: listbox.get(index)
        entry1.delete(0,END)
        entry1.insert(END, select_listbox[1])
        entry2.delete(0,END)
        entry2.insert(END, select_listbox[2])
    except:
        pass

listbox.bind("<<ListboxSelect>>", get_selected_item)

#=====================================Quiz functions================================================
word = []
main = []

def get_all_word():
    word.clear()
    main.clear()
    for num in (Backend.view()):
        word.append(num[1])
        main.append(num[2])

def quiz_word():
    global indexwordq
    global wordq
    global bool
    bool = True
    get_all_word()
    listbox.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    lenword = ((len(word)) - 1)
    indexwordq = (random.randint(0, lenword))
    wordq = word[indexwordq]
    entry1.insert(END, wordq)


def quiz_main():
    global indexmainq
    global mainq
    global bool
    bool = False
    get_all_word()
    listbox.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    lenmain = ((len(main)) - 1)
    indexmainq = (random.randint(0, lenmain))
    mainq = main[indexmainq]
    entry2.insert(END, mainq)

def main_quiz():
    global wordq
    global mainq
    if (bool):
        try:
            mainq = main[indexwordq]
            if (str(entry2.get())) == mainq:
                listbox.delete(0, END)
                listbox.insert(END, "True")
            else:
                listbox.delete(0, END)
                listbox.insert(END, f"False main {wordq} is {mainq}")
        except:
            tkinter.messagebox.showerror("Error", "you don't select Question for answer")

    else:
        try:
            wordq = word[indexmainq]
            if (str(entry1.get())) == wordq:
                listbox.delete(0, END)
                listbox.insert(END, "True")
            else:
                listbox.delete(0, END)
                listbox.insert(END, f"False word {mainq} is {wordq}")
        except:
            tkinter.messagebox.showerror("Error", "you don't select Question for answer")




#============================= Button and Function =========================================

def view_all_word():
    listbox.delete(0, END)
    words = Backend.view()
    for num in words:
        listbox.insert(END, num)

def serch_word():
    if (entry1.get() or entry2.get()) == "":
        tkinter.messagebox.showerror("Error", "The wordbox or mainbox don't have any item")
    else:
        listbox.delete(0, END)
        words = Backend.serch(entry1.get(), entry2.get())

        if words == []:
            tkinter.messagebox.showerror("Error", f"the{entry1.get()} {entry2.get()} not existed ")
        else:
            for num in words:
                listbox.insert(END, num)

def add_new_word():
    if ((entry1.get() == "") or (entry2.get()) == ""):
        tkinter.messagebox.showerror("Error", "The wordbox or mainbox don't have any item")
    else:
        get_all_word()
        if ((entry1.get()) in word) and ((entry2.get()) in main):
            listbox.delete(0, END)
            words = Backend.serch(entry1.get(), entry2.get())
            for num in words:
                    listbox.insert(END, num)
            tkinter.messagebox.showerror("Error", "Word and main existed")
        elif (entry1.get()) in word:
            listbox.delete(0, END)
            words = Backend.serch(entry1.get(), entry2.get())
            for num in words:
                    listbox.insert(END, num)
            tkinter.messagebox.showerror("Error", "Word existed")
        elif (entry2.get()) in main:
            listbox.delete(0, END)
            words = Backend.serch(entry1.get(), entry2.get())
            for num in words:
                    listbox.insert(END, num)
            tkinter.messagebox.showerror("Error", "main existed")
        else:
            listbox.delete(0, END)
            Backend.insert(entry1.get(), entry2.get())
            listbox.insert(END, (entry1.get(), entry2.get()))

def update_word():
    if ((entry1.get() == "") or (entry2.get()) == ""):
        tkinter.messagebox.showerror("Error", "The wordbox or mainbox don't have any item")
    else:
        get_all_word()
        try:
            word.remove(select_listbox[1])
            main.remove(select_listbox[2])
        except:
            pass

        if ((entry1.get()) in word) and ((entry2.get()) in main):
            listbox.delete(0, END)
            words = Backend.serch(entry1.get(), entry2.get())
            for num in words:
                listbox.insert(END, num)
            tkinter.messagebox.showerror("Error", "Word and main existed")
        elif (entry1.get()) in word:
            listbox.delete(0, END)
            words = Backend.serch(entry1.get(), entry2.get())
            for num in words:
                listbox.insert(END, num)
            tkinter.messagebox.showerror("Error", "Please select one item in list box or Word existed")
        elif (entry2.get()) in main:
            listbox.delete(0, END)
            words = Backend.serch(entry1.get(), entry2.get())
            for num in words:
                listbox.insert(END, num)
            tkinter.messagebox.showerror("Error", "Please select one item in list box or main existed")
        else:
            try:
                Backend.update(select_listbox[0],entry1.get(), entry2.get())
                view_all_word()
            except:
                tkinter.messagebox.showerror("Error", "Please select one word in list box")

def delete_word():
    try:
        Backend.delete(select_listbox[0])
        view_all_word()
    except:
        tkinter.messagebox.showerror("Error", "Please select one word in list box")

x = 0
while(True):
    x += 1








def help():
    global n
    n = Tk()
    n.title("Help")
    n.resizable(width=False, height=False)



    n0 = Label(n, text="راهنمای کلید های تنظیمات دیکشنری کلمات")
    n0.grid(row=0)

    n1 = Label(n, text=" برای دیدن تمام کلمات ذخیره شده"
                      " : View all word")
    n1.grid(row=1)
    n2 = Label(n, text=" برای پیدا کردن مورد نظر، توجه داشته باشید که نخست باید کلمه یا معنی مورد نظر را در کادر های مشخص شده وارد کنید"
                      " : Serch word ")
    n2.grid(row=2)
    n3 = Label(n, text="برای اضافه کردن کلمه جدید، برای این کار باید نخست کلمه و معنی جدید را در کادر مشخص شده وارد کنید"
                      " : Add new word")
    n3.grid(row=3)
    n4 = Label(n,foreground="red", text=" توجه داشته باشید که کلمه یا معنی که قبلا از آن استفاده کرده اید را نمی توانید دوباره اضافه کنید")
    n4.grid(row=4)
    n5 = Label(n, text="برای ویرایش کلمه، نخست باید کلمه مورد نظر را از لیست کلمات انتخاب کنید"
                      " : Update word")
    n5.grid(row=5)
    n6 = Label(n, text=" و در کادر های مشخص شده ویرایش را انجام دهید")
    n6.grid(row=6)
    n7 = Label(n,foreground="red", text=" توجه داشته باشید که مثل اضافه کردن کلمه جدید نمی توانید کلمه را طوری ویرایش کنید که")
    n7.grid(row=7)
    n8 = Label(n, foreground="red", text=" خود کلمه یا معنی در لیست کلمه ها وجود داشته باشد")
    n8.grid(row=8)
    n9 = Label(n, text="برای حذف کردن آیتم دلخواه از لیست کلمات"
                       " : Delete word")
    n9.grid(row=9)

    n10 = Label(n, text="")
    n10.grid(row=10)

    n11 = Label(n, text="راهنمای کلید های آزمون کلمات")
    n11.grid(row=11)
    n12 = Label(n, text="برای ایجاد سوال از کلمات"
                        " : Word")
    n12.grid(row=12)
    n13 = Label(n, text="برای ایجاد سوال از معانی"
                        " : Main")
    n13.grid(row=13)
    n14 = Label(n, text="برای تایید جواب"
                        " : Answer")
    n14.grid(row=14)

    n15 = Label(n, text="")
    n15.grid(row=15)

    n16 = Label(n, text=" : شیوه آزمون دادن")
    n16.grid(row=16)
    n17 = Label(n, text="(Word) نخست اگر می خواهید سوال از کلمات باشد بر روی گزینه")
    n17.grid(row=17)
    n18 = Label(n, text="کلیک کنید")
    n18.grid(row=18)
    n19 = Label(n, text="(Main) و یا اگر می خواهید سوال از معانی باشد بر روی گزینه")
    n19.grid(row=19)
    n20 = Label(n, text="کلیک کنید")
    n20.grid(row=20)
    n21 = Label(n, text="(Answer) بعد پاسخ را در جای خالی وارد کرده و بر روی گزینه ")
    n21.grid(row=21)
    n22 = Label(n, text="کلیک کنید")
    n22.grid(row=22)
    n23 = Label(n, text="در انتها سیستم پاسخ شما را برسی خواهد کرد و در لیست کلمات درستی یا نادرستی جواب را بر می گرداند")
    n23.grid(row=23)
    exit = Button(n, text="Exit", width=10, bg="gray", command=n.destroy)
    exit.place(x=5, y=450)




def close():
    window.destroy()
    try:
       n.destroy()
    except:
        pass












button1 = Button(window,text="View all word", width=10, bg="gray", command=lambda : view_all_word())
button1.grid(row=2, column=0)
button2 = Button(window,text="Serch word", width=10, bg="gray", command=lambda :serch_word())
button2.grid(row=3, column=0)
button3 = Button(window,text="Add new word", width=10, bg="gray", command=lambda : add_new_word())
button3.grid(row=4, column=0)
button4 = Button(window,text="Update word", width=10, bg="gray", command=lambda : update_word())
button4.grid(row=5, column=0)
button5 = Button(window,text="Delete word", width=10, bg="gray", command=lambda : delete_word())
button5.grid(row=6, column=0)
button6 = Button(window,text="Close", width=10, bg="gray", command=lambda : close())
button6.grid(row=6, column=4)
button7 = Button(window,text="Help", width=10, bg="gray", command=lambda : help())
button7.grid(row=6, column=1)



newbutton = Button(window,text="Word", width=10, bg="gray", comman=lambda : quiz_word())
newbutton.grid(row=2, column=4)

newbutton2 = Button(window,text="Main", width=10, bg="gray", comman=lambda : quiz_main() )
newbutton2.grid(row=3, column=4)

newbutton1 = Button(window,text="Answer", width=10, bg="gray", comman=lambda : main_quiz())
newbutton1.grid(row=4, column=4)







view_all_word()
window.mainloop()


#pyinstaller --onefile --windowed Frontend.py