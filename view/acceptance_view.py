from view import *
from datetime import date
from tkinter import *
from model.entity.acceptance import *
from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from controller.acceptance_controller import *
import tkinter.messagebox as msg
from model.tools.validation import *
from view.carwash_view import *


class AcceptanceView:

    def destroy_window(self):
        self.win.destroy()

    def select_table(self, selected_acceptance):
        self.id.variable.set(selected_acceptance[0])
        self.car_name.variable.set(selected_acceptance[1])
        self.car_model.variable.set(selected_acceptance[2])
        self.car_year.variable.set(selected_acceptance[3])
        self.color.variable.set(selected_acceptance[4])
        self.plate.variable.set(selected_acceptance[5])
        self.vin.variable.set(selected_acceptance[6])
        self.owner.variable.set(selected_acceptance[7])
        self.owner_phone.variable.set(selected_acceptance[8])
        self.kilometers.variable.set(selected_acceptance[9])
        self.type_service.variable.set(selected_acceptance[10])
        self.date_service.variable.set(selected_acceptance[11])

    def reset_form(self):
        self.id.variable.set(0)
        self.car_name.variable.set("")
        self.car_model.variable.set("")
        self.car_year.variable.set(0)
        self.color.variable.set("")
        self.plate.variable.set("")
        self.vin.variable.set("")
        self.owner.variable.set("")
        self.owner_phone.variable.set("")
        self.kilometers.variable.set(0)
        self.type_service.variable.set("")
        self.date_service.variable.set("")
        acceptance_list = find_all_acceptance()
        self.table.refresh_table(acceptance_list)

    def save_click(self):
        data = save_acceptance(self.car_name.variable.get(), self.car_model.variable.get(),
                               self.car_year.variable.get(),
                               self.color.variable.get(), self.plate.variable.get(), self.vin.variable.get(),
                               self.owner.variable.get(), self.owner_phone.variable.get(),
                               self.kilometers.variable.get(),
                               self.type_service.variable.get(), self.date_service.variable.get())
        if data[0] == True:
            msg.showinfo("save", f"Acceptance Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data[1]}")

    def edit_click(self):
        data = edit_acceptance(self.id.variable.get(), self.car_name.variable.get(), self.car_model.variable.get(),
                               self.car_year.variable.get(),
                               self.color.variable.get(), self.plate.variable.get(), self.vin.variable.get(),
                               self.owner.variable.get(), self.owner_phone.variable.get(),
                               self.kilometers.variable.get(),
                               self.type_service.variable.get(), self.date_service.variable.get())
        if data[0] == True:
            msg.showinfo("Edit", f"acceptance Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data[1]}")

    def remove_click(self):
        data = remove_acceptance_by_id(self.id.variable.get(), self.car_name.variable.get(),
                                       self.car_model.variable.get(),
                                       self.car_year.variable.get(),
                                       self.color.variable.get(), self.plate.variable.get(), self.vin.variable.get(),
                                       self.owner.variable.get(), self.owner_phone.variable.get(),
                                       self.kilometers.variable.get(),
                                       self.type_service.variable.get(), self.date_service.variable.get())
        if data[0] == True:
            msg.showinfo("Remove", f"Acceptance Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data[1]}")

    def set_today(self):
        self.date_service.variable.set(date.today().strftime("%Y-%m-%d"))

    def show_acceptance(self):
        acceptance_list = find_all_acceptance()
        self.table.refresh_table(acceptance_list)

    def __init__(self, title, geometry, open_repairs_command=None, open_periodic_service_command=None,
                 open_pdr_command=None,
                 open_Car_wash_command=None):
        self.win = Tk()
        self.win.geometry(geometry)
        self.win.title(title)
        Label(self.win, text="Car_Accepted", font=("Arial", 20)).place(x=20, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 80, data_type=int)
        self.car_name = LabelAndEntry(self.win, "Car Name", 20, 110, data_type=str)
        self.car_model = LabelAndEntry(self.win, "Car Model", 20, 140, data_type=str)
        self.car_year = LabelAndEntry(self.win, "Car Year", 20, 170, data_type=int)
        self.color = LabelAndEntry(self.win, "Color", 20, 200, data_type=str)
        self.plate = LabelAndEntry(self.win, "Plate", 20, 230, data_type=str)
        self.vin = LabelAndEntry(self.win, "Vin", 20, 260, data_type=str)
        self.owner = LabelAndEntry(self.win, "Owner", 20, 290, data_type=str)
        self.owner_phone = LabelAndEntry(self.win, "Owner Phone", 20, 320, data_type=str)
        self.kilometers = LabelAndEntry(self.win, "Kilometers", 20, 350, data_type=int)
        self.type_service = LabelAndEntry(self.win, "type_service", 20, 380, data_type=str)
        self.date_service = LabelAndEntry(self.win, "date", 20, 410, data_type=str)
        self.table = Table(self.win,
                           ["ID", "Car name", "Car model", "Car year", "Color", "Plate", "Vin", "Owner", "Owner Phone",
                            "Kilometers", "type service", "date"], [10, 70, 70, 70, 70, 70, 70, 70, 80, 70, 70, 70],
                           260, 80,
                           self.select_table)

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=260, y=40)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=330, y=40)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=400, y=40)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=470, y=40)
        Button(self.win, text="Set today", width=7, command=self.set_today).place(x=260, y=380)
        Button(self.win, text="Show Acceptance", width=13, command=self.show_acceptance).place(x=330, y=380)
        self.open_repairs = Button(self.win, text="Open Repairs", width=10, command=lambda: open_repairs_command(self))
        self.open_repairs.place(x=260, y=340)
        self.open_periodic_service = Button(self.win, text="Open Periodic Service", width=17,
                                            command=lambda: open_periodic_service_command(self))
        self.open_periodic_service.place(x=350, y=340)
        self.open_pdr = Button(self.win, text="Open Pdr", width=10, command=lambda: open_pdr_command(self))
        self.open_pdr.place(x=490, y=340)
        self.open_Car_wash = Button(self.win, text="Open_Car wash", width=12,
                                    command=lambda: open_Car_wash_command(self))
        self.open_Car_wash.place(x=580, y=340)

        self.win.mainloop()


ui = AcceptanceView("Acceptance View", "1200x480")


def open_car_wash(current_view):
    current_view.destroy_window()
    CarWashView("CarWash View", "600x400")
