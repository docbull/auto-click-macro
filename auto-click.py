from tkinter import *
import tkinter.font as font
import pyautogui
import time
from settings import *
# time.sleep(1800)

root = Tk()
root.title("⚙️ Auto Clicker")
root.geometry("450x220")
root.resizable(False, False)

def run():
    lists = listbox.get(0, END)
    for i in range(len(lists)):
        if '👆' in lists[i]:
            pos = lists[i].split()
            pyautogui.click(int(pos[1]), int(pos[2]), clicks=int(pos[3]), interval=0.05)
        elif '👣' in lists[i]:
            pos = lists[i].split()
            pyautogui.moveTo()
        elif '⏳' in lists[i]:
            print()

def delete():
    listbox.delete(ANCHOR)

def reset():
    listbox.delete(0, END)

listbox = Listbox(root, height=0, selectmode="extended")
buttonFont = font.Font(size=50)

# set up buttons
clickButton = Button(root, text="👆", command=lambda:clicker(root, listbox))
clickButton['font'] = buttonFont
moveButton = Button(root, text="👣", command=lambda:moveCursor(root, listbox))
moveButton['font'] = buttonFont
pauseButton = Button(root, text="⏳", command=lambda:pause(root, listbox))
pauseButton['font'] = buttonFont

# execution buttons
deleteButton = Button(root, width=9, text="delete", overrelief="solid", command=delete)
resetButton = Button(root, width=9, text="reset", command=reset)
runButton = Button(root, width=9, text="RUN", command=run)

# components arrangement
clickButton.grid(row=0, column=0, sticky=N+E+W+S)
moveButton.grid(row=1, column=0, sticky=N+E+W+S)
pauseButton.grid(row=2, column=0, sticky=N+E+W+S)
listbox.grid(row=0, column=1, rowspan=2, columnspan=3, sticky=N+E+W+S)
deleteButton.grid(row=2, column=1)
resetButton.grid(row=2, column=2)
runButton.grid(row=2, column=3)

root.mainloop()