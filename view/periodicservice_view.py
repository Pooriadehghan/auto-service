from view import *
from controller.periodic_service_controller import *

class PeriodicServiceView:

    def save_click(self):
        status,data=add(self.name_part.variable.get(),self.price.variable.get(),self.salary.variable.get())
        if status:
            msg.showinfo("Save",f"Periodic Service Saved\n{data}")
        else:
            msg.showerror("Save Error",f"Save Error:\n{data}")
        self.reset_form()

    def edit_click(self):
        status,data=edit(self.id.variable.get(),self.name_part.variable.get(),self.price.variable.get(),self.salary.variable.get())
        if status:
            msg.showinfo("Edit",f"Periodic Service Edited\n{data}")
        else:
            msg.showerror("Edit Error",f"Edit Error:\n{data}")
        self.reset_form()

    def remove_click(self):
        status,data=remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove",f"Periodic service Removed\n{data}")
        else:
            msg.showerror("Remove Error",f"Remove Error:\n{data}")
        self.reset_form()

    def show_invoice(self):
        pass


    def reset_form(self):
        self.id.variable.set(0)
        self.name_part.variable.set("")
        self.price.variable.set(0)
        self.salary.variable.set(0)
        status,periodicservice_list=find_all()
        self.table.refresh_table(periodicservice_list)

    def select_table(self,selected_periodicservice):
        # print(f"Clicked On - {selected_periodicservice}")
        self.id.variable.set(selected_periodicservice[0])
        self.name_part.variable.set(selected_periodicservice[1])
        self.price.variable.set(selected_periodicservice[2])
        self.salary.variable.set(selected_periodicservice[3])

    def __init__(self):
        self.win=Tk()
        self.win.title=("Periodic Service View")
        self.win.geometry("640x300")
        Label(self.win,text="Periodic Services",font=("Arial",20)).place(x=20,y=20)
        self.id=LabelAndEntry(self.win,"ID",20,90,data_type="int",state="readonly")
        self.name_part=LabelAndEntry(self.win,"Name Part",20,120)
        self.price=LabelAndEntry(self.win,"Price",20,150,data_type="int")
        self.salary=LabelAndEntry(self.win,"Salary",20,180,data_type="int")


        self.table=Table(self.win,["ID","Name Part","Price","Salary"],[60,100,100,100],250,45,self.select_table)
        Button(self.win,text="New",width=7,command=self.reset_form).place(x=20,y=220)
        Button(self.win,text="Save",width=7,command=self.save_click).place(x=90,y=220)
        Button(self.win,text="Edit",width=7,command=self.edit_click).place(x=160,y=220)
        Button(self.win,text="Remove",width=7,command=self.remove_click).place(x=20,y=250)
        Button(self.win,text="Show Invoices",width=17,command=self.show_invoice).place(x=90,y=250)


        self.reset_form()

        self.win.mainloop()

PeriodicServiceView()