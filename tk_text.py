import tkinter as tk
root = tk.Tk()
root.geometry("400x240")

def getTextInput():
    result=textExample.get("1.0","end")
    print(result)

textExample=tk.Text(root, height=10).pack()

btnRead=tk.Button(root, height=1, width=10, text="Read", command=getTextInput).pack()

root.mainloop()