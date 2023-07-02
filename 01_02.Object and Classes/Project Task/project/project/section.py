from project.task import Task
from typing import List


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task_completed = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task_completed.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        count = 0
        tasks_removed = []
        for t in self.tasks:
            if t.completed:
                count += 1
                tasks_removed.append(t)
        self.tasks = [x for x in self.tasks if x not in tasks_removed]
        return f"Cleared {count} tasks."

    def view_section(self):
        output = "\n".join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n" + \
            f"{output}"
