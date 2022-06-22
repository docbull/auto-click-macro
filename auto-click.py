from tkinter import *
import pyautogui
# time.sleep(1800)

root = Tk()
root.title("⚙️ Auto Clicker")
root.geometry("540x380")
root.resizable(False, False)

xLabel = Label(root, text = "X Axis")
yLabel = Label(root, text = "Y Axis")
xLabel.grid(row=0, column=0)
yLabel.grid(row=0, column=1)
# xLabel.pack()
# yLabel.pack()
xAxis = Text(root, width=10, height=1)
# xAxis.insert(END, "X axis")
yAxis = Text(root, width=10, height=1)
# yAxis.insert(END, "Y axis")
xAxis.grid(row=1, column=0)
yAxis.grid(row=1, column=1)
# xAxis.pack()
# yAxis.pack()

def runMacro():
    x = int(xAxis.get("1.0", END))
    y = int(yAxis.get("1.0", END))
    pyautogui.click(600, 185)

button1 = Button(root, text="Run", command=runMacro)
button1.grid(row=15, column=15)
# button1.pack()

root.mainloop()