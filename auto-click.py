from tkinter import *
import tkinter.font as font
import pyautogui
import time
# time.sleep(1800)

root = Tk()
root.title("⚙️ Auto Clicker")
root.geometry("450x220")
root.resizable(False, False)

def runMacro():
    lists = listbox.get(0, END)
    for i in range(len(lists)):
        print(lists[i])
    # pyautogui.click(600, 185)

def clicker(x, y):
    pyautogui.click(x, y)

def moveCursor(x, y):
    pyautogui.moveTo(x, y)

def pause():
    time.sleep(1)

def add(entry):
    global items
    items.append(entry.get())
    listbox.insert(END, entry.get())
    entry.delete(0, 'end')

def delete():
    global items
    selection = listbox.curselection()
    if(len(selection) == 0):
        return
    value = listbox.get(selection[0])
    ind = items.index(value)
    del items[ind]
    listbox.delete(selection[0])

def reset():
    listbox.delete(0, END)

items = ['Test #1', 'Test #2', 'Test #3']
buttonFont = font.Font(size=50)

clickButton = Button(root, text="👆", command=clicker)
clickButton['font'] = buttonFont
moveButton = Button(root, text="👣", command=moveCursor)
moveButton['font'] = buttonFont
pauseButton = Button(root, text="⏳", command=pause)
pauseButton['font'] = buttonFont

listbox = Listbox(root, height=0, selectmode="extended")
for i in range(len(items)):
    listbox.insert(END, items[i])

deleteButton = Button(root, width=9, text="delete", overrelief="solid", command=delete)
resetButton = Button(root, width=9, text="reset", command=reset)
runButton = Button(root, width=9, text="RUN", command=runMacro)

clickButton.grid(row=0, column=0, sticky=N+E+W+S)
moveButton.grid(row=1, column=0, sticky=N+E+W+S)
pauseButton.grid(row=2, column=0, sticky=N+E+W+S)
listbox.grid(row=0, column=1, rowspan=2, columnspan=3, sticky=N+E+W+S)
deleteButton.grid(row=2, column=1)
resetButton.grid(row=2, column=2)
runButton.grid(row=2, column=3)

root.mainloop()