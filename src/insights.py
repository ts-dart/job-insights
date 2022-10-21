import csv


def get_unique_job_types(path):
    lines = []

    with open(path) as file:
        data = csv.DictReader(file)

        for index in data:
            if index['job_type'] not in lines:
                lines.append(index['job_type'])

    return lines


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job_type == job['job_type']]


def get_unique_industries(path):
    industries = []

    with open(path) as file:
        for index in csv.DictReader(file):
            if index['industry'] not in industries:
                industries.append(index['industry'])

    return [industry for industry in industries if industry != '']


def filter_by_industry(jobs, industry):
    return [job for job in jobs if industry == job['industry']]


def get_max_salary(path):
    max_salary = 0

    with open(path) as file:
        for index in csv.DictReader(file):
            curr = index['max_salary']
            if curr != '' and curr != 'invalid':
                curr_int = int(index['max_salary'])
                max_salary = curr_int if curr_int > max_salary else max_salary

    return max_salary


def get_min_salary(path):
    min_salary = 1000000000

    with open(path) as file:
        for index in csv.DictReader(file):
            curr = index['min_salary']
            if curr != '' and curr != 'invalid':
                curr_int = int(index['min_salary'])
                min_salary = curr_int if curr_int < min_salary else min_salary

    return min_salary


def matches_salary_range(job, salary):
    job['min_salary'] = '' if 'min_salary' not in job else job['min_salary']
    job['max_salary'] = '' if 'max_salary' not in job else job['max_salary']

    if job['min_salary'] == '' or job['max_salary'] == '':
        raise ValueError
    elif type(job['min_salary']) != int or type(job['max_salary']) != int:
        raise ValueError
    elif job['min_salary'] > job['max_salary']:
        raise ValueError
    elif type(salary) != int:
        raise ValueError

    return True if job['min_salary'] <= salary <= job['max_salary'] else False


def filter_by_salary_range(jobs, salary):
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
    return []
