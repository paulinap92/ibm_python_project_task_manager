from enum import Enum
from dataclasses import dataclass

class MenuOption(Enum:
    """
    Enumeration to define the different menu options.
    """
    ADD_TASK = 1
    MARK_COMPLETED = 2
    SHOW_TASKS = 3
    REMOVE_TASK = 4
    EXIT = 5


class Task:
    """
    Represents a task with a description and a completion status.
    """

    def __init__(self, description: str, completed: bool=False) -> None:
        """
        Initializes a new instance of Task with a description and a completion status.

        :param description: The description of the task.
        :param completed: The completion status of the task. Default is False.
        """
        self.description = description
        self.completed = completed


class TaskManager:
    """
    Manages a list of tasks.
    """

    def __init__(self):
        """
        Initializes a new empty list of tasks.
        """
        self.tasks = []

    def add_task(self, description: str) -> None:
        """
        Adds a new task to the list of pending tasks.

        :param description: The description of the new task.
        """
        task = Task(description)
        self.tasks.append(task)

    def mark_completed(self, position: int) -> None:
        """
        Marks a task as completed given its position in the task list.
        Handles the IndexError exception if the specified position does not exist.

        :param position: The position of the task to mark as completed.
        """
        try:
            self.tasks[position].completed = True
        except IndexError:
            print("Error: The specified position does not exist")

    def show_tasks(self):
        """
        Shows all pending tasks along with their status.
        """
        if not self.tasks:
            print("There are no pending tasks")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                print(f"{i + 1}. {task.description} - {status}")

    def remove_task(self, position: int) -> None:
        """
        Removes a task from the list of pending tasks given its position.
        Handles the IndexError exception if the specified position does not exist.

        :param position: The position of the task to remove.
        """
        try:
            del self.tasks[position]
        except IndexError:
            print("Error: The specified position does not exist")


@dataclass
class Menu:
    """
    Displays the menu of available options for the user.
    """
    value: int = 0

    @staticmethod
    def display_menu():
        """
        Displays the menu of available options for the user.
        """
        print("\nMenu:")
        for option in MenuOption:
            print(f"{option.value}. {option.name.replace('_', ' ').title()}")
