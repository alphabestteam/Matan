

import datetime
from task_class import Task
from developer_class import Developer


class Project:
    def __init__(self, project_info: str, open_date: datetime.datetime, tasks_list: list[Task], done_tasks_list: list[Task], developer_list: list[Developer]) -> None:
        self._project_info = project_info
        self.open_date = open_date
        self.end_date = open_date
        
        for task in tasks_list:
            self.end_date = self.end_date + datetime.timedelta(days=task.get_working_days())

        self.tasks_list = tasks_list
        self.done_tasks_list = done_tasks_list
        self.developer_list = developer_list
        self.project_cost = 0

        for task in self.done_tasks_list:
            self.project_cost += task.get_revenue_dev()
        
        self.is_complete = (len(self.tasks_list) == 0)
    

    def set_project_info(self, project_info: str):
        self._project_info = project_info
    def get_project_info(self) -> str:
        return self._project_info
    

    def set_open_date(self, open_date: datetime.datetime):
        self.open_date = open_date
        self.end_date = open_date
        
        for task in self.tasks_list:
            self.end_date = self.end_date + datetime.timedelta(days=task.get_working_days())
    def get_open_date(self) -> datetime.datetime:
        return self.end_date
    

    """
    no need for set end date , based on open date...
    """
    def get_end_date(self) -> datetime.datetime:
        return self.end_date
    

    def add_task(self, task: Task):
        """
        Add task to task list
        input: Task
        returns: None
        """
        if type(task) == Task and not task.get_is_complete():
            self.tasks_list.append(task)
            self.end_date = self.end_date + datetime.timedelta(days=task.get_working_days())
            self.is_complete = False
            task.project = self
        else:
            if type(task) != Task:
                raise Exception("task not task type") 
            else:
                self.done_tasks_list.append(task)
                self.project_cost += task.get_revenue_dev()


    def remove_task(self, task: Task):
        """
        Removes task from task list
        input: Task
        returns: None
        """
        if type(task) == Task and not task.get_is_complete():
            self.tasks_list.remove(task)
            self.end_date = self.end_date - datetime.timedelta(days=task.get_working_days())
            self.project_cost = self.project_cost - task.get_revenue_dev()
            self.done_tasks_list.append(task)
            self.is_complete = len(self.tasks_list) == 0
        else:
            raise Exception("task not task type Or not complete!")


    def get_task_list(self) -> list[Task]:
        return self.tasks_list
    

    def get_done_tasks_list(self) -> list[Task]:
        return self.done_tasks_list
    

    def add_developer(self, developer: Developer):
        """
        adds developer to developer list
        input: Developer
        returns: None
        """
        if type(developer) == Developer:
            self.developer_list.append(developer)
        else:
            raise Exception("developer not Developer type")
    def get_developer_list(self) -> list[Developer]:
        return self.developer_list
    

    """
    No need for set project cost
    """
    def get_project_cost(self) -> float:
        return self.project_cost
    

    def get_project_is_complete(self) -> bool:
        return self.is_complete
    