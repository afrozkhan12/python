import tkinter as tk

def display_message():
    user_text = entry.get()
    label.config(text=f"Hello, {user_text}!")

root = tk.Tk()
root.title("Textbox and Buttons")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

hello_button = tk.Button(root, text="Hello", command=display_message)
hello_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()