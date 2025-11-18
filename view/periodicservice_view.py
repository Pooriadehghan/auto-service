from view import *


class PeriodicServiceView:

    def save_click(self):
        status, data = add(self.name_part.variable.get(), self.price.variable.get(), self.salary.variable.get())
        if status:
            msg.showinfo("Save", f"Periodic Service Saved\n{data}")
        else:
            msg.showerror("Save Error", f"Save Error:\n{data}")
        self.reset_form()

    def edit_click(self):
        status, data = edit(self.id.variable.get(), self.name_part.variable.get(), self.price.variable.get(),
                            self.salary.variable.get())
        if status:
            msg.showinfo("Edit", f"Periodic Service Edited\n{data}")
        else:
            msg.showerror("Edit Error", f"Edit Error:\n{data}")
        self.reset_form()

    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"Periodic service Removed\n{data}")
        else:
            msg.showerror("Remove Error", f"Remove Error:\n{data}")
        self.reset_form()

    def show_all(self):
        periodic_service_list = find_all_periodic_service()
        self.table.refresh_table(periodic_service_list)

    def reset_form(self):
        self.id.variable.set(0)
        self.name_part.variable.set("")
        self.price.variable.set(0)
        self.salary.variable.set(0)
        periodic_service_list = find_all()
        self.table.refresh_table(periodic_service_list)

    def select_table(self, selected_periodic_service):

        self.id.variable.set(selected_periodic_service[0])
        self.name_part.variable.set(selected_periodic_service[1])
        self.price.variable.set(selected_periodic_service[2])
        self.salary.variable.set(selected_periodic_service[3])

    def __init__(self, title,geometry,open_invoice_command=None):
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(geometry)
        Label(self.win, text="Periodic Services", font=("Arial", 20)).place(x=20, y=20)
        self.id = LabelAndEntry(self.win, "ID", 20, 90, data_type="int", state="readonly")
        self.name_part = LabelAndEntry(self.win, "Name Part", 20, 120)
        self.price = LabelAndEntry(self.win, "Price", 20, 150, data_type="int")
        self.salary = LabelAndEntry(self.win, "Salary", 20, 180, data_type="int")

        self.table = Table(self.win, ["ID", "Name Part", "Price", "Salary"], [60, 100, 100, 100], 280, 90,
                           self.select_table)
        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=220)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=90, y=220)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=180, y=220)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=20, y=260)
        Button(self.win, text="show services", width=10, command=self.show_all).place(x=90, y=260)

        self.open_invoice = Button(self.win, text="Open Invoice", width=10, command=lambda: open_invoice_command(self))
        self.open_invoice.place(x=180, y=260)

        self.win.mainloop()



ui = PeriodicServiceView("Periodic Service View", "700x400")
