from tkmodule.tkmodule import *
from tkinter import font
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo
import os

root=createTk()
root.Window(title="Untitled - Notepad",fullscreen=True)

def New():
    global file
    root.tk.title("Untitled - Notepad")
    file = None
    root.Textvar.delete(1.0, END)
    
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
            context=root.Textvar.get(1.0, END)
            f.write(context)
            f.close()

            root.tk.title(os.path.basename(file) + " - nfsNote")
    else:
        # Save the file
        f = open(file, "w")
        f.write(root.Textvar.get(1.0, END))
        f.close()
        
def Open():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("Text Documents", "*.txt")])
    
    if file=="":
        file=None
    
    else:
        root.tk.title(os.path.basename(file) + " - nfsNote")
        root.Textvar.delete(1.0,END)
        f=open(file,'r')
        context=f.read()
        root.Textvar.insert(1.0,context)
        f.close()
    
def Quit():
    root.Quit()
    
def About():
    showinfo(title="Notepad",message="Notepad by Novfensec Inc.")

file=None

menubar=Menubars(root)

menubar.createMenu()
menubar.addCmd(label="New",command=New)
menubar.addCmd(label="Open",command=Open)
menubar.addCmd(label="Save",command=Save)
menubar.nav.add_separator()
menubar.addCmd(label="Exit",command=Quit)
menubar.addHead(label="File")

menubar.createMenu()
menubar.addCmd(label="About Notepad",command=About)
menubar.addHead(label="Help")

menubar.view()

Textfont=font.Font(family="Trebuchet-MS",size=18)

root.textarea(scroll=True,fill=BOTH,expand=True,border=5,relief=FLAT,font=Textfont)
root.Run()