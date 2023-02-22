import tkinter as tk
from tkinter import messagebox
from main import OrganizationChart, Employee


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Organization Chart")

        # Create organization chart object
        self.organization_chart = OrganizationChart()

        # Create UI elements
        self.label_name = tk.Label(text="Name")
        self.label_position = tk.Label(text="Position")
        self.label_team = tk.Label(text="Team")
        self.label_manager = tk.Label(text="Manager")
        self.label_task = tk.Label(text="Task")
        self.entry_name = tk.Entry()
        self.entry_position = tk.Entry()
        self.entry_team = tk.Entry()
        self.entry_manager = tk.Entry()
        self.entry_task = tk.Entry()
        self.button_add_employee = tk.Button(text="Add Employee", command=self.add_employee)
        self.button_add_task = tk.Button(text="Add Task", command=self.add_task)

        # Add UI elements to the window
        self.label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.label_position.grid(row=1, column=0)
        self.entry_position.grid(row=1, column=1)
        self.label_team.grid(row=2, column=0)
        self.entry_team.grid(row=2, column=1)
        self.label_manager.grid(row=3, column=0)
        self.entry_manager.grid(row=3, column=1)
        self.button_add_employee.grid(row=4, column=0)
        self.label_task.grid(row=5, column=0)
        self.entry_task.grid(row=5, column=1)
        self.button_add_task.grid(row=6, column=0)

    def add_employee(self):
        name = self.entry_name.get()
        position = self.entry_position.get()
        team = self.entry_team.get()
        manager_name = self.entry_manager.get()

        manager = self.organization_chart.get_employee_by_name(manager_name)
        if not manager:
            messagebox.showerror("Error", f"Could not find manager {manager_name}")
            return

        employee = Employee(name, position, team, manager)
        self.organization_chart.add_employee(employee)

        messagebox.showinfo("Success", f"Added employee {name} to team {team} under {manager_name}")

    def add_task(self):
        name = self.entry_name.get()
        task = self.entry_task.get()

        employee = self.organization_chart.get_employee_by_name(name)
        if not employee:
            messagebox.showerror("Error", f"Could not find employee {name}")
            return

        self.organization_chart.add_task_for_employee(name, task)
        messagebox.showinfo("Success", f"Added task '{task}' for employee {name}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
