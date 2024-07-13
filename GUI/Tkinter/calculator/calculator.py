from tkinter import *


#====================== settings =========================
root = Tk()
root.geometry("400x200")
root.title("calculator")
root.resizable(width=False, height=False)
root.configure(bg="gray")

#====================== variable =========================

num1 = StringVar()
num2 = StringVar()
result = StringVar()

#====================== function =========================

def sum1 ():
    try:
        result.set((float(num1.get())) + (float(num2.get())))
    except:
        result.set("Error")
def sum2 ():
    try:
        result.set((float(num1.get())) - (float(num2.get())))
    except:
        result.set("Error")
def sum3 ():
    try:
        result.set((float(num1.get())) * (float(num2.get())))
    except:
        result.set("Error")
def sum4 ():
    try:
        result.set((float(num1.get())) / (float(num2.get())))
    except:
        result.set("Error")

#====================== frames =========================

frames1 = Frame(root,width=400, height=50, bg=("gray"))
frames1.pack(side=TOP)
frames2 = Frame(root,width=400, height=50, bg=("gray"))
frames2.pack(side=TOP)
frames3 = Frame(root,width=400, height=50, bg=("gray"))
frames3.pack(side=TOP)
frames4 = Frame(root,width=400, height=50, bg=("gray"))
frames4.pack(side=TOP)

#====================== button =========================

button1 = Button(frames3,text="+", width=10, highlightcolor="gray", command=lambda :sum1())
button1.pack(side=LEFT, padx=10, pady=10)
button2 = Button(frames3,text="-", width=10, highlightcolor="gray", command=lambda :sum2())
button2.pack(side=LEFT, padx=10, pady=10)
button3 = Button(frames3,text="*", width=10, highlightcolor="gray", command=lambda :sum3())
button3.pack(side=LEFT, padx=10, pady=10)
button4 = Button(frames3,text="/", width=10, highlightcolor="gray", command=lambda :sum4())
button4.pack(side=LEFT, padx=10, pady=10)

#====================== label and entries =========================

label1 = Label(frames1, text="Enter first number :", bg="gray")
label1.pack(side=LEFT, padx=10, pady=10 )
entrie1 = Entry(frames1, textvariable=num1)
entrie1.pack(side=LEFT)
label2 = Label(frames2, text="Enter second number :" , bg="gray")
label2.pack(side=LEFT, padx=10, pady=10 )
entrie2 = Entry(frames2, textvariable=num2)
entrie2.pack(side=LEFT)
label3 = Label(frames4, text="Rsult :", bg="gray")
label3.pack(side=LEFT, padx=10, pady=10 )
entrie3 = Entry(frames4, textvariable=result)
entrie3.pack(side=LEFT)


root.mainloop()


