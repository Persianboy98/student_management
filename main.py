import tkinter as tk

class StudentManagementApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self. geometry('250x400')



if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
