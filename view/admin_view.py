from tkinter import *
import tkinter.messagebox as msg
from view.component import *
from controller.admin_controller import AdminController


class AdminView:
    def save_click(self):
        status, data = add(self.username.variable.get(), self.password.variable.get())
        if status:
            msg.showinfo("Save", f"Admin Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    def edit_click(self):
        status, data = edit(self.username.variable.get(), self.password.variable.get())
        if status:
            msg.showinfo("Edit", f"Admin Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    def remove_click(self):
        status, data = remove(self.username.variable.get())
        if status:
            msg.showinfo("Remove", f"Admin Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def select_table(self, selected_admin):
        self.username.variable.set(selected_admin[0])
        self.password.variable.set(selected_admin[1])

    def reset_form(self):
        self.username.variable.set("")
        self.password.variable.set("")
        status, admin_list = find_all()
        self.table.refresh_table(admin_list)

    def __init__(self):
        self.win = Tk()
        self.win.title("Admin Info")
        self.win.geometry("500x250")

        self.username = LabelAndEntry(self.win, "Username", 20, 20)
        self.password = LabelAndEntry(self.win, "Password", 20, 60)

        self.table = Table(
            self.win,
            ["Username", "Password"],
            [150, 150],
            250, 20,
            self.select_table
        )

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=120)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=160)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=160)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=160)

        self.reset_form()
        self.win.mainloop()
