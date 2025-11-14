from tkinter import *
import tkinter.messagebox as msg
from view.component.label_and_entry import LabelAndEntry
from view.component.table import Table
from controller.admin_controller import *


class AdminView:

    def save_click(self):
        status, data = save(self.username.variable.get(), self.password.variable.get())
        if status:
            msg.showinfo("Save", f"Admin Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    def edit_click(self):
        status, data = edit(self.id.variable.get(), self.username.variable.get(), self.password.variable.get())
        if status:
            msg.showinfo("Edit", f"Admin Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"Admin Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def select_table(self, selected_admin):
        self.id.variable.set(selected_admin[0])
        self.username.variable.set(selected_admin[1])
        self.password.variable.set(selected_admin[2])

    def reset_form(self):
        self.id.variable.set(0)
        self.username.variable.set("")
        self.password.variable.set("")
        status, admin_list = find_all()
        if status and isinstance(admin_list, list):
            self.table.refresh_table(admin_list)
        else:
            msg.showerror("Database Error", f"Error: {admin_list}")

    def show_admin(self):
        admin_list = find_all()
        self.table.refresh_table(admin_list)

    def __init__(self, title, geometry):
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(geometry)
        Label(self.win, text="Admin", font=("Arial", 20)).place(x=10, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 50, data_type="int")
        self.username = LabelAndEntry(self.win, "Username", 20, 90)
        self.password = LabelAndEntry(self.win, "Password", 20, 130)

        self.table = Table(
            self.win,
            ["ID", "Username", "Password"],
            [90, 150, 150],
            250, 50,
            self.select_table
        )

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=170)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=210)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=210)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=210)
        Button(self.win, text="Show admin", width=10, command=self.show_admin).place(x=90, y=170)

        self.reset_form()
        self.win.mainloop()



ui = AdminView("Admin View", "700x400")
