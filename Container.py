import os


class Container:
    def __init__(self, path):
            self.path = path # Full path

    def GetName(self):
        return os.path.basename(self.path)

    def GetDirectory(self):
        return os.path.dirname(self.path)

    def GetPath(self):
        return str(self.path)


class File(Container):
    def __init__(self, path):
        Container.__init__(self, path)

class Directory(Container):
    def __init__(self, path):
        Container.__init__(self, path)
        self.content = []

    def __len__(self):
        return len(self.content)

    def UpdateContent(self):
        self.content.clear()
        # Find all items in directory
        itemList = os.listdir(self.path)
        for itemName in itemList:
            # Convert items relative path to absolute path
            path = os.path.join(self.GetPath(),itemName)
            # Check if item is file
            if os.path.isfile(path):
                self.content.append(File(path))
            # If not file it must be directory
            else:
                self.content.append(Directory(path))
    
    def GetContent(self):
        # If content has already been populated dont refill it
        if len(self.content) is 0:
            self.UpdateContent()
        return self.content

