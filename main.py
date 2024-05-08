import tkinter as tk
from students import Person
import tkinter.messagebox as messagebox


class StudentManagementApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry('250x400')
        self.create_widgets()
        # self.database = Database()

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

        btn_clear = tk.Button(self, text='Clear student', command=self.clear_entries)
        btn_delete.grid(row=7, column=0, padx=10, pady=10)

    def edit_student(self):
        pass

    def view_student(self):
        pass

    def del_student(self):
        pass

    def clear_entries(self):
        self.entry_id.delete(0, tk.End)
        self.entry_first_name.delete(0, tk.End)
        self.entry_last_name.delete(0, tk.End)
        self.entry_age.delete(0, tk.End)
        self.entry_email.delete(0, tk.End)

    def add_student(self):

        meli = self.entry_id.get()
        first_name = self.entry_first.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        if meli and first_name and last_name and email:
            person = Person(meli, first_name, last_name, age, email)
            messagebox.showinfo("success", "student added succeccfully!")

            self.clear_entrise()

        else:
            messagebox.showwarning('Error', 'please fill in all the fields !')


if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
