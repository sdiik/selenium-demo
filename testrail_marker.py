def testrail_case(case_id):
    def wrapper(func):
        setattr(func, 'testrail_case_id', case_id)
        return func
    return wrapper
