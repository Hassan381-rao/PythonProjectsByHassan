
students = [{'Name':'Hassan','grades':[86,95,75]},{'Name':'Zohaib','grades':[96,85,90]},]
students[0]['grades'].append(85)
for student in students:
    average_grade = sum(student['grades']) / len(student['grades'])
    print(f"{student['Name']}has an average grade of { average_grade:.2f}")
'''
students = [{'Name': 'Hassan', 'grades': [86, 95, 75]}, {'Name': 'Zohaib', 'grades': [96, 85, 90]}]
students[0]['grades'].append(85)
for student in students:
    average_grade = sum(student['grades']) / len(student['grades'])
    print(f"{student['Name']} has an average grade of {average_grade:.2f}")
'''