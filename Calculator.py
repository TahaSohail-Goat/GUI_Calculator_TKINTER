from tkinter import  *


root = Tk()

root.title("Taha - Calculator")

root.geometry("280x380")

root.resizable(0,0)

root.configure(background = '#1A1A1A')

result_label = Label(root , text = 0 , fg = 'white' , bg = '#1A1A1A')
result_label.grid(row = 0 , column = 0 , pady = (50 , 25))
result_label.config(font = ('verdana',30,'bold'))

btn_7 = Button(root , text = '7' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_7.grid(row = 1 , column = 0)
btn_7.config(font = ('verdana',14))


btn_8 = Button(root , text = '8' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_8.grid(row = 1 , column = 1)
btn_8.config(font = ('verdana',14))

# btn_9 = Button(root , text = '9' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
# btn_9.grid(row = 1 , column = 2)
# btn_9.config(font = ('verdana',14))

# btn_add = Button(root , text = '+' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
# btn_add.grid(row = 1 , column = 0)
# btn_add.config(font = ('verdana',14))

root.mainloop()