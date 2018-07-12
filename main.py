from tkinter import filedialog
from tkinter import *
import sys, os

class GUI:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.width = 640
        self.root.height = 480
        self.root.bind('<Escape>',self.__closeWindow)

        self.__generateWindow()

    def __generateWindow(self):
        Row = 0
        Pady = 4
        Padx = 4
        self.loadFrame = Frame(self.root)
        self.fileList = Listbox(self.loadFrame,height=10,selectmode="multiple")
        self.fileList.grid(column=0, row= Row, columnspan=5, pady = Pady, padx = Padx, sticky=N+W+E+S)
        Row +=1
        self.directoryText = StringVar(self.loadFrame, value="")
        self.loadEntry = Entry(self.loadFrame, textvariable=self.directoryText, width = 50)
        self.loadEntry.grid(column=0, row= Row, columnspan=4, pady = Pady, padx = Padx, sticky=N+W)
        self.loadButton = Button(self.loadFrame, text="Open Directory", command=self.__loadDirectory)
        self.loadButton.grid(column=4, row = Row, pady = Pady, padx = Padx, sticky=N+W)
        self.loadFrame.pack()

    def __closeWindow(self,event):
        self.root.withdraw()
        sys.exit() # Quicker potentially breaks something?
        # self.root.quit() # Slow

    def __loadDirectory(self):
        self.directory = filedialog.askdirectory()
        self.directoryText.set(self.directory)
        self.directoryContent = os.listdir(self.directory)
        self.fileList.delete(0,END)
        self.fileList.insert(END, *self.directoryContent)

if __name__ == "__main__":
    root = Tk()
    gui = GUI(root,"Utilities")
    root.mainloop()
