from tkinter import messagebox
from logger import logging
from exceptions import CustomException
import mysql.connector
import dotenv
def create_db_connection():

    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="college"
        )
        print(" connection successful")
    except Exception as err:
        print(f"Error: '{err}'")
    logging.info("DB connected successfully.")
    return connection

#create db and table
def create_database_and_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cursor = connection.cursor()


    cursor.execute("CREATE DATABASE IF NOT EXISTS employee_management")


    connection = mysql.connector.connect(
        host="host",
        user="",
        password="root",
        database="employee_management"
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100),
        phone VARCHAR(20),
        position VARCHAR(50),
        salary DECIMAL(10, 2),
        date_of_joining DATE
    )
    """)

    connection.commit()
    connection.close()

#adding employee
def add_employee(self):
    name = self.name_entry.get()
    email = self.email_entry.get()
    phone = self.phone_entry.get()
    position = self.position_entry.get()
    salary = self.salary_entry.get()
    doj = self.doj_entry.get()

    logging.info("New employee name: '{}'".format(name))


    if not (name and email and phone and position and salary and doj):
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        #insrting employee
        query = """
        INSERT INTO employees (name, email, phone, position, salary, date_of_joining)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (name, email, phone, position, salary, doj)
        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Success", "Employee added successfully")
        self.clear_fields()
        self.display_employees()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to add employee: {str(e)}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def remove_employee(self):
    selected_item = self.tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "elect an employee to remove")
        return

    # Get employeeId
    emp_id = self.tree.item(selected_item, "values")[0]

    # Confirm deletion
    confirm = messagebox.askyesno("Confirm", "confirm to remove employee?")
    if not confirm:
        return

    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        # Delete employee from database
        query = "DELETE FROM employees WHERE id = %s"
        cursor.execute(query, (emp_id,))
        conn.commit()

        messagebox.showinfo("Success", "Employee removed successfully")
        self.display_employees()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove employee: {str(e)}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    logging.info("deletion succesful.")

