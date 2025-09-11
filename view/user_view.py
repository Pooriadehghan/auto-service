from tkinter import *
import tkinter.messagebox as msg
from view.component import *
from controller.user_controller import *


class UserView:
    def save_click(self):
        status, data = add(
            self.role.variable.get(),
            self.name.variable.get(),
            self.family.variable.get(),
            self.phone.variable.get(),
            self.address.variable.get(),
            self.department.variable.get()
        )
        if status:
            msg.showinfo("Save", f"User Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    def edit_click(self):
        status, data = edit(
            self.id.variable.get(),
            self.role.variable.get(),
            self.name.variable.get(),
            self.family.variable.get(),
            self.phone.variable.get(),
            self.address.variable.get(),
            self.department.variable.get()
        )
        if status:
            msg.showinfo("Edit", f"User Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    def remove_click(self):
        status, data = delete(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"User Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def select_table(self, selected_user):
        self.id.variable.set(selected_user[0])
        self.role.variable.set(selected_user[1])
        self.name.variable.set(selected_user[2])
        self.family.variable.set(selected_user[3])
        self.phone.variable.set(selected_user[4])
        self.address.variable.set(selected_user[5])
        self.department.variable.set(selected_user[6])

    def reset_form(self):
        self.id.variable.set(0)
        self.role.variable.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.phone.variable.set("")
        self.address.variable.set("")
        self.department.variable.set("")
        status, user_list = find_all()
        self.table.refresh_table(user_list)

    def __init__(self):
        self.win = Tk()
        self.win.title("User Info")
        self.win.geometry("800x400")

        self.id = LabelAndEntry(self.win, "Id", 20, 20, data_type="int", state="readonly")
        self.role = LabelAndEntry(self.win, "Role", 20, 60)
        self.name = LabelAndEntry(self.win, "Name", 20, 100)
        self.family = LabelAndEntry(self.win, "Family", 20, 140)
        self.phone = LabelAndEntry(self.win, "Phone", 20, 180)
        self.address = LabelAndEntry(self.win, "Address", 20, 220)
        self.department = LabelAndEntry(self.win, "Department", 20, 260)

        self.table = Table(
            self.win,
            ["Id", "Role", "Name", "Family", "Phone", "Address", "Department"],
            [40, 80, 100, 100, 100, 120, 100],
            300, 20,
            self.select_table
        )

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=320)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=90, y=320)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=160, y=320)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=230, y=320)

        self.reset_form()
        self.win.mainloop()