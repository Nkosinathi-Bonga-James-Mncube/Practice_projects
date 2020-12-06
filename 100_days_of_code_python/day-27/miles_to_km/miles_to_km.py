from tkinter import *

window = Tk()
window.title("Miles to Km Convertor")
window.minsize(width=400,height=100)
window.config(padx=100,pady=100)
def get_value():
    input_value = int(input.get())
    value=str(round((input_value/5)* 8))
    label2.config(text=value)
     
input = Entry(width=10)
input.grid(column=0,row=3)
label = Label()
label.config(text="Miles is equal to ")
label.grid(column=2,row=3)

label2= Label()
label2.grid(column=3,row=3)

label3= Label()
label3.config(text="km")
label3.grid(column=4,row=3)

button= Button(text="Calculate",command=get_value)
button.grid(column=2,row=4)
window.mainloop()
