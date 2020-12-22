def get_student_names(**kwargs):
    """it gives sorted list of values of a dict"""
    return sorted(list(kwargs.values()))


dic = {"Student 1": "Steve", "Student 2": "Becky", "Student 3": "John"}
print(get_student_names(**dic))
