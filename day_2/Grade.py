studant_name = input('student name ')
m1, m2, m3, m4, m5 = eval(input(f'enrter the marks of the {studant_name}: '))
Total = m1+m2+m3+m4+m5
Average = Total/5
print(f'name: {studant_name} , Total: {Total} , Average: {(Average)}%')
if(Average >= 45 and Average <= 55):
    grade = 'C grade'
elif (Average >= 56 and Average <= 65):
    grade = 'B grade'
elif (Average >= 66 and Average <= 75):
    grade = 'A grade'
elif (Average >= 76 and Average <= 100):
    grade = 'A+ grade'
else:
    grade = 'Fail'

print(grade)
