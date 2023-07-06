def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    student = 0
    for login, logout in permanence_period:
        if not isinstance(login, int) or not isinstance(logout, int):
            return None
        if login <= target_time <= logout:
            student += 1
    return student
