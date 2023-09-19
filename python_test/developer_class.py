

class Developer:
    def __init__(
        self,
        name: str,
        tasks_complete: list,
        work_days: int,
        revenue: float,
        tasks_to_do: list,
    ) -> None:
        self.name = name
        self._tasks_complete = tasks_complete
        self._work_days = work_days
        self._revenue = revenue
        self._tasks_to_do = tasks_to_do
        self.time_in_job = 1

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_tasks_complete(self, tasks_complete: list):
        self._tasks_complete = tasks_complete

    def get_tasks_complete(self) -> list:
        return self._tasks_complete

    def set_work_days(self, work_days: int):
        self._work_days = work_days

    def get_working_days(self) -> int:
        return self._work_days

    def set_revenue(self, revenue: float):
        self._revenue = revenue

    def get_revenue(self) -> float:
        return self._revenue

    def set_tasks_to_do(self, tasks_to_do: list):
        self._tasks_to_do = tasks_to_do

    def get_tasks_to_do(self) -> list:
        return self._tasks_to_do

    def set_time_in_job(self, time_in_job: int):
        self.time_in_job = time_in_job

    def get_time_in_job(self) -> int:
        return self.time_in_job


# def main():
#     test_dev = Developer("matan", [], 7, 0, [])


# if __name__ == "__main__":
#     main()