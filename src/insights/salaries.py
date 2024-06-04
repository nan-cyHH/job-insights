from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            if "max_salary" in job and job["max_salary"].isdigit():
                salary = int(job["max_salary"])
                max_salary = max(max_salary, salary)
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for job in self.jobs_list:
            if "min_salary" in job and job["min_salary"].isdigit():
                salary = int(job["min_salary"])
                min_salary = min(min_salary, salary)
        return min_salary

    def convert_to_int(self, value: Union[int, str]) -> int:
        if isinstance(value, (int, str)):
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"Value {value} is not numeric.")
        else:
            raise ValueError(f"Value {value} is not a valid number or string.")

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("Job does not have salary information")

        min_salary = self.convert_to_int(job["min_salary"])
        max_salary = self.convert_to_int(job["max_salary"])
        salary = self.convert_to_int(salary)

        if max_salary < min_salary:
            raise ValueError("Max salary is less than min salary")

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[Dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
