def find_courses(list_of_students, list_of_courses,student_id):
    alinacak_ders = list()
    for student in list_of_students:
        id = student["id"]
        name = student["name"]
        surname = student["surname"]
        taken_courses = student["taken_courses"]
        for course in list_of_courses:
            code = course["code"]
            course_name = course["name"]
            capacity = course["capacity"]
            used_capacity = course["used_capacity"]
            prereq = course["prereq"]
            
            if id == student_id:
                if prereq == 0:
                    return alinacak_ders
                else:
                    length = len(prereq)
                    a = 0
                    for i in prereq:
                        if i in taken_courses:
                            a+=1
                    if a == length:
                        if used_capacity< capacity:
                            alinacak_ders.append(course_name)
        return alinacak_ders