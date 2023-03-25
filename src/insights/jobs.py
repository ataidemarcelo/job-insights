from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = []
        for job in jobs_reader:
            jobs.append(job)

    return jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = set()
    for job in jobs:
        type = job['job_type']
        job_types.add(type)

    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_by_job_type = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_by_job_type.append(job)

    return jobs_by_job_type
