from tkinter import *
from label_and_entry import LabelAndEntry
from car import Car
import tkinter.messagebox as msg

from table import Table

car_list = []

def reset_form():
    name.variable.set("")
    model.variable.set("")
    man_year.variable.set("")
    pelak.variable.set("")

    car_table.show_data(car_list)


def save_click():
    try:
        car = Car(name.variable.get(), model.variable.get(), man_year.variable.get(),pelak.variable.get())
        car_list.append(car)
        msg.showinfo("Save", "Car Saved")
        reset_form()
    except Exception as e:
        msg.showerror("Save Error", f"Error : {e}")


win = Tk()
win.geometry("660x280")
win.title("Profile")

name = LabelAndEntry(win, "Name", 20, 20)
model = LabelAndEntry(win, "Model", 20, 60)
man_year = LabelAndEntry(win, "Man_Year", 20, 100)
pelak = LabelAndEntry(win, "Pelak", 20, 140)

headings = ["Name", "Model", "man_Year", "Pelak"]
widths = [100,100,80, 100]

car_table = Table(win, headings, widths,250,20)


Button(win, text="Save", width=12, command=save_click).place(x=70, y=220)

win.mainloop()
