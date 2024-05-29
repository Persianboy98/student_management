import tkinter as tk
from students import Person
import tkinter.messagebox as messagebox
from db import Database
from ttkbootstrap import Treeview


class StudentManagementApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry('250x400')
        self.create_widgets()
        self.configure(bg="pink")
        self.database = Database()

    def create_widgets(self):
        lbl_id = tk.Label(self, text='melli code:')
        lbl_id.grid(row=0, column=0, padx=10, pady=10)

        lbl_first_name = tk.Label(self, text='first name:')
        lbl_first_name.grid(row=1, column=0, padx=10, pady=10)

        lbl_last_name = tk.Label(self, text='last nsme:')
        lbl_last_name.grid(row=2, column=0, padx=10, pady=10)

        lbl_age = tk.Label(self, text='Age:')
        lbl_age.grid(row=3, column=0, padx=10, pady=10)

        lbl_email = tk.Label(self, text="Email:")
        lbl_email.grid(row=4, column=0, padx=10, pady=10)

        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.grid(row=1, column=1, padx=10, pady=10)

        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.grid(row=2, column=1, padx=10, pady=10)

        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=4, column=1, padx=10, pady=10)

        btn_add = tk.Button(self, text='Add student', command=self.add_student)
        btn_add.grid(row=5, column=0, padx=10, pady=10)

        btn_edit = tk.Button(self, text='Edit student', command=self.edit_student)
        btn_edit.grid(row=5, column=1, padx=10, pady=10)

        btn_view = tk.Button(self, text='View student', command=self.view_student)
        btn_view.grid(row=6, column=0, padx=10, pady=10)

        btn_delete = tk.Button(self, text='Delet student', command=self.del_student)
        btn_delete.grid(row=6, column=1, padx=10, pady=10)

        btn_clear = tk.Button(self, text='Clear entries', command=self.clear_entries)
        btn_clear.grid(row=7, column=0, padx=10, pady=10)

    def edit_student(self):
        try:
            if self.selected_student:
                edit_window = tk.Toplevel(self)
                edit_window.title("Edit Student")
                student_data = self.selected_student

                lbl_id = tk.Label(edit_window, text='Meli code')
                lbl_id.grid(row=0, column=0, padx=10, pady=10)
                self.entry_edit_id = tk.Entry(edit_window, state='normal')
                self.entry_edit_id.grid(row=0, column=1, padx=10, pady=10)
                self.entry_edit_id.insert(tk.END, student_data[0])

                lbl_first_name = tk.Label(edit_window, text='First name:')
                lbl_first_name.grid(row=1, column=0, padx=10, pady=10)
                self.entry_edit_first_name = tk.Entry(edit_window)
                self.entry_edit_first_name.grid(row=1, column=1, padx=10, pady=10)
                self.entry_edit_first_name.insert(tk.END, student_data[1])

                lbl_last_name = tk.Label(edit_window, text='Last_name')
                lbl_last_name.grid(row=2, column=0, padx=10, pady=10)
                self.entry_edit_last_name = tk.Entry(edit_window)
                self.entry_edit_last_name.grid(row=2, column=1, padx=10, pady=10)
                self.entry_edit_last_name.insert(tk.END, student_data[2])

                lbl_age = tk.Label(edit_window, text='Age')
                lbl_age.grid(row=3, column=0, padx=10, pady=10)
                self.entry_edit_age = tk.Entry(edit_window)
                self.entry_edit_age.grid(row=3, column=1, padx=10, pady=10)
                self.entry_edit_age.insert(tk.END, student_data[3])

                lbl_email = tk.Label(edit_window, text='Email')
                lbl_email.grid(row=4, column=0, padx=10, pady=10)
                self.entry_edit_email = tk.Entry(edit_window)
                self.entry_edit_email.grid(row=4, column=1, padx=10, pady=10)
                self.entry_edit_email.insert(tk.END, student_data[4])

                btn_save = tk.Button(edit_window, text='save changes',
                                     command=lambda: self.database.update_student(self.selected_student[0],
                                                                                  Person(self.entry_edit_id.get(),
                                                                                         self.entry_edit_first_name.get(),
                                                                                         self.entry_edit_last_name.get(),
                                                                                         self.entry_edit_age.get(),
                                                                                         self.entry_edit_email.get())))
                btn_save.grid(row=5, column=0, columnspan=2, padx=10, pady=10)











            else:
                messagebox.showwarning('warning', "please select a student to edit!")
        except:
            messagebox.showwarning('warning', "please select a student to edit!")

    def view_student(self):

        view_window = tk.Toplevel(self)
        view_window.title('view student')

        title_label = tk.Label(view_window, text="All students", font=('Arial', 16))
        title_label.pack(pady=10)

        student_grid = Treeview(view_window, columns=("meli", "first_name", "last_name", "age", "email"),
                                show="headings")

        student_grid.heading("meli", text="meli code")
        student_grid.heading("first_name", text="First Name")
        student_grid.heading("last_name", text="Last Name")
        student_grid.heading("age", text="Age")
        student_grid.heading("email", text="Email")
        student_grid['show'] = 'headings'

        def on_select(event):
            item_id = student_grid.selection()[0]
            self.selected_student = student_grid.item(item_id, 'values')

        student_grid.bind("<<TreeviewSelect>>", on_select)

        students = self.database.get_all_student()

        for student in students:
            student_grid.insert("", tk.END, values=student)

        student_grid.pack(fill=tk.BOTH, expand=True)

    def del_student(self):
        if self.selected_student:
            try:

                if messagebox.askyesno("confirm Deletion","Are you sure you want to delete this student?"):
                    meli_code = self.selected_student[0]
                    self.database.delete_student(meli_code)



                    self.selected_student = None

            except:
                messagebox.showwarning("Error","An error occurred while deleting student!")
        else:
            messagebox.showwarning("warning","please select a student to delete")

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def add_student(self):

        meli = self.entry_id.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        if meli and first_name and last_name and email:
            per1 = Person(meli, first_name, last_name, age, email)
            # messagebox.showinfo("success", "student added succeccfully!")
            self.database.add_student(per1)
            self.clear_entries()

        else:
            messagebox.showwarning('Error', 'please fill in all the fields !')


if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
