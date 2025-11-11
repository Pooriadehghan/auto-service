# from tkinter import *
# from view.component.label_and_entry import LabelAndEntry
# from view.component.table import Table
from view import *
from controller.repair_controller import *
# import tkinter.messagebox as msg

class RepairView:

    def save_click(self):
        status,data=add(self.name_part.variable.get(),self.label.variable.get(),self.price.variable.get(),self.quantity.variable.get(),self.salary.variable.get())
        if status:
            msg.showinfo("save",f"Repair saved\n{data}")
        else:
            msg.showerror("save Error",f"Save Error:\n{data}")
        self.reset_form()

    def edit_click(self):

        status,data=edit(self.id.variable.get(),self.name_part.variable.get(),self.label.variable.get(),self.price.variable.get(),self.quantity.variable.get(),self.salary.variable.get())
        if status:
            msg.showinfo("Edit",f"Repair Edited\n{data}")
        else:
            msg.showerror("Edit Error",f"Edit Error:\n{data}")
        self.reset_form()

    def remove_click(self):
        status,data=remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove",f"Removed\n{data}")
        else:
            msg.showerror("Remove Error",f"Remove Error:\n{data}")
        self.reset_form()


    def invoice_click(self):
        pass

    def select_table(self,selected_repair):
        # print(f"Clicked On - {selected_repair}")
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
        status,repair_list=find_all()
        print(repair_list)
        self.table.refresh_table(repair_list)

    def __init__(self):
        self.win=Tk()
        self.win.title("Repair View")
        self.win.geometry("880x320")
        Label(self.win,text="Repairs",font=("Arial",20)).place(x=20,y=5)
        self.id=LabelAndEntry(self.win,"ID",20,60,data_type="int",state="readonly")
        self.name_part=LabelAndEntry(self.win,"Name Part",20,90)
        self.label=LabelAndEntry(self.win,"Label",20,120)
        self.price=LabelAndEntry(self.win,"Price",20,150,data_type="int")
        self.quantity=LabelAndEntry(self.win,"Quantity",20,180,data_type="int")
        self.salary=LabelAndEntry(self.win,"Salary",20,210,data_type="int")


        self.table=Table(self.win,["ID","Name Part","Label","Price","Quantity","Salary"],[60,120,120,100,100,100],250,40,self.select_table)
        Button(self.win,text="New",width=7,command=self.reset_form).place(x=20,y=240)
        Button(self.win,text="Save",width=7,command=self.save_click).place(x=100,y=240)
        Button(self.win,text="Edit",width=7,command=self.edit_click).place(x=180,y=240)
        Button(self.win,text="remove",width=7,command=self.remove_click).place(x=20,y=280)
        Button(self.win,text="Show Invoices",width=18,command=self.invoice_click).place(x=100,y=280)

        self.reset_form()
        self.win.mainloop()


# RepairView()