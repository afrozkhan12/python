import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")

listbox = tk.Listbox(root)
listbox.pack()

# Adding items to the listbox
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)

root.mainloop()