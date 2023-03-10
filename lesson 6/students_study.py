list_students = [
    {"name" : "Sasha","landguage" : ["Python", "Java"]},
    {"name" : "Nik","landguage" : ["FrontEnd"]},
    {"name" : "Vika","landguage" : ["FrontEnd", "FullStack"]},
    {"name" : "Sergiy","landguage" : ["Python", "FullStack", "Java"]},
    {"name" : "Vlad","landguage" : ["Python", "FrontEnd", "Java"]}
]

def students_study(list_students):
    study_in_2_grp = ""
    in_front_end = ""
    not_front_end = ""
    python_java = ""
    for students in list_students:
        grp_2 = students.get("landguage")
        if len(grp_2) >= 2:
            study_in_2_grp += students.get("name") + " "
    for students in list_students:
        front_end = students.get("landguage")
        if "FrontEnd" not in front_end:
            not_front_end += students.get("name") + " "
    for students in list_students:
        std_py_ja = students.get("landguage")
        if "Python" and "Java" in std_py_ja:
            python_java += students.get("name") + " "
    return f"Study in 2 groups: {study_in_2_grp};" \
           f"Do not study FrontEnd: {not_front_end};" \
           f"In are studied Python or Java: {python_java}"


print(students_study(list_students))