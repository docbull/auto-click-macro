from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import pyautogui
import time

fontSetup = ('Arial', 15)

def insertCommand(listbox, type, cmd):
    listbox.insert(END, type + ' ' + cmd)

def close(window):
    window.destroy()

def clicker(root, listbox):
    clickerWindow = Toplevel(root)
    clickerWindow.title("👆 Clicker")
    clickerWindow.geometry("450x220")
    clickerWindow.resizable(False, False)
    buttonLabel = Label(clickerWindow, text="Button: ", font=fontSetup)
    buttonType = ttk.Combobox(clickerWindow, values=["Left", "Right"], font=fontSetup)
    buttonType.set("Left")
    positionLabel = Label(clickerWindow, text="Position: ", font=fontSetup)
    positionXY = Text(clickerWindow, width=10, height=1.5)
    amountLabel = Label(clickerWindow, text="Amount: ", font=fontSetup)

    cmd = "click"

    cancelButton = Button(clickerWindow, text="Cancel", command=lambda:close(clickerWindow))
    okButton = Button(clickerWindow, text="OK", command=lambda:insertCommand(listbox, "👆", cmd))

    buttonLabel.grid(row=1, column=0, sticky=W)
    buttonType.grid(row=1, column=1, columnspan=2, sticky=E)
    positionLabel.grid(row=2, column=0, sticky=W)
    positionXY.grid(row=2, column=1, sticky=E)
    amountLabel.grid(row=3, column=0, sticky=W)
    cancelButton.grid(row=4, column=0, sticky=E)
    okButton.grid(row=4, column=1, sticky=E)
    # pyautogui.click(x, y)

def moveCursor(root, listbox):
    cursorWindow = Toplevel(root)
    cursorWindow.title("👣 Move Cursor")
    cursorWindow.geometry("450x220")
    cursorWindow.resizable(False, False)
    listbox.insert(END, "Cursor")
    # pyautogui.moveTo(x, y)

def pause(root, listbox):
    pauseWindow = Toplevel(root)
    pauseWindow.title("⏳ Pause")
    pauseWindow.geometry("450x220")
    pauseWindow.resizable(False, False)
    listbox.insert(END, "Pause")
    # time.sleep(1)

def openWindow(root, window, title):
    window = Toplevel(root)
    window.title(title)
    window.geometry("450x220")
    window.resizable(False, False)