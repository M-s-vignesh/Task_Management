# Task Manager

A simple **Task Manager** application built using **Python** and **SQLite**. This application allows users to add, update, delete, and view tasks efficiently.

---

## 🚀 Features
- 📌 Add new tasks with a deadline
- ✏️ Update existing tasks
- ❌ Delete tasks
- 📋 View all tasks in a tabular format
- 🔍 Search for a specific task
- 📅 Sort tasks by **description, deadline, or status**
- ✅ View **Pending Tasks**
- ✅ View **Completed Tasks**
- 🎯 Task **Prioritization**

---

## 🛠️ Technologies Used
- **Python** (Core functionality)
- **SQLite** (Database management)
- **Tabulate** (Pretty table formatting in CMD)
- **unittest** (Unit testing framework)

---

## 📥 Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/M-s-vignesh/Task_Management.git
   cd Task_Management
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

---

## 🔧 Usage

### **Run the Task Manager**
```sh
python task.py
```

### **Task Manager Menu**
```
==============================
      TASK MANAGER MENU
==============================
 1. Add Task
 2. Update Task
 3. Delete Task
 4. View All Tasks
 5. View Particular Task
 6. View Pending Tasks
 7. View Completed Tasks
 8. Task Prioritization
 9. Exit
```

---

## 🧪 Unit Testing
This project includes **unit tests** using Python's `unittest` framework. The test cases cover:
- ✅ Adding a new task
- ✅ Updating a task
- ✅ Deleting a task
- ✅ Viewing all tasks
- ✅ Viewing a particular task
- ✅ Sorting tasks
- ✅ Task prioritization

### **Run Unit Tests**
```sh
python -m unittest tests.py
```

---

## 📌 Example Output
```
+----+-------------+------------+-----------+
| ID | Description | Deadline   | Status    |
+----+-------------+------------+-----------+
|  1 | Task 1      | 2025-02-10 | pending   |
|  2 | Task 2      | 2025-02-15 | completed |
+----+-------------+------------+-----------+
```

---

## 🏗️ Project Structure
```
📂 task-manager
│-- 📄 tasks.py         # Core task management functions
│-- 📄 Tasks.db         # SQLite database handling
│-- 📄 tests.py         # Unit tests
│-- 📄 README.md        # Project documentation
│-- 📄 requirements.txt # List of dependencies
```

---

## ✅ To-Do (Future Improvements)
- ✅ Implement a **GUI** version using Tkinter or Flask
- ✅ Add **task priority levels**
- ✅ Implement **task reminders**

---

## 🤝 Contributing
Feel free to contribute by:
- Opening an **issue** for bugs or feature requests
- Submitting a **pull request** with enhancements

---

## ⭐ Show Your Support
If you find this project helpful, please **⭐ star the repository** and share it with others!

