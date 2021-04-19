def average_score(n_stage):
    global applicant_list
    for student in applicant_list:
        if len(student) == 11:
            student.remove(student[10])
        for k, v in departments_dict.items():
            if k == student[7 + n_stage]:
                if len(v) > 1:
                    student.append(float(max(int(student[6]), (int(student[v[0]]) + int(student[v[1]])) / 2)))
                else:
                    student.append(float(max(int(student[6]), int(student[v[0]]))))
            else:
                continue
    return sorted(applicant_list, key=lambda x: (x[7 + n_stage], -float(x[10]), x[0], x[1]), reverse=True)


applicant_list = []
end_list = []
departments_dict = {'Biotech': [2, 3],
                    'Chemistry': [3],
                    'Engineering': [4, 5],
                    'Mathematics': [4],
                    'Physics': [2, 4]
                    }
departments_students = {'Biotech': [],
                        'Chemistry': [],
                        'Engineering': [],
                        'Mathematics': [],
                        'Physics': []
                        }
n = int(input())

with open('applicant_list.txt', 'r', encoding='utf-8') as f:
    for element in f:
        applicant_list.append(element.split())
    f.close()
for stage in range(3):
    applicant_list = average_score(stage)
    for key, value in departments_dict.items():
        for elements in applicant_list[-1::-1]:
            if len(departments_students[key]) >= n:
                break
            elif elements[7 + stage] == key:
                departments_students[key].append(elements)
                applicant_list.remove(elements)
            else:
                continue

for departments in departments_students:
    departments_students[departments].sort(key=lambda student: (-float(student[10]), student[0] + student[1]))
    with open(f'{departments.lower()}.txt', 'w', encoding='utf-8') as f:
        for students in departments_students[departments]:
            f.write(f'{students[0]} {students[1]} {students[10]}' + '\n')
