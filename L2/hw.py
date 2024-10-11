from tkinter import *

top = Tk()
top.title("Zomato")
top.geometry("550x400")
top.config(background="red")

# the label for user_name
user_name = Label(top,text="Email").place(x=40,y=60)

# the label for user_password
user_password = Label(top,text="Password").place(x=40,y=100)

submit_button = Button(top,text="Submit Order").place(x=40,y=330)

user_name_input_area = Entry(top,width=30).place(x=110,y=60)

user_password_entry_area = Entry(top,show='*',width=30).place(x=110,y=100)

food_name = Label(top,text="What food would you like?").place(x=40,y=160)
food_name_input_area = Entry(top,width=20).place(x=40,y=190)

options = ["Chicken Sandwich", "BLT", "Veg Sandwich", "None"]
spinbox_food = Spinbox(top, values=options, state="readonly", wrap=True).place(x= 300,y=190)


beverage_name = Label(top,text="What food would you like?").place(x=40,y=230)
beverage_name_input_area = Entry(top,width=20).place(x=40,y=260)

options2 = ["cola", "fanta", "orange juice", "Water","None"]
spinbox_drink = Spinbox(top, values=options2, state="readonly", wrap=True).place(x= 300,y=260)


top.mainloop()