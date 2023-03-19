from task import Task
from task_list import TaskList


def main():
    task1 = Task("Do Laundry")
    task2 = Task("Wash Dishes")
    task3 = Task("Buy Coffee")

    task4 = Task("Watch YouTube")
    task5 = Task("Play Video Games")

    task_list1 = TaskList("Chores")
    task_list2 = TaskList("Relaxation")

    task_list1.add_task_to_list(task1)
    task_list1.add_task_to_list(task2)
    task_list1.add_task_to_list(task3)

    task_list2.add_task_to_list(task4)
    task_list2.add_task_to_list(task5)


    task_list1.check_off_task(task_id=task2.id)
    task_list1.check_off_task(task_id=task3.id)

    for task in task_list1.get_task_list().values():

        print(f"task: {task.name}, is checked: {task.is_checked}")


if __name__ == "__main__":
    main()