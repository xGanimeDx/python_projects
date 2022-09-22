from tkinter import Tk, Label
from time import strftime

root = Tk()
root.title('Digital Clock')

label = Label(root, font=('aerial', 72), background='black', foreground='white')

def time() -> None:
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label.pack(anchor='center')
time()

root.mainloop()
