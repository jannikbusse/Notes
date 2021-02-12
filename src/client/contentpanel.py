
from tkinter import *
import apihandler

class ContainerManager():
    panelDict = {}
    panels = []
    thread = "my thread"
    parent = None

    cols = 2

    def __init__(self, root):
        print("container manager init")
        self.parent = root

    def add_entry(self, c):
        if c["channel"] not in self.panelDict.keys():
            self.panelDict[c["channel"]] = [(c["thread"], c["content"], c["id"])]
            return
        self.panelDict[c["channel"]].append((c["thread"], c["content"], c["id"]))
        
  
    def update_views(self):
        self.panelDict.clear()
        for p in self.panels:
            p.rm()
            print("found panels")

    
        for c in apihandler.get_notes(self.thread):
            self.add_entry(c)

        print(self.panelDict)
        counter = 0

        for key in self.panelDict.keys():
            panel = ContentPanel(self, self.parent, key, x = counter%self.cols, y = int(counter/self.cols))
            panel.add_entries(self.panelDict[key])
            self.panels.append(panel)
            counter += 1







class ContentPanel():
    listbox = None
    cManager = None
    channel = None
    entries = []
    

    def __init__(self, manager, root, channel_name, x = 0, y = 0):
        
        self.cManager = manager
        self.channel = channel_name
        self.listbox = Listbox(root, height=20, width=40)
        self.listbox.bind("<Delete>", self.delete_pressed)
        self.listbox.pack(fill="both")
        self.listbox.grid(row=y,column=x)


    def delete_pressed(self, event):
        current = self.listbox.curselection()[0]
        print("here " + self.entries[current - 1][2])
        apihandler.delete_note(self.entries[current - 1][2])
        self.cManager.update_views()


    def rm(self):
        print("removing one")
        self.listbox.destroy()
        self.listbox.pack_forget()

        
        
        self.entries = []

    

    def add_entries(self, l):
        self.listbox.delete(0, 'end')
        self.listbox.insert('end', "<< " + self.channel.upper() + " >>" )
        self.entries = l
        for c in l:
            self.listbox.insert('end', c[1])
        

            