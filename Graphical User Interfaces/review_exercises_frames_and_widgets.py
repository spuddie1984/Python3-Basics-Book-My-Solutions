import tkinter as tk

'''
1. Try to re-create all the screenshots in this section without looking
at the source code. Focus on the last frame widget example
'''
window = tk.Tk()

border_effects = {
    "flat":tk.FLAT,
    "sunken":tk.SUNKEN,
    "raised":tk.RAISED,
    "groove":tk.GROOVE,
    "ridge":tk.RIDGE
}

for effect_name, effect in border_effects.items():
    frame = tk.Frame(master=window, relief=effect, borderwidth=5)
    # frame.pack(side=tk.RIGHT)

    label = tk.Label(master=frame,text=effect_name)
    # label.pack()
'''
2. Write a program that displays a Button widget that is fifty text units
wide and twenty-five text units tall. It should have a white back-
ground with blue text that reads "Click here".
'''
button = tk.Button(
text="Click here",
width=50,
height=25,
bg="white",
fg="blue",
)
# button.pack()
'''
3. Write a program that displays an Entry widget that is forty text
units wide and has a white background and black text. Use
.insert() to display text in the Entry widget that reads "What is
your name?"
'''

entry = tk.Entry(fg="black", bg="white", width=40)
entry.insert(0,"What is your name?")
entry.pack()

window.mainloop()