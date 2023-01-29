def study_schedule(permanence_period, target_time):
    if target_time != 0 or target_time is None:
        return None

    users_online = 0

    for start_period, end_period in permanence_period:
        if not start_period or not end_period:
            return None
        if start_period <= target_time <= end_period:
            users_online += 1

        return users_online
