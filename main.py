class Task:
    def __init__(self, task_id, title, priority):
        self.task_id = task_id
        self.task_title = title
        self.task_priority = priority
        self.task_status = "Pending"

    def task_completion(self):
        self.task_status = "Completed"

    def __str__(self):
        return f"{self.task_id} | {self.task_title} | {self.task_priority} | {self.task_status}"


class TaskManager:
    def __init__(self):
        self.tasks = []   

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully")

    def view_tasks(self):
        if not self.tasks:
            print("No task available!")
            return

        print("\nID | Title | Priority | Status")
        print("-" * 35)
        for task in self.tasks:
            print(task)

    def task_completion(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.task_completion()
                print("Task marked is completed!")
                return
        print("Task not found.")
manager = TaskManager()

t1 = Task(1, "Finish Python Project", "High")
t2 = Task(2, "Study OOP", "Medium")

manager.add_task(t1)
manager.add_task(t2)
manager.view_tasks()
manager.task_completion(1)
manager.view_tasks()


