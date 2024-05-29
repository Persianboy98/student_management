import mysql.connector
import tkinter.messagebox as messagebox
class Database:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='0173276',
            database='student_management'
        )

        self.cursor = self.connection.cursor()

    def add_student(self, person):
        try:
            query = "INSERT INTO students (meli, first_name, last_name, age, email) VALUES (%s, %s, %s, %s, %s)"
            person = (person.meli, person.first_name, person.last_name, person.age, person.email)
            self.cursor.execute(query, person)
            self.connection.commit()
            messagebox.showinfo("success","student added succesessfully")


        except Exception as e:
            print(e)
            messagebox.showwarning('Error','it can not add to db')


    def get_all_student(self):
        try:
            query = "SELECT * From students"
            self.cursor.execute(query)
            students = self.cursor.fetchall()
            return students
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error:{err}")
            return None

    def update_student(self, student_id, person):
        try:
                query = """
                    UPDATE students SET meli = %s,first_name= %s, last_name = %s, age = %s, email =%s
                    WHERE meli = %s
                """
                person = (person.meli, person.first_name, person.last_name, person.age, person.email, student_id)
                self.cursor.execute(query, person)
                self.connection.commit()
                messagebox.showinfo("Success ","student updated succsessfully!")
        except mysql.connector.Error as err:
                messagebox.showwarning("Error", f"Database error : {err}")

    def delete_student(self, meli):

        try:
            query = "DELETE FROM students WHERE meli = %s"
            self.cursor.execute(query, (meli,))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Success","Student not found!")
            else:
                messagebox.showwarning("succes", "student updatet successfully!")

        except mysql.connector.Error as err:
            messagebox.showwarning("Error", f"Database error:{err}")
