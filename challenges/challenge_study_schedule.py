def study_schedule(permanence_period, target_time) -> int:
    try:
        quantity_students: int = 0
        for init_time, end_time in permanence_period:
            if init_time <= target_time <= end_time:
                quantity_students += 1
        return quantity_students
    except TypeError:
        return None
