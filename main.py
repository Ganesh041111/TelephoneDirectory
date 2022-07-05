#GANESH SHINGRE ::: MOBILE NUMBER FILE STORE 


from tkinter import *
from tkinter import messagebox
from tkinter import font

root = Tk()
root.title("MOBILE NUMBER FILE STORE")
root.geometry("600x750")
frame_1=Frame(root,width=600,height=750,bg="powder blue")
frame_1.pack(side=LEFT)
num_list=[]


def insert_but():
    txt1=text_1.get()
    txt2=text_2.get()
    root.clipboard_append(txt1)
    root.clipboard_append(txt2)
    
    num_list.append(txt2)
    num_count=num_list.count(txt2)
    num_check=txt2.isnumeric()
    
    check = open('Directory.txt','a')
    check1 = open('Directory.txt','r')
    test = check1.read()
    
    if num_count > 1:
        messagebox.showwarning("Warning","Mobile no already exist!!")
        num_list.pop()
    elif num_check==False or len(txt2) != 10:
        messagebox.showerror("Error","Enter valid Mobile Number!!")
        num_list.pop()
    
    elif txt2 in test:
            messagebox.showwarning("title","Mobile no already exist!!")
            num_list.pop()
    elif len(txt1)==0:
            messagebox.showerror("title","Enter Name!!")
            num_list.pop()

    else:
        fh=open("Directory.txt","a")
        fh.write(txt1)
        n=len(txt1)

        for i in range (0,25-n):
            fh.write(" ")
        fh.write("----      ")
        fh.write(txt2)
        fh.write("\n")
        fh.close()
        text_1.delete(0,END)
        text_2.delete(0,END)
        messagebox.showinfo("info","Entry Successful !!")
        

def clear_but():
    textA_1.delete(1.0,END)
   
def check_but():
    textA_1.delete(1.0,END)
    with open("Directory.txt","r") as f:
        textA_1.insert(INSERT,f.read())
   
lab_1=Label(root,text=" ENTER YOUR INFORMATION HERE ",font=("Albertus 10 bold"),width=45,bg="turquoise2")
lab_1.place(x=125,y=15)
lab_2=Label(root,text=" Enter Name ",font=("Albertus 10 bold"),width=16,bg="CadetBlue1")
lab_2.place(x=66,y=95)
lab_3=Label(root,text=" Enter Number ",font=("Albertus 10 bold"),width=16,bg="CadetBlue1")
lab_3.place(x=66,y=155)
lab_4=Label(root,text=" VIEW YOUR INFORMATION ",font=("Albertus 10 bold"),width=45,bg="turquoise2")
lab_4.place(x=125,y=244)

text_1=Entry(root,width=42,font="Courier 10 bold italic")
text_1.place(x=215,y=96)
text_2=Entry(root,width=42,font="Courier 10 bold italic")
text_2.place(x=215,y=154)

textA_1=Text(root,width=55,height=22,bg="light cyan",font="Courier 12 bold ")
textA_1.place(x=25,y=280)

but_1=Button(root,text="Insert",width=6,height=1,bg="cyan",font=("Albertus 10 bold"),command=insert_but)
but_1.place(x=270,y=200)
but_2=Button(root,text="Check",width=6,height=1,bg="cyan",font=("Albertus 10 bold"),command=check_but)
but_2.place(x=225,y=700)
but_3=Button(root,text="Clear",width=6,height=1,bg="cyan",font=("Albertus 10 bold"),command=clear_but)
but_3.place(x=315,y=700)


root.mainloop()