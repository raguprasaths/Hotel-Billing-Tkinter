from tkinter import *

window = Tk()

window.geometry("700x600")


# function to calculate the
# price of all the orders
def calculate():
  # dic for storing the
  # food quantity and price
  dic = {
    'Kiddy veg burger': [e1, 34],
    'Classic veg burger': [e2, 79],
    'Cheese burger': [e3, 180],
    'Paneer cheese burger': [e4, 199],
    'Tandoori chicken burger': [e5, 104],
    'Chicken cheese burger': [e6, 124]
  }
  total = 0
  for key, val in dic.items():
    if val[0].get() != "":
      total += int(val[0].get()) * val[1]

  label16 = Label(window,text="Your Total Bill is - " + str(total),font="times 18")
  label16.place(x=300, y=490)
  label16.after(1000, label16.destroy)
  window.after(1000, calculate)


label1 = Label(window, text="MEAT & EAT", font="times 20 bold")
label1.place(x=340, y=20, anchor="center")

label2 = Label(window, text="Menu", font="times 20 bold")
label2.place(x=70,y=70,)

label3 = Label(window, text="Kiddy veg burger - Rs 34", font="times 14")

label3.place(x=20, y=120)

label4 = Label(window, text="Classic veg burger - Rs 79", font="times 14")

label4.place(x=20, y=150)

label5 = Label(window, text="Cheese burger - Rs 180", font="times 14")
label5.place(x=20, y=180)

label6 = Label(window, text="Paneer cheese burger - Rs 199", font="times 14")
label6.place(x=20, y=210)

label7 = Label(window,text="Tandoori chicken burger - Rs 104",font="times 14")
label7.place(x=20, y=240)

label8 = Label(window, text="Chicken cheese burger - Rs 124", font="times 14")
label8.place(x=20, y=270)

# billing section
label9 = Label(window, text="Enter you quantity", font="times 20 bold")
label9.place(x=300, y=70)

label10 = Label(window, text="Kiddy veg burger", font="times 14")
label10.place(x=300, y=120)

e1 = Entry(window)
e1.place(x=300, y=150)

label11 = Label(window, text="Classic veg burger", font="times 14")
label11.place(x=300, y=200)

e2 = Entry(window)
e2.place(x=300, y=230)

label12 = Label(window, text="Cheese burger", font="times 14")
label12.place(x=300, y=280)

e3 = Entry(window)
e3.place(x=300, y=310)

label13 = Label(window, text="Paneer cheese burger", font="times 14")
label13.place(x=300, y=360)

e4 = Entry(window)
e4.place(x=300, y=390)

label14 = Label(window, text="Tandoori chicken burger", font="times 14")
label14.place(x=500, y=120)

e5 = Entry(window)
e5.place(x=500, y=150)

label15 = Label(window, text="Chicken cheese burger", font="times 14")

label15.place(x=500, y=200)

e6 = Entry(window)
e6.place(x=500, y=230)

# execute calculate function after 1 second
window.after(1000, calculate)

# closing the main loop
window.mainloop()
