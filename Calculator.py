from tkinter import  *


root = Tk()

root.title("Taha - Calculator")

root.geometry("280x300")

root.resizable(0,0)

root.configure(background = '#1A1A1A')

result_label = Label(root , text = 0 , fg = 'white' , bg = '#1A1A1A')
result_label.grid(row = 0 , column = 0 , pady = (50 , 25))
result_label.config(font = ('verdana',30,'bold'))



root.mainloop()