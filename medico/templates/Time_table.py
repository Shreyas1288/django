

#Details of each Teacher
num=int(input("Enter Total number of teachers"))
slot=int(input("Total number of slot"))
teacher_name=[]
teachers_class=[]  #numbers
timetable=[[],[],[],[],[],[]]
dikkat_slot=[[2,3,4,5,8],[2,8],[1,3]]        #alphabets
sum=0
for i in num:
    print("Details of teacher"+str(num))        #initially 3
    teacher_name.append(input("Enter teacher name"))
    teachers_class.append(input("Enter total class in a week"))

for i in teachers_class:
    sum=sum+i

if(sum>6*slot):
    print("Cannot make Time Table (please increase slots)")

else:
    for i in range(6):



