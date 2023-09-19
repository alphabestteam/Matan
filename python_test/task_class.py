

import datetime
from developer_class import Developer


class Task:
    def __init__(
        self,
        task_info: str,
        open_date: datetime.datetime,
        working_days: int,
        complexity: int,
        is_complete=False,
    ) -> None:
        self._task_info = task_info
        self.open_date = open_date
        self.project = None
        self._working_days = working_days
        self.finish_date = open_date + datetime.timedelta(days=working_days)

        if type(complexity) == int and complexity >= 1 and complexity <= 5:
            self._complexity = complexity
        else:
            raise Exception("complexity is not between 1 and 5!")

        self._developer = None
        self.revenue_dev = 0
        self._is_complete = is_complete


    def set_task_info(self, task_info: str):
        self._task_info = task_info
    def get_task_info(self) -> str:
        return self._task_info


    def set_open_date(self, open_date: datetime.datetime):
        self.open_date = open_date
        self.finish_date = open_date + datetime.timedelta(days=self._working_days)
    def get_open_date(self) -> datetime.datetime:
        return self.open_date


    def set_project(self, project):
        if type(project) !=  None:
            self.project = project
        else:
            raise Exception("project is not Project type!")
    def get_project(self):
        return self.project


    def set_working_days(self, working_days: int):
        self._working_days = working_days
        self.finish_date = self.open_date + datetime.timedelta(days=working_days)
    def get_working_days(self) -> int:
        return self._working_days


    """
    no set finish date because in order to change the 
    finish date we can add the desired working days...
    """
    def get_finish_date(self) -> datetime.datetime:
        return self.finish_date


    def set_complexity(self, complexity: int):
        if type(complexity) == int and complexity >= 1 and complexity <= 5:
            self._complexity = complexity
        else:
            raise Exception("complexity is not between 1 and 5!")
    def get_complexity(self) -> int:
        return self._complexity


    def set_developer(self, developer: Developer):
        if type(developer) == Developer:
            self._developer = developer
            developer._tasks_to_do.append(self)
            self.revenue_dev = developer.get_time_in_job() * (
                self.get_complexity() / self.get_working_days()
            )
        else:
            raise Exception("developer not developer type!")
    def get_developer(self) -> Developer:
        return self._developer


    """
    no set revenue in order to reduce Security weaknesses
    """
    def get_revenue_dev(self) -> float:
        return self.revenue_dev


    def set_is_complete(self, is_complete: bool):
        self._is_complete = is_complete

        if self._is_complete:
            self._developer.set_tasks_complete(
                self._developer.get_tasks_complete().append(self)
            )
            self._developer._tasks_to_do.remove(self)
            self._developer.set_revenue(
                self._developer.get_revenue() + self.revenue_dev
            )
            self._developer.set_time_in_job(self._developer.get_time_in_job() + self.get_complexity())
    def get_is_complete(self) -> bool:
        return self._is_complete
    

    #just for testing...
    def __str__ (self):
        return f"task info: {self._task_info}\ntask open date: {self.open_date}, task finish date {self.finish_date}\n{self.revenue_dev}"
    

# def main():
#     test_dev = Developer("matan", [], 900, 0, [])
#     print(test_dev.get_time_in_job())
#     test_task = Task("test", datetime.datetime(2023, 9, 19), 40,  3)
#     test_task.set_developer(test_dev)
#     test_task.set_is_complete(True)
#     print(test_dev.get_revenue())


# if __name__ == "__main__":
#     main()