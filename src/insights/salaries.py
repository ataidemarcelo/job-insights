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


def validate_job(job):
    min_salary = not job.__contains__("min_salary")
    max_salary = not job.__contains__("max_salary")

    if min_salary or max_salary:
        raise ValueError('Keys: "min_salary" e "max_salary" são obrigatórios')

    min_type = type(job["min_salary"]) != int
    max_type = type(job["max_salary"]) != int

    if min_type or max_type:
        raise ValueError('"min_type" e "max_type" tem que ser do type "int"')


# def validate_salary(salary):
#     salary_type = salary.isnumeric() or salary < 0

#     if salary_type:
#         raise ValueError('"salary_type" tem que ser do type "int"')


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        validate_job(job)
        # validate_salary(salary)

        min_value = job["min_salary"]
        max_value = job["max_salary"]

        if min_value > max_value:
            raise ValueError('"min_value" não pode ser maior que "max_value"')

        return int(salary) >= min_value and int(salary) <= max_value

    except AttributeError:
        raise ValueError('Erro ao validar!')


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
