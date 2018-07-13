from tkinter import filedialog
from tkinter import *
import sys, os
from Container import Directory, File

class GUI:
    def __init__(self, root, title):
        self.root = root
        root.title(title)
        root.width = 640
        root.height = 480
        root.bind('<Escape>',self.__closeWindow)

        self.__generateWindow(root)

    def __generateWindow(self, frame):
        Row = 0
        Pady = 4
        Padx = 4
        titleText = StringVar(frame, value="Utilities")
        title = Label(frame,textvariable=titleText, font = "Helvetica 16 bold") 
        title.grid(column=0,row=0,pady = Pady, padx = Padx*2, sticky=N+W+S)
        
        self.loadFrame = LabelFrame(root,text="Open Directory")
        self.directoryText = StringVar(self.loadFrame, value="")
        self.loadEntry = Entry(self.loadFrame, textvariable=self.directoryText, width = 50)
        self.loadEntry.grid(column=0, row= Row, columnspan=4, pady = Pady, padx = Padx, sticky=N+W+S)
        self.loadButton = Button(self.loadFrame, text="Open Directory", command=self.__loadDirectoryCmd)
        self.loadButton.grid(column=4, row = Row, pady = Pady, padx = Padx, sticky=N+W)
        Row +=1
        self.fileList = Listbox(self.loadFrame,height=2,selectmode="multiple")
        self.fileList.grid(column=0, row= Row, columnspan=5, pady = Pady, padx = Padx, sticky=N+W+E+S)
        
        self.loadFrame.grid(column=0,row=1,pady = Pady, padx = Padx, sticky=N+W+E+S)

    def __closeWindow(self,event):
        self.root.withdraw()
        sys.exit() # Quicker potentially breaks something?
        # self.root.quit() # Slow

    def __loadDirectoryCmd(self): # 
        # Create Folder
        self.loadedDir = Directory(filedialog.askdirectory())
        # Display path
        self.directoryText.set(self.loadedDir.GetPath())
        # Clear list
        self.fileList.delete(0,END)
        # Insert directory content into list
        contentNames = [content.GetName() for content in self.loadedDir.GetContent() ]
        self.fileList.insert(0, *contentNames)
        self.fileList.config(height=min(len(contentNames),10))

if __name__ == "__main__":
    root = Tk()
    gui = GUI(root,"Utilities")
    root.mainloop()
