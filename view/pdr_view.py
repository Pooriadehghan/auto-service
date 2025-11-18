from view import *
from controller.pdr_controller import *


class PdrView:

    def save_click(self):
        data = save_pdr(self.car_id.variable.get(), self.service_description.variable.get()
                        , self.equipment_used.variable.get(), self.salary.variable.get())
        if data[0] == True:
            msg.showinfo("save", f"pdr saved successfully")
            self.reset_form()
        else:
            msg.showerror("save error", f"Error\n{data[1]}")

    def edit_click(self):
        data = edit_pdr(self.car_id.variable.get(), self.car_id.variable.get(), self.service_description.variable.get(),
                        self.equipment_used.variable.get(), self.salary.variable.get())
        if data[0] == True:
            msg.showinfo("edit", f"edit successfully")
            self.reset_form()
        else:
            msg.showerror("edit error", f"Error\n{data[1]}")

    def remove_click(self):
        data = remove_pdr_by_id(self.id.variable.get())
        if data[0] == True:
            msg.showinfo("Remove", f"removed successfully")
        else:
            msg.showerror("remove error", f"Error\n{data[1]}")

    def reset_form(self):
        self.id.variable.set(0)
        self.car_id.variable.set(0)
        self.service_description.variable.set("")
        self.equipment_used.variable.set("")
        self.salary.variable.set(0)

    def select_table(self, selected_pdr):
        self.id.variable.set(selected_pdr[0])
        self.car_id.variable.set(selected_pdr[1])
        self.service_description.variable.set(selected_pdr[2])
        self.equipment_used.variable.set(selected_pdr[3])
        self.salary.variable.set(selected_pdr[4])

    def show_pdr(self):
        record_list = find_all_pdr()

        if isinstance(record_list, tuple) and record_list[0] in False:
            msg.showerror("show_pdr error", f"Error\n{record_list[1]}")
            return
        if isinstance(record_list, list):
            self.table.refresh_table(record_list)
        else:
            self.table.refresh_table([])

    def __init__(self, title, geometry,open_invoice_command=None):
        self.win = Tk()
        self.win.geometry(geometry)
        self.win.title(title)
        Label(self.win, text="PDR", font=("Arial", 20)).place(x=20, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 80, data_type="int",state="readonly")
        self.car_id = LabelAndEntry(self.win, "Car ID", 20, 110, data_type="int")
        self.service_description = LabelAndEntry(self.win, "Description", 20, 140, data_type="str")
        self.equipment_used = LabelAndEntry(self.win, "Equipment", 20, 170, data_type="str")
        self.salary = LabelAndEntry(self.win, "Salary", 20, 200, data_type="int")

        self.table = Table(self.win, ["ID", "CAR_ID", "SERVICE_DESCRIPTION", "EQUIPMENT_USED", "SALARY"],
                           [40, 80, 140, 140, 100], 250, 80, self.select_table)

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=330)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=300)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=300)
        Button(self.win, text="Show car", width=7, command=self.show_pdr).place(x=90, y=330)

        self.open_invoice=Button(self.win,text="Open Invoice", width=10, command=lambda: open_invoice_command(self))
        self.open_invoice.place(x=160,y=330)



        self.win.mainloop()

ui=PdrView("Pdr","900x400")