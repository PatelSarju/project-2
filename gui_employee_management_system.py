import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("800x500")
        
        self.employee_list = []
        self.id_set = set()
        
        self.create_widgets()

    def create_widgets(self):
        # Create Frames
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Title Label
        self.title_label = tk.Label(self.frame, text="Employee Management System", font=("Arial", 18))
        self.title_label.grid(row=0, column=1, pady=20)

        # Add Employee Button
        self.add_button = tk.Button(self.frame, text="Add Employee", width=20, command=self.add_employee)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        # Update Employee Button
        self.update_button = tk.Button(self.frame, text="Update Employee", width=20, command=self.update_employee)
        self.update_button.grid(row=1, column=1, padx=10, pady=10)

        # Delete Employee Button
        self.delete_button = tk.Button(self.frame, text="Delete Employee", width=20, command=self.delete_employee)
        self.delete_button.grid(row=1, column=2, padx=10, pady=10)

        # Fetch Employee Button
        self.fetch_button = tk.Button(self.frame, text="Fetch Employee", width=20, command=self.fetch_employee)
        self.fetch_button.grid(row=1, column=3, padx=10, pady=10)

        # Treeview to display employee data
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Job Role", "Salary"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Job Role", text="Job Role")
        self.tree.heading("Salary", text="Salary")
        self.tree.pack(padx=10, pady=20)

    def add_employee(self):
        def save_employee():
            emp_id = int(emp_id_entry.get())
            if emp_id in self.id_set:
                messagebox.showerror("Error", "This ID already exists!")
                return
            emp_name = emp_name_entry.get()
            emp_age = int(emp_age_entry.get())
            emp_role = emp_role_entry.get()
            emp_salary = int(emp_salary_entry.get())

            self.employee_list.append({'Id': emp_id, 'Name': emp_name, 'Age': emp_age, 'Job_role': emp_role, 'Salary': emp_salary})
            self.id_set.add(emp_id)
            self.tree.insert("", "end", values=(emp_id, emp_name, emp_age, emp_role, emp_salary))
            add_window.destroy()
            messagebox.showinfo("Success", "Employee added successfully!")

        # Create a new window for adding employee
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Employee")
        add_window.geometry("400x300")

        # Employee ID Entry
        tk.Label(add_window, text="Employee ID:").grid(row=0, column=0, padx=10, pady=10)
        emp_id_entry = tk.Entry(add_window)
        emp_id_entry.grid(row=0, column=1)

        # Employee Name Entry
        tk.Label(add_window, text="Name:").grid(row=1, column=0, padx=10, pady=10)
        emp_name_entry = tk.Entry(add_window)
        emp_name_entry.grid(row=1, column=1)

        # Employee Age Entry
        tk.Label(add_window, text="Age:").grid(row=2, column=0, padx=10, pady=10)
        emp_age_entry = tk.Entry(add_window)
        emp_age_entry.grid(row=2, column=1)

        # Job Role Entry
        tk.Label(add_window, text="Job Role:").grid(row=3, column=0, padx=10, pady=10)
        emp_role_entry = tk.Entry(add_window)
        emp_role_entry.grid(row=3, column=1)

        # Employee Salary Entry
        tk.Label(add_window, text="Salary:").grid(row=4, column=0, padx=10, pady=10)
        emp_salary_entry = tk.Entry(add_window)
        emp_salary_entry.grid(row=4, column=1)

        # Save Button
        save_button = tk.Button(add_window, text="Save", command=save_employee)
        save_button.grid(row=5, column=1, pady=10)

    def fetch_employee(self):
        def show_employee():
            emp_id = int(emp_id_entry.get())
            for employee in self.employee_list:
                if employee['Id'] == emp_id:
                    messagebox.showinfo("Employee Info", f"ID: {employee['Id']}\nName: {employee['Name']}\nAge: {employee['Age']}\nJob Role: {employee['Job_role']}\nSalary: {employee['Salary']}")
                    fetch_window.destroy()
                    return
            messagebox.showerror("Error", "Employee not found!")

        # Create a new window for fetching employee
        fetch_window = tk.Toplevel(self.root)
        fetch_window.title("Fetch Employee")
        fetch_window.geometry("300x150")

        # Employee ID Entry
        tk.Label(fetch_window, text="Enter Employee ID:").grid(row=0, column=0, padx=10, pady=10)
        emp_id_entry = tk.Entry(fetch_window)
        emp_id_entry.grid(row=0, column=1)

        # Fetch Button
        fetch_button = tk.Button(fetch_window, text="Fetch", command=show_employee)
        fetch_button.grid(row=1, column=1, pady=10)

    def update_employee(self):
        def save_updated_employee():
            emp_id = int(emp_id_entry.get())
            for employee in self.employee_list:
                if employee['Id'] == emp_id:
                    detail = detail_entry.get().title()
                    if detail in employee:
                        new_value = new_value_entry.get()
                        employee[detail] = new_value
                        messagebox.showinfo("Success", f"Employee {detail} updated successfully!")
                        self.refresh_tree()
                        update_window.destroy()
                        return
                    else:
                        messagebox.showerror("Error", "Invalid column name")
                        return
            messagebox.showerror("Error", "Employee not found!")

        # Create a new window for updating employee
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Employee")
        update_window.geometry("400x250")

        # Employee ID Entry
        tk.Label(update_window, text="Enter Employee ID:").grid(row=0, column=0, padx=10, pady=10)
        emp_id_entry = tk.Entry(update_window)
        emp_id_entry.grid(row=0, column=1)

        # Column Name Entry
        tk.Label(update_window, text="Column to Update:").grid(row=1, column=0, padx=10, pady=10)
        detail_entry = tk.Entry(update_window)
        detail_entry.grid(row=1, column=1)

        # New Value Entry
        tk.Label(update_window, text="New Value:").grid(row=2, column=0, padx=10, pady=10)
        new_value_entry = tk.Entry(update_window)
        new_value_entry.grid(row=2, column=1)

        # Update Button
        update_button = tk.Button(update_window, text="Update", command=save_updated_employee)
        update_button.grid(row=3, column=1, pady=10)

    def delete_employee(self):
        def delete_emp():
            emp_id = int(emp_id_entry.get())
            for employee in self.employee_list:
                if employee['Id'] == emp_id:
                    self.employee_list.remove(employee)
                    self.id_set.remove(emp_id)
                    self.refresh_tree()
                    messagebox.showinfo("Success", "Employee deleted successfully!")
                    delete_window.destroy()
                    return
            messagebox.showerror("Error", "Employee not found!")

        # Create a new window for deleting employee
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Employee")
        delete_window.geometry("300x150")

        # Employee ID Entry
        tk.Label(delete_window, text="Enter Employee ID:").grid(row=0, column=0, padx=10, pady=10)
        emp_id_entry = tk.Entry(delete_window)
        emp_id_entry.grid(row=0, column=1)

        # Delete Button
        delete_button = tk.Button(delete_window, text="Delete", command=delete_emp)
        delete_button.grid(row=1, column=1, pady=10)

    def refresh_tree(self):
        # Clear the Treeview and insert updated employee data
        for item in self.tree.get_children():
            self.tree.delete(item)
        for emp in self.employee_list:
            self.tree.insert("", "end", values=(emp['Id'], emp['Name'], emp['Age'], emp['Job_role'], emp['Salary']))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()