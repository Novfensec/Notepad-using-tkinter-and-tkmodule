from tkmodule.tkmodule import *
from tkinter import font
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo
import os

# Parent Window
root=createTk()
root.window(title="Untitled - Notepad",fullscreen=True)

def New():
    global file
    root.title("Untitled - Notepad")
    file = None
    root.Text_var.delete(1.0, END)
    
def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled - Notepad.txt', defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
        if file=="":
            file=None
        
        else:
            f=open(file,'w')
            context=root.Text_var.get(1.0, END)
            f.write(context)
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(root.Text_var.get(1.0, END))
        f.close()
        
def Open():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("Text Documents", "*.txt")])
    
    if file=="":
        file=None
    
    else:
        root.title(os.path.basename(file) + " - Notepad")
        root.Text_var.delete(1.0,END)
        f=open(file,'r')
        context=f.read()
        root.Text_var.insert(1.0,context)
        f.close()
    
def Quit():
    root.quit()
    
def About():
    showinfo(title="Notepad",message="Notepad by Novfensec Inc.")

file=None

# Menubar
menubar=Menubars(root)

# filemenu starts
menubar.createMenu()
menubar.addCmd(label="New",command=New)
menubar.addCmd(label="Open",command=Open)
menubar.addCmd(label="Save",command=Save)
menubar.Navigation_var.add_separator()
menubar.addCmd(label="Exit",command=Quit)
menubar.addHead(label="File")

# helpmenu starts
menubar.createMenu()
menubar.addCmd(label="About Notepad",command=About)
menubar.addHead(label="Help")

menubar.view()

Textfont=font.Font(family="Trebuchet-MS",size=18)
root.textarea(scroll=True,fill=BOTH,expand=True,border=5,relief=FLAT,font=Textfont)

root.run()
