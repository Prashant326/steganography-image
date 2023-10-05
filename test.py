# here i will added some requre module for my project

from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image , ImageTk
import os
from stegano import lsb
from  tkinter import messagebox


#color and bgcolor variables

FRAM1_COLOR='black'
FRAM2_COLOR='white'
FRAM3_COLOR='#8B9D83'
FRAM4_COLOR='#8B9D83'
FRAM5_COLOR='#8B9D83'

POP_FRAM_COLOR='#1C3738'
POP_TEXT_COLOR='#FFFFFF'

MAINFRAME_BG_COLOR='#14453D'

FONT_STYLE='Verdana'        #text style


#function To get imge path and open img and show in frame

def Show_Image():
    global filename

    #ask to open file

    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetypes=( ("JPG file","*.jpg"),
                                                    ("PNG file","*.png"),
                                                   ("All file","*.txt")))

    #open img here
    if(filename):
        img=Image.open(filename)
        img=ImageTk.PhotoImage(img)
        lbl.configure(image=img,width=440,height=270)   #set here img width and height
        lbl.image=img


#hide data in image function here
def Hide_Data():
    global secret
    
    
    message=text_enter.get(1.0,END)     #get data from textfeild

    try:
        secret=lsb.hide(str(filename),message)  #hide data to img hide is inbuilt function in stegano in lsb 
    except:
        messagebox.showwarning(title='Warning', message='First select Image')


#this function show the hiden data from img

def Show_Data():
    try:
        clear_message=lsb.reveal(filename)      #stegano in lsb has reveal function that show data from img 
    except:
        messagebox.showwarning(title='Warning', message='Open image to show message')
    else:
        text_enter.delete(1.0,END)
        text_enter.insert(END,clear_message)    #the hiden message show from img to textfield


#this function give pop to save img

def Save_Name():
    global pop_root

    def Set_name():
        g_name=enter_img_name.get()   #get name from enter_img_name and img will be save from this name
        secret.save(g_name)

    #pop frame

    pop_root = Tk()
    pop_root.title('Name')
    pop_root.configure(bg=POP_FRAM_COLOR)
    pop_root.geometry("450x200+400+200")

    areyousure1 = tk.Label(pop_root, bg=POP_FRAM_COLOR, fg=POP_TEXT_COLOR, text="Enter Name for Image To save [.png , .jpg]", font=('Arial', 15), pady=15, padx=25)
    areyousure1.grid(column=0, row=0, columnspan=2,padx=10)


    Save_img_name = StringVar()
    enter_img_name = Entry(pop_root, textvariable=Save_img_name, font=('Arial', 20), width=20)
    enter_img_name.grid(column=0, row=1,columnspan=2,pady=5)

    img_name_save_button = tk.Button(pop_root, text="Save", width=12, height=1, activebackground='green', activeforeground='white',
                            font=(FONT_STYLE,13), command=Set_name, pady=5)
    img_name_save_button.grid(column=0, row=2, pady=25,padx=10)

    save_exit = tk.Button(pop_root, text="Exit", width=12, height=1, activebackground='green', activeforeground='white',
                          font=(FONT_STYLE,13), command=Close_pop_root, pady=5)
    save_exit.grid(column=1, row=2, pady=25,padx=10)

    pop_root.mainloop()

#remove img

def Remove_Image():
    lbl.configure(image='')


#clear text from textfield
def Clear_Text():
    text_enter.delete(1.0,END)


#close pop menu
def Close_pop_root():
    pop_root.destroy()

#exit from pop
def Closeyes():
    exit()


def Closeno():
    exitsure.destroy()


#main window exit pop
def Close_window():
    global exitsure

    exitsure = Tk()
    exitsure.configure(bg=POP_FRAM_COLOR)
    exitsure.geometry("450x200+400+200")
    exitsure.resizable(False,False)
    exitsure.title('Exit')

    areyousure = tk.Label(exitsure,text="Are you sure you want to exit?",bg=POP_FRAM_COLOR,fg=POP_TEXT_COLOR,font=('Arial',20),pady=20,padx=30)
    areyousure.grid(column=0, row=0,columnspan=2)

    ExitYes = tk.Button(exitsure,text="Yes", width=12,height=1,activebackground='red',activeforeground='white',font=(FONT_STYLE,13),pady=5,command = Closeyes)
    ExitYes.grid(column=0, row=1,pady=20,padx=10)

    ExitNo = tk.Button(exitsure,text="No", width=12,height=1,activebackground='green',activeforeground='white',font=(FONT_STYLE,13),pady=5,command = Closeno)
    ExitNo.grid(column=1, row=1,pady=20,padx=10)

    exitsure.mainloop()



#main farme(application logic)
root=Tk()

root.title("Steganography - Hide a Secret Text Message in an Image")

root.geometry("1000x650+180+80")
root.resizable(False,False)
root.configure(bg=MAINFRAME_BG_COLOR)


#icon for frame

image_icon=PhotoImage(file='icon.png')
root.iconphoto(False,image_icon)


#logo in application

logo=PhotoImage(file='icon.png')
Label(root,image=logo,bg=MAINFRAME_BG_COLOR).place(x=10,y=0)
Label(root,text='Steganography',bg=MAINFRAME_BG_COLOR,fg='white',font=(FONT_STYLE,25,)).place(x=100,y=20)


#first Frame

f1=Frame(root,bd=3,bg=FRAM1_COLOR,width=490,height=300,relief=GROOVE)
f1.place(x=10,y=80)

lbl=Label(f1,bg=FRAM1_COLOR)
lbl.place(x=15,y=10)


#second Frame

f2=Frame(root,bd=3,bg=FRAM2_COLOR,width=480,height=300,relief=GROOVE)
f2.place(x=510,y=80)

text_enter=Text(f2,font=('Robote',20),bg=FRAM2_COLOR,fg='black',relief=GROOVE,wrap=WORD)
text_enter.place(x=0,y=0,width=460,height=310)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=458,y=0,height=315)

scrollbar1.configure(command=text_enter.yview())
text_enter.configure(yscrollcommand=scrollbar1.set)


#third Frame

f3=Frame(root,bd=3,bg=FRAM3_COLOR,width=490,height=100,relief=GROOVE)
f3.place(x=10,y=390)

Button(f3,text='Open Image',width=17,height=2,font=(FONT_STYLE,14),activebackground=
       'black',activeforeground='white',command=Show_Image).place(x=20,y=17)
Button(f3,text='Save Image',width=17,height=2,font=(FONT_STYLE,14),activebackground=
       'black',activeforeground='white',command=Save_Name).place(x=250,y=17)


#Fourth Frame

f4=Frame(root,bd=3,bg=FRAM4_COLOR,width=480,height=100,relief=GROOVE)
f4.place(x=510,y=390)

Button(f4,text='Hide Data',width=17,height=2,font=(FONT_STYLE,14),activebackground=
       'orange',activeforeground='black',command=Hide_Data).place(x=20,y=17)
Button(f4,text='Show Data',width=17,height=2,font=(FONT_STYLE,14),activebackground=
       'green',activeforeground='white',command=Show_Data).place(x=250,y=17)



#five Frame

f5=Frame(root,bd=3,bg=FRAM5_COLOR,width=980,height=100,relief=GROOVE)
f5.place(x=10,y=515)

Button(f5,text='Remove Image',width=23,height=2,font=(FONT_STYLE,14),activebackground=
       'black',activeforeground='white',command=Remove_Image).place(x=20,y=17)
Button(f5,text='Clear Text',width=23,height=2,font=(FONT_STYLE,14),activebackground=
       'black',activeforeground='white',command=Clear_Text).place(x=340,y=17)
Button(f5,text='Exit',width=23,height=2,font=(FONT_STYLE,14),activebackground=
       'red',activeforeground='white',command=Close_window).place(x=660,y=17)

root.mainloop()