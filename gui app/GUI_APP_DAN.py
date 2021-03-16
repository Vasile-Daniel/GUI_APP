# Vasile-Daniel DAN, data: 16 March 2021, Edinburgh  
# 
# The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. 
import tkinter as tk
from tkinter import filedialog, Text 
import os 

root = tk.Tk()

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (( "executables", "*.exe"), ("all files", "*.*") ))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, heigh=700, width = 700, bg = "#263D42")
# attached to root
canvas.pack()
# add another conteiner 
frame = tk.Frame(root, bg = "white")
# place the frame 
frame.place(relwidth=0.8, relheight = 0.8, relx = 0.1, rely =0.1)

openFile  = tk.Button(root, text = "Open File",padx = 10, pady = 5, fg = "white", bg = "#263D42", command=addApp)
# attached to the root 
openFile.pack()

runApps = tk.Button(root, text = "Run Apps",padx = 10, pady = 5, fg = "white", bg = "#263D42", command = runApps)
# attached to the root 
runApps.pack()


for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

