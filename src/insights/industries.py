from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_data = read(path)
    industries = set()
    for job in jobs_data:
        industry = job['industry']
        if len(industry) > 0:
            industries.add(industry)

    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_by_industry = []
    for job in jobs:
        if job['industry'] == industry:
            jobs_by_industry.append(job)

    return jobs_by_industry
