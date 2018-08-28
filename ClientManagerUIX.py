from tkinter import *
from tkinter import ttk
import csv
import os

ClientDict = {'Microsoft': 'Microsoft'}
ItemLookUpID = ''
root = Tk()
root.title("Client/Server Manager")
# 'Master' window, is given a title
ServerTree = ttk.Treeview(root)
# Creates a treeview widget inside the root window
ServerTree["columns"] = ("one", "two")
ServerTree.column("one", width=150)
ServerTree.column("two", width=90)
ServerTree.heading("one", text="Role/Name")
ServerTree.heading("two", text="Ipv4 Address")
print(id)


def ReadData():
    with open('testfile.csv') as csv_file:
        filereader = csv.reader(csv_file)
        line_count = 0
        for row in filereader:
            if line_count > 0:
                    id = ServerTree.insert(row[0], 'end', text=str(row[1]), values=(row[2], row[3]))
            line_count += 1


def ClickEntry(event):
    CurrentItemData = ServerTree.item(ServerTree.focus())
    if not (CurrentItemData["values"][0] is ''):
        CurrentServer.set(CurrentItemData["values"][0])
    else:
        CurrentServer.set('Server group selected')
    return CurrentItemData


def RightClickEntry(event):
    CurrentItemData = ServerTree.item(ServerTree.focus())
    if CurrentItemData["values"][1] is not '':
        os.system('Echo Test')
        # Connect via RDP



ReadData()
CurrentServer = StringVar()
ContextBox = Label(root, textvariable=CurrentServer)
ServerTree.bind('<<TreeviewSelect>>', ClickEntry)
ServerTree.bind('<Button-3>', RightClickEntry)
ServerTree.pack()
ContextBox.pack()
root.mainloop()
# Main event loop is created
