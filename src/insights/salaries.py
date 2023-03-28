from typing import Union, List, Dict

from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if job['max_salary'].isnumeric():
            salary_job = int(job['max_salary'])
            if salary_job > max_salary:
                max_salary = salary_job

    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salary = 999999999
    for job in jobs:
        if job['min_salary'].isnumeric():
            salary_job = int(job['min_salary'])
            if salary_job < min_salary:
                min_salary = salary_job

    return min_salary


def validate_job(job: Dict) -> None:
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])

        if min_salary > max_salary:
            raise ValueError('"min_salary" deve ser maior que "max_salary"')
    except Exception as err:
        raise ValueError(f'Erro ao validar "job": {err.__class__}')
    else:
        return job


def validate_salary(salary: Union[int, str]) -> None:
    try:
        int(salary)
    except Exception as err:
        raise ValueError(f'Erro ao validar "salary": {err.__class__}')
    else:
        return salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    valid_job = validate_job(job)
    valid_salary = validate_salary(salary)

    max_salary = int(valid_job["max_salary"])
    min_salary = int(valid_job["min_salary"])
    salary_data = int(valid_salary)

    return salary_data >= min_salary and salary_data <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except Exception:
            pass

    return filtered_jobs
