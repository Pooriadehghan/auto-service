from view import *
from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from tkinter import *

class CarWashView:
    def save_click(self):
        data = save_Carwash(self.car_id.variable.get(),
                            self.price.variable.get(), self.type_wash_var.get())
        if data[0] == True:
            msg.showinfo("Save", f"Type Car Wash Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data[1]}")

    def edit_click(self):
        data = edit_Carwash(self.id.variable.get(),self.car_id.variable.get(),
                            self.price.variable.get(), self.type_wash_var.get())
        if data[0] == True:
            msg.showinfo("Edit", f"Edit Successful")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data[1]}")

    def remove_click(self):
        data = remove_Car_wash_by_id(self.id.variable.get())
        if data[0] == True:
            msg.showinfo("Remove", f"Remove Successful")
            self.reset_form()

        else:
            msg.showerror("Remove Error", f"Error\n{data[1]}")

    def select_table(self, selected_car_wash):
        self.id.variable.set(selected_car_wash[0])
        self.price.variable.set(selected_car_wash[1])
        self.car_id.variable.set(selected_car_wash[2])

    def reset_form(self):

        self.id.variable.set(0)
        self.car_id.variable.set(0)
        self.price.variable.set(0)
        CarWash_list = find_all_Carwash()
        self.table.refresh_table(CarWash_list)

    def show_car_wash(self):
        record_list = find_all_Carwash()

        if isinstance(record_list, tuple) and record_list[0] is False:
            msg.showerror("Car Wash", record_list[1])
            return

        if isinstance(record_list, list):
            self.table.refresh_table(record_list)
        else:
            self.table.refresh_table([])

    def __init__(self, title, geometry,open_invoice_command=None):
        self.win = Tk()
        self.win.geometry(geometry)
        self.win.title(title)
        Label(self.win, text="CarWash", font=("Arial", 20)).place(x=20, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 80, data_type="int",state="readonly")
        self.car_id = LabelAndEntry(self.win, "Car ID", 20, 110, data_type="int")
        self.price = LabelAndEntry(self.win, "PRICE", 20, 140, data_type="str")
        self.type_wash_var = StringVar(value="IN")
        self.type_wash = Label(self.win, text="type_wash")
        self.type_wash.place(x=20, y=200)
        Radiobutton(self.win, text="IN", variable=self.type_wash_var, value="IN").place(x=20, y=220)
        Radiobutton(self.win, text="OUT", variable=self.type_wash_var, value="OUT").place(x=20, y=240)
        Radiobutton(self.win, text="IN & OUT", variable=self.type_wash_var, value="IN & OUT").place(x=20, y=260)

        self.table = Table(self.win, ["ID", "Car_ID", "Price", "Type_Wash"],
                           [40, 50, 80, 80], 250, 80, self.select_table)
        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=330)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=300)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=300)
        Button(self.win, text="Show car", width=7, command=self.show_car_wash).place(x=90, y=330)

        self.open_invoice = Button(self.win, text="Open Invoice", width=10, command=lambda: open_invoice_command(self))
        self.open_invoice.place(x=160, y=330)

        self.win.mainloop()


ui = CarWashView("Car Wash", "600x400")
