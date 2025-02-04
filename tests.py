import unittest
import sqlite3
import os
from datetime import datetime

class TestTaskManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up database and table for tests"""
        cls.testdb = 'Test_Tasks.db'
        connection = sqlite3.connect(cls.testdb)
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            description TEXT NOT NULL UNIQUE,
                            deadline TEXT,
                            status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL DEFAULT 'pending'
                        )""")
        connection.commit()
        connection.close()

    def setUp(self):
        """Clear the tasks table before each test"""
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()

        # Check if the table exists before deleting
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='tasks';
        """)
        table_exists = cursor.fetchone()

        if table_exists:
            cursor.execute("DELETE FROM tasks")
            connection.commit()
        
        connection.close()


    def test_to_add_task(self):
        """Test to check whether the tasks get added"""
        print("\nRunning test_to_add_tasks...", end="", flush=True)
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        data = {'description' : 'Task 1',
                'deadline' : '2025-02-21'}
        cursor.execute("""INSERT INTO tasks(description, deadline) 
                       VALUES(:description, :deadline)""",data)
        connection.commit()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        connection.close()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], data['description'])
        print(" ✅ Passed!")

    def test_to_view_tasks(self):
        """test to view all the tasks"""
        print("\nRunning test_to_view_tasks...", end="", flush=True)
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        data = {'description' : 'Task 2',
                'deadline' : '2025-02-21'}
        cursor.execute("""INSERT INTO tasks(description, deadline) 
                       VALUES(:description, :deadline)""",data)
        connection.commit()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        connection.close()
        self.assertEqual(len(tasks), 1)
        print(" ✅ Passed!")

    def test_to_update_a_task(self):
        """test to update a task"""
        print("\nRunning test_to_update_tasks...", end="", flush=True)
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        data = {'description' : 'Task 2',
                'deadline' : '2025-02-21'}
        cursor.execute("""INSERT INTO tasks(description, deadline) 
                       VALUES(:description, :deadline)""",data)
        connection.commit()
        cursor.execute("SELECT * FROM tasks where description=?",
                        (data['description'],))
        task_id = cursor.fetchone()[0]
        details = {'deadline' : '2025-02-10',}
        cursor.execute("""UPDATE tasks
                       SET deadline=? where description=?""", 
                       (details['deadline'],data['description']))
        connection.commit()
        cursor.execute("SELECT * FROM tasks where id=?",
                    (task_id,))
        tasks = cursor.fetchall()
        connection.close()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][2], details['deadline'])
        print(" ✅ Passed!")


    def test_to_delete_task(self):
        """test to delete the task"""
        print("\nRunning test_to_delete_task...", end="", flush=True)
        connection = sqlite3.connect(self.testdb)
        cursor = connection.cursor()
        data = {'description' : 'Task 2',
                'deadline' : '2025-02-21'}
        cursor.execute("""INSERT INTO tasks(description, deadline) 
                       VALUES(:description, :deadline)""",data)
        connection.commit()
        cursor.execute("SELECT * FROM tasks where description=?",
                        (data['description'],))
        task_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM tasks where id=?",
                    (task_id,))
        connection.commit()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        self.assertEqual(len(tasks), 0)
        connection.close()
        print(" ✅ Passed!")

    @classmethod
    def tearDownClass(cls):
        """remove the temp db after tests"""
        if os.path.exists(cls.testdb):  # Check if the file exists before deleting
            os.remove(cls.testdb)
