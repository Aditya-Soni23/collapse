

from tkinter import *

root=Tk()


root.title("Driving Lisence")
root.geometry("400x300")



root.configure(bg="white")
canvas = Canvas(root, width=400, height=300)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Driving Lisence")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Name :")
label_birth_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="Date of birth :")
label_pin_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Pin no. :")
label_adress_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Adress :")
label_authorisation_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Authorisation :")

label_name = Label(root)
label_birth = Label(root)
label_pin = Label(root)
label_adress = Label(root)
label_authorisation = Label(root)



def myCardDetails():
    name = "Aditya Soni"
    print(type(name))
    birth = "23rd Feb, 2009"
    print(type(birth))
    pin = "451478"
    print(type(pin))
    adress = "Diamond City"
    print(type(adress))
    authorisation = ["Two wheeler",",", "Four wheeler"]
    print(type(authorisation))
    label_name['text'] = name
    label_birth['text'] = birth
    label_pin['text'] = pin
    label_adress['text'] = adress
    label_authorisation['text'] = authorisation


button1 = Button(root, text = "Show my Driving Lisence", command = myCardDetails)

button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_birth_window = canvas.create_window(90, 205, anchor=CENTER, window=label_birth)
label_pin_window = canvas.create_window(155, 252, anchor=CENTER, window=label_pin)
label_adress_window = canvas.create_window(155, 252, anchor=CENTER, window=label_adress)
label_authorisation_window = canvas.create_window(155, 252, anchor=CENTER, window=label_authorisation)
canvas.pack()

root.mainloop()
