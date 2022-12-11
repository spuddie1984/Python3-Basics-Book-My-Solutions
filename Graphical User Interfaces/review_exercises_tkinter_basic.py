import tkinter as tk

window = tk.Tk()

'''
1. Using Tkinter from IDLE’s interactive window, execute code that
creates a window with a Label widget displaying the text "GUIs are
great!
'''

greeting1 = tk.Label(text="GUIs are great! ")
greeting1.pack()

'''
2. Repeat exercise 1 with the text "Python rocks!"
'''

greeting2 = tk.Label(text="Python rocks!")
greeting2.pack()

'''
3. Repeat exercise 1 with the text "Engage!"
'''

greeting3 = tk.Label(text="Engage!")
greeting3.pack()

window.mainloop()