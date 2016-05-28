from tkinter import *
#!/usr/bin/bash/ env python
#major start 5/5/16
#stops the program tempoarily
import time
#finding directory, creating directories
import os
#opening file in default text editor or browser
import webbrowser
#filename pattern matching
import glob
#for GETTING THINGS TO WORK
import subprocess
#for small things
import sys


def main():
    choice = input('''
══════════════════════════════════════════╗
WELCOME TO AYDIN'S SCHOOL ORGANISATION    ║
PROGRAM.                                  ║
THIS PROGRAM ALLOWS THE USER TO CREATE    ║
SUBJECTS AND STORE NOTES ON SAID SUBJECT. ║
1. notes                                  ║
2. .PDF's                                 ║
3. exit                                   ║
══════════════════════════════════════════╝                                          
''')
    if choice == '1':
        print('''
══════════════════════════════════════════════╗
here you can make notes for subjects,         ║
type the name of the subject in here,         ║
if there is already a file of said subject    ║
then it will open and you can edit it.        ║
other wise a new file will be created         ║
                                              ║
''', end='')                                          
        firstchoice = input('''                                              ║
1. make a new file                            ║
2. detlete existing files                     ║
3. edit existing file                         ║
══════════════════════════════════════════════╝
''')
        if firstchoice == '1': 
            for i in glob.glob("\TESTFOLDER\*.txt"):
                i = i[12:]
                print(i)
            print('this is a list of the existing files.')
            addsubj = input('add subject: ')+'.txt'
            if os.path.exists(addsubj):
                print("this file already exists. opening")
                webbrowser.open(addsubj) 
                main()
            else:
                file = open(addsubj, 'w+')
                webbrowser.open(addsubj)
                main()
        elif firstchoice == '2':
            for i in glob.glob("\TESTFOLDER\*.txt"):
                i = i[12:]
                print(i)
            delfile = input("Enter whole file name here (eg eng): ") + '.txt'
            if os.path.exists(delfile):
                os.remove(delfile)
                print('done returning to menu')
                main()
            else:
                print('thatfile doenst exist. retuning to menu')
                time.sleep(3)
                main()
        elif firstchoice == '3':
            for i in glob.glob("\TESTFOLDER\*.txt"):
                i = i[12:]
                print(i)
            print('these are the existing files, enter the name of one of the existing ones listed above')
            editfile = input("Enter the name of the file(e.g eng or maths): ") + '.txt'
            if os.path.exists(editfile):
                webbrowser.open(editfile)
                main()
            else:
                print('file doesnt exist. returning to menu')
                time.sleep(3)
                main()
        else:
            print('invalid command, returning to main menu')
            time.sleep(3)
            main()
        
    elif choice == '2':
        print('''
here you can choose to save a syllabus.
take the document and turn it into a .pdf and place it in the root directory.
(search TESTFOLDER in the USB explorer)''')
        for i in glob.glob("\TESTFOLDER\*.pdf"):
            i = i[12:]
            print(i)
        secchoice = input('type the name from the above .pdf'"'s to open: ") + '.pdf'
        if os.path.exists(secchoice):
            chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            p = subprocess.Popen([chrome_path, 'file://D:/TESTFOLDER/' + secchoice])
            returncode = p.wait()
            time.sleep(3)
            
            main()
        else:
            print('that .pdf doesn'"'t exist, returning to menu")
            time.sleep(3)
            main()
                
    elif choice == '3':
        print('exiting')
        goodbye = ('G','o','o','d',' ', 'B','y','e')
        for i in goodbye:
            print(i, end='')
            time.sleep(0.5)
    elif choice == '4':
        print('time to play a text adventure')
        text()
    else:
        print('invalid command')
        time.sleep(3)
        
        main()
    
    return()

root = Tk()#creating the window with a variable name called root

root.title("Pnotes")#window title
root.geometry('300x250')#window size

def update(self):
    self.after(100, self.checkForGroupUpdates)

#i make a listbox and place it. then i list all items in the folder and print them out to the list box
combolist = Listbox(root)
combolist.pack(side=LEFT, fill=Y, padx=10, pady=10)
combolist.insert(END, "EXISITNG FILES")
combolist.insert(END, "notes")
for i in glob.glob("\TESTFOLDER\*.txt"):
    i = i[12:]
    combolist.insert(END, i)
combolist.insert(END, "PDF's")
for i in glob.glob("\TESTFOLDER\*.pdf"):
    i = i[12:]
    combolist.insert(END, i)
#a simple quit button, used multiple times all with the same variable names
Qbut = Button(root, command=root.destroy, text='Quit')
Qbut.place(x=260, y=220)

#define a function so that it can be used by a button.
#the program creates a new window, list box and some dialoge boxes
def notes():
    notebox = Tk()
    notebox.title('Pnotes - notes')
    notebox.geometry('300x250')
    
    listnotes = Listbox(notebox, selectmode=SINGLE)
    listnotes.pack(side=LEFT, padx=10, pady=10)
    listnotes.insert(END, "notes")
    for i in glob.glob("\TESTFOLDER\*.txt"):
        i = i[12:]
        listnotes.insert(END, i)
    
    newnotelbl = Label(notebox, text='<-enter new note name')
    newnotelbl.place(x=140, y=10)
    update(listnotes)
    
    # i start another function here for use within this window
    #this one is for naming a new file, then creating a new file if that name hasnt already been used
    def notename(self):
        addnote = newnote.get()
        addnote = addnote + ".txt"
        print(addnote)
        if os.path.exists(addnote):
            print("this file already exists. opening")
            webbrowser.open(addnote) 
        else:
            file = open(addnote, 'w+')
            webbrowser.open(addnote)
        
    #here i make an entry box, to enter the new note name. i define the function or method that the item will do above it for tidyness (ironically)
    newnote = Entry(notebox, textvariable='notename')
    newnote.place(x=10, y=10)

    #this is different type of function or method. this is an event. it captures the user input and does a task
    def opennote(event):
        notesel = listnotes.get(ACTIVE)
        if ".txt" not in notesel:
            print('that isnt a valid selection')
        else:
            webbrowser.open(listnotes.get(ACTIVE))

    def delnote():
        notesel = listnotes.get(ACTIVE)
        delbox = Tk()
        delbox.title("Pnotes - delete file")
        delbox.geometry('100x100')

        def itemcheck():
            print(notesel)
            if notesel == 'notes':
                print('that item cannot be deleted')
            elif notesel == 'help.txt':
                print('that cant be done mr anderson')
            else:
                os.remove(notesel)
            
        delyes = Button(delbox, text='yes', command=itemcheck)
        delyes.place(x=5, y=5, height=45, width=45)
        delno = Button(delbox, text='no', command=delbox.destroy)
        delno.place(x=60, y=5, height=45, width=45)
        sure = Label(delbox, text=notesel + '''
will be deleted''')
        sure.place(x=5, y=55)

    deletenote = Button(notebox, command=delnote, text='delete note')
    deletenote.place(x=140, y=220)
            
    #here are the binds, i bind some commands to user input to make the program work smoother  
    listnotes.bind("<Return>", opennote)
    newnote.bind('<Return>', notename)

    howto = Label(notebox, text='''
highlight and press enter
on the selected document
to open and edit it.
or highlight and press
the delete button below
to delete it.
''')
    howto.place(x=140, y=40)
 
    Qbut = Button(notebox, command=notebox.destroy, text='Quit')
    Qbut.place(x=260, y=220)
    return()
        
#after creating the note window, under it is the button that will use this function
notebut = Button(root, command=notes, text='notes')
notebut.place(x=200, y=50, height=50, width=70)


#like the notes function this is here is the pdf fucntion. again at the top i create a new window and set it's characterisitics.        
def PDFs():
    pdfbox = Tk()
    pdfbox.title('Pnotes - PDF')
    pdfbox.geometry('300x250')
    
    listpdf = Listbox(pdfbox)
    listpdf.pack(side=LEFT, fill=Y, padx=10, pady=10)
    listpdf.insert(END, "notes")
    for i in glob.glob("\TESTFOLDER\*.pdf"):
        i = i[12:]
        listpdf.insert(END, i)

    openpdf = Button(pdfbox, text='memes')
    openpdf.place(x=200, y=50, height=50, width=70)
    
    Qbut = Button(pdfbox, command=pdfbox.destroy, text='Quit')
    Qbut.place(x=260, y=220)
    return()    



pdbut = Button(root, command=PDFs, text='PDF"'"s")
pdbut.place(x=200, y=130, height=50, width=70)

#this is the helpbutton function. when the assigned button is pressed it will open the help file.
def openhelp():
    webbrowser.open('help.txt')

#here is the button that will use the help button function
helpbut = Button(root, command=openhelp, text='help')
helpbut.place(x=200, y=220)
#this loops the program. almost like a return statement, for the main program/window.
root.mainloop()

