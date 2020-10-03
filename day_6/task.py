# start
studant_List = []
studants_List = []
for i in range(5):
    studant_name = input('student name ')
    # studant_List.append(studant_name)
    m1, m2, m3, m4, m5 = eval(
        input(f'enrter the marks of the {studant_name}: '))
    Total = m1+m2+m3+m4+m5
    # studant_List.append(Total)
    Average = Total/5
    # studant_List.append(Average)
    #print(f'name: {studant_name} , Total: {Total} , Average: {(Average)}%')
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
    studant_List = [studant_name, Total, Average, grade]
    # print(studant_List)
    studants_List.append(studant_List)

# studants_List.insert(0, studant_List[0:4])
# studants_List.insert(1, studant_List[4:8])
# studants_List.insert(2, studant_List[8:12])
# studants_List.insert(3, studant_List[12:16])
# studants_List.insert(4, studant_List[16:20])
# #studants_List.insert(5, studant_List[20:24])
print(studants_List)
