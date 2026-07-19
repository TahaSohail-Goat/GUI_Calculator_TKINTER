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

btn_9 = Button(root , text = '9' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_9.grid(row = 1 , column = 2)
btn_9.config(font = ('verdana',14))

btn_add = Button(root , text = '+' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_add.grid(row = 1 , column = 3)
btn_add.config(font = ('verdana',14))

btn_4 = Button(root , text = '4' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_4.grid(row = 2 , column = 0)
btn_4.config(font = ('verdana',14))

btn_5 = Button(root , text = '5' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_5.grid(row = 2 , column = 1)
btn_5.config(font = ('verdana',14))

btn_6 = Button(root , text = '6' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_6.grid(row = 2 , column = 2)
btn_6.config(font = ('verdana',14))

btn_sub = Button(root , text = '-' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_sub.grid(row = 2, column = 3)
btn_sub.config(font = ('verdana',14))


btn_3 = Button(root , text = '3' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_3.grid(row = 3 , column = 0)
btn_3.config(font = ('verdana',14))

btn_2 = Button(root , text = '2' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_2.grid(row = 3 , column = 1)
btn_2.config(font = ('verdana',14))

btn_1 = Button(root , text = '1' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_1.grid(row = 3 , column = 2)
btn_1.config(font = ('verdana',14))

btn_mul = Button(root , text = '*' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_mul.grid(row = 3 , column = 3)
btn_mul.config(font = ('verdana',14))


btn_C = Button(root , text = 'C' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_C.grid(row = 4 , column = 0)
btn_C.config(font = ('verdana',14))

btn_0 = Button(root , text = '0' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_0.grid(row = 4 , column = 1)
btn_0.config(font = ('verdana',14))


btn_eq = Button(root , text = '=' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_eq.grid(row = 4 , column = 2)
btn_eq.config(font = ('verdana',14))

btn_div = Button(root , text = '/' , bg = '#00a65a' , fg = 'white' , width = 5 , height = 2)
btn_div.grid(row = 4 , column = 3)
btn_div.config(font = ('verdana',14))
root.mainloop()