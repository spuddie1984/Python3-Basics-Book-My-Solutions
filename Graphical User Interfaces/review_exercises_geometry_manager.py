import tkinter as tk

'''
1. Try to re-create all the screenshots in this section without looking
at the source code
'''

window = tk.Tk()
frame1 = tk.Frame(master=window, width=500, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
window.mainloop()

'''
2. Below is an image of a window made with Tkinter (refer to page 592). Try to re-create
the window using the techniques you’ve learned thus far. You may
use any geometry manager you like.
'''

