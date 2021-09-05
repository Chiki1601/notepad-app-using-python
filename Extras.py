###############################################
# Not satisfied with the number of functions? #
# Perhaps you can try this!                   #
###############################################

from tkinter import *

# * Make Window
# * Make pad

def read_only():
    pad.config(state='disabled')

def editable():
    pad.config(state='normal')

settings = Menu(options)
options.add_cascade(label='Settings', menu=settings)
settings.add_command(label='Make Read Only', command=read_only)
settings.add_command(label='Editable', command=editable)


root.mainloop()
