import sqlite3
from datetime import datetime
from tabulate import tabulate

class TaskManager:
    def __init__(self):
        self.testdb = 'Tasks.db'
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            description TEXT NOT NULL UNIQUE,
                            deadline TEXT,
                            status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL DEFAULT 'pending'
                        )""")
        connection.commit()
        connection.close()

    def add_task(self):
        """Function to add tasks to db"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        description = input("\nEnter your task description : ").strip()
        if len(description) == 0:
            print("\n❌ Error: Empty value not allowed!")
            connection.close()
            self.add_task()
        else:
            cursor.execute("SELECT description FROM tasks")
            desc =  [row[0] for row in cursor.fetchall()]
            if description in desc:
                print("\n❌ Error: Task already exists! Enter new task name.")
                connection.close()
                self.add_task()
            else:
                deadline = input("\nEnter the deadline for this task(YYYY-MM-DD) :").strip()
                if len(deadline) > 0:
                    date_format="%Y-%m-%d"
                    try:
                        datetime.strptime(deadline, date_format)
                        dead_date = datetime.strptime(deadline, date_format)
                        if dead_date >= datetime.now():
                            data = {'description' : description,
                                    'deadline' : deadline}
                            cursor.execute("""INSERT INTO tasks(description, deadline) 
                                        VALUES(:description, :deadline)""",data)
                            connection.commit()
                            connection.close()
                            print("\n", description ,"Added Succesfully ✅.")
                            self.main_menu()
                        else:
                            print("\n❌ Error: date should be greater than or equal to today's date")
                            connection.close()
                            self.add_task()
                    except ValueError:
                        print("\n❌ Error: Invalid date format")
                        connection.close()
                        self.add_task()
                else:
                    data = {'description' : description}
                    cursor.execute("""INSERT INTO tasks(description) 
                                        VALUES(:description)""",data)
                    connection.commit()
                    connection.close()
                    print("\n", description ,"Added Succesfully ✅.")
                    self.main_menu()
        
    def update_task(self):
        """function to update a task"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        description = input("\nEnter your task description which you want to update : ").strip()
        if len(description) == 0:
            print("\n❌ Error: Empty value not allowed!")
            connection.close()
            self.update_task()
        else:
            cursor.execute("SELECT description FROM tasks")
            desc =  [row[0] for row in cursor.fetchall()]
            if description not in desc:
                print("\n❌ Error: Task doesn't exists!")
                connection.close()
                self.update_task()
            else:
                print("\n")
                print(" 1. Update Description")
                print(" 2. Update Deadline")
                print(" 3. Update Status")
                try:
                    option = int(input("\nPlease Select one option : "))
                    if option not in range(1,4):
                        print("\n⚠️ Warning: Check your input!")
                        self.update_task()
                    elif option == 1:
                        new_description = input("\nEnter your new task description : ").strip()
                        if len(new_description) == 0:
                            print("\n❌ Error: Empty value not allowed!")
                            connection.close()
                            self.update_task()
                        else:
                            cursor.execute("SELECT description FROM tasks WHERE description != ?", (description,))
                            task_list = [row[0] for row in cursor.fetchall()]
                            if new_description in task_list:
                                print("\n❌ Error: Task already exists! Enter new task name to update.")
                                connection.close()
                                self.update_task()
                            else:
                                cursor.execute("""UPDATE tasks
                                    SET description=? where description=?""", 
                                    (new_description,description))
                                connection.commit()
                                connection.close()
                                print("\n", description ,"updated to ",new_description," ✅.")
                                self.main_menu()
                    elif option == 2:
                        new_deadline = input("\nEnter the new deadline for this task(YYYY-MM-DD) :").strip()
                        if len(new_deadline) > 0:
                            date_format="%Y-%m-%d"
                            try:
                                datetime.strptime(new_deadline, date_format)
                                dead_date = datetime.strptime(new_deadline, date_format)
                                if dead_date >= datetime.now():
                                    cursor.execute("""UPDATE tasks
                                        SET deadline=? where description=?""", 
                                        (new_deadline,description))
                                    connection.commit()
                                    connection.close()
                                    print("\nNew Deadline : ",new_deadline,"updated to ",description," ✅.")
                                    self.main_menu()
                                else:
                                    print("\n❌ Error: date should be greater than or equal to today's date")
                                    connection.close()
                                    self.update_task()
                            except ValueError:
                                print("\n❌ Error: Invalid date format")
                                connection.close()
                                self.update_task()
                        else:
                            cursor.execute("""UPDATE tasks
                                        SET deadline=? where description=?""", 
                                        (None,description))
                            connection.commit()
                            connection.close()
                            print("\nNew Deadline : - updated to ",description," ✅.")
                            self.main_menu()
                    elif option == 3:
                        status = input("\nEnter status [completed/pending] :").strip()
                        if status.capitalize() == 'Completed':
                            cursor.execute("""UPDATE tasks
                                        SET status=? where description=?""", 
                                        ('completed',description))
                            connection.commit()
                            connection.close()
                            print("\n",description," status updated to completed ✅.")
                            self.main_menu()
                        elif status.capitalize() == 'Pending':
                            cursor.execute("""UPDATE tasks
                                        SET status=? where description=?""", 
                                        ('pending',description))
                            connection.commit()
                            connection.close()
                            print("\n",description," status updated to pending ✅.")
                            self.main_menu()
                        else:
                            print("\n❌ Error: Invalid Status")
                            self.update_task()
                except:
                    print("\n⚠️ Warning: Check your input!")
                    self.update_task()

    def delete_task(self):
        """Function to delete Task"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        description = input("\nEnter your task description which you want to delete : ").strip()
        if len(description) == 0:
            print("\n❌ Error: Empty value not allowed!")
            connection.close()
            self.delete_task()
        else:
            cursor.execute("SELECT description FROM tasks")
            desc =  [row[0] for row in cursor.fetchall()]
            if description not in desc:
                print("\n❌ Error: Task doesn't exists!")
                connection.close()
                self.delete_task()
            else:
                confirm = input("\nAre you sure you want to delete [Y/N]")
                if confirm == 'Y':
                    cursor.execute("DELETE FROM tasks where description=?",
                            (description,))
                    connection.commit()
                    connection.close()
                    print("\n",description," deleted ✅.")
                    self.main_menu()
                elif confirm == 'N':
                    connection.close()
                    print("\n",description,"hasn't deleted ❌")
                    self.main_menu()
                else:
                    connection.close()
                    print("\n Invalid option ❌")
                    self.delete_task()

    def sort_tasks(self, title, option):
        """Function to sort all tasks"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        query = f"SELECT id, description, deadline, status FROM tasks ORDER BY {title} {option.upper()}"
        cursor.execute(query)
        tasks = cursor.fetchall()
        connection.close()
        return tasks


    def view_all_tasks(self):
        """Function to view all tasks"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        cursor.execute("SELECT id, description, deadline, status FROM tasks")
        tasks = cursor.fetchall()
        connection.close()

        headers = ["ID", "Description", "Deadline", "Status"]
        print(tabulate(tasks, headers, tablefmt="grid"))

        sort_tasks = input("\nDo you want to sort tasks [Y/N]? ").strip().upper()
        if sort_tasks == 'Y':
            print("\n 1. Sort By Description")
            print(" 2. Sort By Deadline")
            print(" 3. Sort By Status")
            
            try:
                title = int(input("\nEnter the option for sorting: "))
                sort_options = {1: 'description', 2: 'deadline', 3: 'status'}

                if title not in sort_options:
                    print("\n❌ Invalid option")
                    self.main_menu()
                else:
                    order = input("\nSort by [asc/desc]? ").strip().upper()
                    if order not in ['ASC', 'DESC']:
                        print("\n❌ Invalid Sort option")
                        self.main_menu()
                    else:
                        sorted_tasks = self.sort_tasks(sort_options[title], order)
                        print(tabulate(sorted_tasks, headers, tablefmt="grid"))
                        self.main_menu()
            except ValueError:
                print("\n❌ Invalid input! Please enter a number.")
                self.main_menu()

        elif sort_tasks == 'N':
            self.main_menu()
        else:
            print("\n❌ Invalid option")
            self.main_menu()

    def view_particular_task(self):
        """Function to view a single task"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        description = input("\nEnter your task description you want to view : ").strip()
        if len(description) == 0:
            print("\n❌ Error: Empty value not allowed!")
            connection.close()
            self.view_particular_task()
        else:
            cursor.execute("SELECT description FROM tasks")
            desc =  [row[0] for row in cursor.fetchall()]
            if description not in desc:
                print("\n❌ Error: Task doesn't exists!")
                connection.close()
                self.main_menu()
            else:
                cursor.execute("SELECT * FROM tasks where description = ?",(description,))
                task = cursor.fetchall()
                headers = ["ID", "Description", "Deadline", "Status"]
                print(tabulate(task, headers, tablefmt="grid"))
                connection.close()
                self.main_menu()

    def view_pending_or_completed_tasks(self,status):
        """Function to view task based on status"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        cursor.execute("SELECT id, description, deadline, status FROM tasks WHERE status = ?", (status,))
        tasks = cursor.fetchall()
        connection.close()

        headers = ["ID", "Description", "Deadline", "Status"]
        print(tabulate(tasks, headers, tablefmt="grid"))
        self.main_menu()

    def task_priority(self):
        """Function to view high priority tassk"""
        print("\n" + "=" * 50)
        print("             High Priority Tasks      ")
        print("=" * 50)
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        query = f"SELECT id, description, deadline, status FROM tasks WHERE deadline IS NOT NULL AND status='pending' ORDER BY deadline ASC"
        cursor.execute(query)
        tasks = cursor.fetchall()
        connection.close()
        headers = ["ID", "Description", "Deadline", "Status"]
        print(tabulate(tasks, headers, tablefmt="grid"))
        self.main_menu()


    def main_menu(self):
        """Main menu Function"""
        print("\n" + "=" * 30)
        print("      TASK MANAGER MENU      ")
        print("=" * 30)
        print(" 1. Add Task")
        print(" 2. Update Task")
        print(" 3. Delete Task")
        print(" 4. View All Tasks")
        print(" 5. View Particular Task")
        print(" 6. View Pending Tasks")
        print(" 7. View Completed Task")
        print(' 8. Task Prioritization')
        print(" 9. Exit")
        print("=" * 30)
        print("\n")
        try:
            option = int(input("Please Select one option : "))
            if option not in range(1,10):
                print("\n⚠️ Warning: Check your input!")
                self.main_menu()
            elif option == 1:
                self.add_task()
            elif option == 2:
                self.update_task()
            elif option == 3:
                self.delete_task()
            elif option == 4:
                self.view_all_tasks()
            elif option == 5:
                self.view_particular_task()
            elif option ==6:
                self.view_pending_or_completed_tasks('pending')
            elif option ==7:
                self.view_pending_or_completed_tasks('completed')
            elif option ==8:
                self.task_priority()
            elif option == 9:
                return
        except:
            print("\n⚠️ Warning: Check your input!")
            self.main_menu()


obj = TaskManager()
obj.main_menu()

        