from view import *


class RepairView:

    def save_click(self):
        status, data = add(self.name_part.variable.get(), self.label.variable.get(), self.price.variable.get(),
                           self.quantity.variable.get(), self.salary.variable.get())
        if status:
            msg.showinfo("save", f"Repair saved\n{data}")
        else:
            msg.showerror("save Error", f"Save Error:\n{data}")
        self.reset_form()

    def edit_click(self):

        status, data = edit(self.id.variable.get(), self.name_part.variable.get(), self.label.variable.get(),
                            self.price.variable.get(), self.quantity.variable.get(), self.salary.variable.get())
        if status:
            msg.showinfo("Edit", f"Repair Edited\n{data}")
        else:
            msg.showerror("Edit Error", f"Edit Error:\n{data}")
        self.reset_form()

    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"Removed\n{data}")
        else:
            msg.showerror("Remove Error", f"Remove Error:\n{data}")
        self.reset_form()

    def select_table(self, selected_repair):
        self.id.variable.set(selected_repair[0])
        self.name_part.variable.set(selected_repair[1])
        self.label.variable.set(selected_repair[2])
        self.price.variable.set(selected_repair[3])
        self.quantity.variable.set(selected_repair[4])
        self.salary.variable.set(selected_repair[5])

    def reset_form(self):
        self.id.variable.set(0)
        self.name_part.variable.set("")
        self.price.variable.set(0)
        self.quantity.variable.set(0)
        self.salary.variable.set(0)
        self.label.variable.set("")
        status, repair_list = find_all()
        print(repair_list)
        self.table.refresh_table(repair_list)

    def show_repair(self):
        repair_list = find_all_repair()
        self.table.refresh_table(repair_list)

    def __init__(self, title, geometry, open_invoice_command=None):
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(geometry)
        Label(self.win, text="Repairs", font=("Arial", 20)).place(x=20, y=5)
        self.id = LabelAndEntry(self.win, "ID", 20, 60, data_type="int", state="readonly")
        self.name_part = LabelAndEntry(self.win, "Name Part", 20, 90)
        self.label = LabelAndEntry(self.win, "Label", 20, 120)
        self.price = LabelAndEntry(self.win, "Price", 20, 150, data_type="int")
        self.quantity = LabelAndEntry(self.win, "Quantity", 20, 180, data_type="int")
        self.salary = LabelAndEntry(self.win, "Salary", 20, 210, data_type="int")

        self.table = Table(self.win, ["ID", "Name Part", "Label", "Price", "Quantity", "Salary"],
                           [60, 120, 120, 100, 100, 100], 250, 60, self.select_table)
        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=250)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=90, y=250)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=180, y=250)
        Button(self.win, text="remove", width=7, command=self.remove_click).place(x=20, y=290)
        Button(self.win, text="Show repairs", width=10, command=self.show_repair).place(x=90, y=290)
        self.open_invoice = Button(self.win, text="Open Invoice", width=10, command=lambda: open_invoice_command(self))
        self.open_invoice.place(x=180, y=290)
        self.reset_form()
        self.win.mainloop()


ui = RepairView("repair view", "900x400")
