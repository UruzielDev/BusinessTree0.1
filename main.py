import json
from datetime import datetime


class Employee:
    def __init__(self, name, title, salary, position, team, manager, tasks=None, availability=None, notes=None, photo=None, media=None, job_role=None):
        self.name = name
        self.position = position
        self.team = team
        self.manager = manager
        self.tasks = tasks or []
        self.availability = availability or []
        self.notes = notes or ""
        self.photo = photo or ""
        self.media = media or []
        self.job_role = job_role or ""
        self.title = title
        self.salary = salary


class OrganizationChart:
    def __init__(self):
        self.employees = []
        self.relationships = {}
        self.calendar = {}

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_relationship(self, employee1, employee2):
        self.relationships[employee1] = employee2

    def add_calendar_event(self, employee, date, event):
        if employee not in self.calendar:
            self.calendar[employee] = {}
        if date not in self.calendar[employee]:
            self.calendar[employee][date] = []
        self.calendar[employee][date].append(event)

    def export_data(self):
        data = {
            'employees': [employee.__dict__ for employee in self.employees],
            'relationships': self.relationships,
            'calendar': self.calendar
        }
        return json.dumps(data)

    def import_data(self, data):
        data = json.loads(data)
        self.employees = []
        for employee_data in data['employees']:
            employee = Employee(**employee_data)
            self.add_employee(employee)
        self.relationships = data['relationships']
        self.calendar = data['calendar']

    def get_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def get_employees_by_position(self, position):
        return [employee for employee in self.employees if employee.position == position]

    def get_employees_by_team(self, team):
        return [employee for employee in self.employees if employee.team == team]

    def get_employees_by_availability(self, start_date, end_date):
        available_employees = []
        for employee in self.employees:
            if not employee.availability:
                continue
            for available_range in employee.availability:
                available_start_date = datetime.strptime(available_range['start_date'], '%Y-%m-%d')
                available_end_date = datetime.strptime(available_range['end_date'], '%Y-%m-%d')
                if start_date <= available_start_date <= end_date or start_date <= available_end_date <= end_date:
                    available_employees.append(employee)
                    break
        return available_employees

    def get_employees_by_job_role(self, job_role):
        return [employee for employee in self.employees if employee.job_role == job_role]

    def get_manager_for_employee(self, employee):
        for manager, subordinate in self.relationships.items():
            if subordinate == employee:
                return manager
        return None

    def get_subordinates_for_manager(self, manager):
        return [subordinate for subordinate in self.relationships.values() if subordinate.manager == manager]

    def add_task_for_employee(self, employee_name, task):
        employee = self.get_employee_by_name(employee_name)
        if employee:
            employee.tasks.append(task)

    def add_note_for_employee(self, employee_name, note):
        employee = self.get_employee_by_name(employee_name)
        if employee:
            employee.notes += note

    def add_media_for_employee(self, employee_name, media):
        employee = self.get_employee_by_name(employee_name)
        if employee:
            employee.media.append(media)

    def add_job_role_for_employee(self, employee_name, job_role):
        employee = self.get_employee_by_name(employee_name)
        if employee:
            employee.job_role = job_role
