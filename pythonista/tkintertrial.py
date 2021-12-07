import tkinter as tk

window = tk.Tk()
greetings = tk.Label(text = " Hello, user ", bg="pink",fg="black")
greetings.pack()
entry = tk.Entry(fg = "blue", bg= "black",width = 25)
name = entry.get()
entry.pack()
text_box= tk.Text()
text_box.pack()
button =tk.Button(text = " submit ", width =15, height = 5, bg = "blue", fg="yellow")
button.pack()
window.mainloop()

