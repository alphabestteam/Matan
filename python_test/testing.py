

import datetime
from developer_class import Developer
from project_class import Project
from task_class import Task


def main():
    new_project = Project("test project", datetime.datetime(2023, 9, 19), [], [], [Developer("matan", [], 5, 0, [])])
    new_task = Task("test", datetime.datetime(2023, 9, 19), 5, 3)
    new_task.set_developer(Developer("matan", [], 900, 0, []))
    new_task.set_is_complete(False)
    new_project.add_task(new_task)
    print(new_project.get_end_date())


if __name__ == "__main__":
    main()
