from tkinter import *
import os

class Editor:
        def __init__(self,master):
                '''Editor class for storing details of the file Editor Program'''
                #Bindings and Details of File
                self.name=''
                self.Title=''
                self.master=master
                self.content=''
                self.master.title('Untitled')
                self.text=Text(self.master)
                self.text.pack(fill=BOTH,expand=YES)
                self.text.bind("<Control-s>",self.save)
                self.text.bind("<Control-o>",self.open)
                self.text.bind("<Control-n>",self.new)

                #The Menus
                
                m1=Menu(master)
                master.config(menu=m1)
                subm=Menu(m1,tearoff=0)
                m1.add_cascade(label="File",menu=subm)
                subm.add_command(label='New',command=self.new)
                subm.add_command(label='Open...',command=self.open)
                subm.add_command(label='Save',command=self.save)
                subm.add_command(label='Saved Files',command=self.saved)
                subm.add_separator()
                subm.add_command(label='Exit',command=self.exit)

                #icon
                master.iconbitmap('Designcontest-Vintage-Ink-Pen-2.ico')
                if os.path.isdir("Saved-Files"):
                        pass
                else:
                        os.mkdir("Saved-Files")

        def new(self,i=0):
                self.master.title('Untitled')
                self.text.delete(1.0,END)
                self.name=''
        def open(self,i=0):
                opn=Tk()
                opn.title('Open')
                opn.iconbitmap('Designcontest-Vintage-Ink-Pen-2.ico')
                l=Label(opn,text="File Name:")
                l.pack(side=LEFT)
                name=Entry(opn)
                def setn(l):
                        self.name=name.get()
                        f=open(os.path.join("./Saved-Files",self.name),'r')
                        self.content=f.read()
                        self.text.insert(END,self.content)
                        self.master.title(self.name)
                        f.close()
                        opn.destroy()
                name.bind('<Return>',setn)
                name.pack(side=LEFT,padx=10,pady=10)
        def save(self,i=0):
                if self.name=='':
                        sve=Tk()
                        sve.title("Save")
                        l=Label(sve,text="File Name:")
                        l.pack(side=LEFT)
                        name=Entry(sve)
                        sve.iconbitmap('Designcontest-Vintage-Ink-Pen-2.ico')
                        def setn(l):
                                self.name=name.get()
                                f=open(os.path.join("./Saved-Files",self.name),'w')
                                f.write(self.content)
                                self.master.title(self.name)
                                f.close()
                                sve.destroy()
                        self.content=self.text.get(1.0,END)
                        self.content=self.content[0:len(self.content)-1]
                        name.bind('<Return>',setn)
                        name.pack(side=LEFT,padx=10,pady=10)
                else:
                        f=open(os.path.join("./Saved-Files",self.name),'w')
                        self.content=self.text.get(1.0,END)
                        self.content=self.content[0:len(self.content)-1]
                        f.write(self.content)
                        f.close()
        def saved(self):
                Flist=os.listdir("Saved-Files")
                Flist=str(Flist)
                win=Tk()
                win.title("Saved Files:-")
                l=Label(win,text=Flist)
                l.pack(fill=BOTH,padx=10,pady=10)
                win.iconbitmap('Designcontest-Vintage-Ink-Pen-2.ico')
                
        def exit(self):
                self.master.destroy()

root=Tk()
e=Editor(root)

root.mainloop()
