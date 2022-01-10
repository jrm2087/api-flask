# friends_ages = {'jose': 34, 'carolina': 27, 'farouk': 33, 'annie': 32}
#
# friends_ages['jose'] = 35
#
# print(friends_ages['jose'])

# friends = [
#     {'name': 'jose', 'age': 34},
#     {'name': 'farouk', 'age': 33},
#     {'name': 'annie', 'age': 32},
# ]
#
# print(friends[1]['name'])

student_attendance = {'jose': 87, 'carolina': 92, 'annie': 100}

for s in student_attendance:
    print(f'{s}: {student_attendance[s]}')

if 'josex' in student_attendance:
    print(f"jose: {student_attendance['jose']}")
else:
    print('jose no es un estudiante en esta clase.')

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(student_attendance))
