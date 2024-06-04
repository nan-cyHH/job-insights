from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            data = list(reader)
            self.jobs_list = data

        return self.jobs_list

    def get_unique_job_types(self):
        job_types = set()
        for job in self.jobs_list:

            if 'job_type' in job and job['job_type']:
                job_types.add(job['job_type'])
        return list(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")

        filtered_jobs = []
        for job in jobs:
            if all(
                job.get(key) == value for key, value in filter_criteria.items()
            ):
                filtered_jobs.append(job)

        return filtered_jobs
