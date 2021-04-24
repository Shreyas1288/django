from django.shortcuts import render
from django.http import HttpResponse
from institute.models import Institute_Details,Login,Branches,Teachers
from . models import Generate
# Create your views here.
def generate(request,id):

    obj=Institute_Details.objects.get(id=id)
    obj1=Login(id=obj.c_id.id)
    obj2=Branches.objects.all()
    obj3=Teachers.objects.all()

    branch=[]                  # College branches
    list_var_teachers = []
    list_var_branches = []    # Teacher branches
    list_var_classes=[]        # problen slots
    list_var_lecturesno=[]
    time_table=[]
    max_class=[]

    for i in obj3:
            if(i.c_id.id==id):
                var2=[]
                var1=i.problem

                str1=""
                for j in var1:
                    if(j==","):
                        var2.append(str1)
                        str1=""

                    elif(j==" "):
                        continue
                    else:
                        str1=str1+j
                list_var_classes.append(var2)
                var2=[]
                var1 = i.classes
                str1 = ""
                for j in var1:
                    if (j == ","):
                        var2.append(str1)
                        str1 = ""
                        continue
                    elif (j == " "):
                        continue
                    else:
                        str1 = str1 + j
                list_var_branches.append(var2)

                list_var_teachers.append(i.id)
                max_class.append(1)
                list_var_lecturesno.append(i.no_lectures)

    for i in obj2:
        if(i.c_id.id==id):
            branch.append(i.id)

    for i in range(6 * (obj.slots) *(len(branch))):
        time_table.append(0)

    print(list_var_branches)
    print(list_var_teachers)
    print(list_var_lecturesno)
    print(list_var_classes)
    print(branch)
    for i in range(len(branch)):
        str1=""
        p=list_var_lecturesno[:]
        counter = -1
        for j in range(6*(obj.slots)):

            if(j%obj.slots==0):
                counter=counter+1
                q=max_class[:]

            max=-1
            flag=0
            teacher=-1
            teacher_no=-1
            for k in range(len(list_var_teachers)):

                var=len(list_var_classes[k])
                if(var>max and p[k]>0 and q[k]>0):        #dikkat slot max

                    if(str(j%obj.slots) in list_var_classes[k]):    #dikkat slot check
                        continue

                    if(str(branch[i]) in list_var_branches[k]):
                        counter1=-1
                        for l in list_var_branches[k]:    #koi aur branch
                            counter1=counter1+1
                            flag = 0

                            if(l==branch[i]):
                                continue

                            if((str(list_var_teachers[k])) == (str((time_table[6*counter1*obj.slots+j])))):

                                flag=1
                                break


                        if flag==0:
                            max=var
                            teacher_no=k

                            teacher=list_var_teachers[k]

                        elif flag==1:
                            continue

            if(teacher==-1):

                    time_table[6*i*obj.slots+j]=0


            else:
                p[teacher_no] = p[teacher_no] - 1
                q[teacher_no]=q[teacher_no]-1

                time_table[6 * i * obj.slots + j] = teacher

        for j in range(len(p)):

            if(p[j]>0):

                if(branch[i] in list_var_branches[j]):
                    counter2=-1

                    for k in (6*obj.slots):
                        if(k%obj.slots==0):
                            counter2=counter2+1
                        if(time_table[6*obj.slots*counter+k]!=0):
                            continue
                        if((k%obj.slots) in list_var_classes[k]):
                            continue
                        else:
                            counter3=-1
                            flag=0
                            for l in branch:
                                counter3=counter3+1
                                if (l == branch[i]):
                                    continue

                                if ((str(list_var_teachers[j])) == (str((time_table[6 * counter3 * obj.slots + j])))):
                                    flag = 1
                                    break
                            if flag==1:
                                continue
                            elif flag==0:
                                time_table[i*6*obj.slots+k]=list_var_teachers[j]
                                p[j]=p[j]-1

        for j in range(len(p)):

            if (p[j] > 0):
                for k in (6 * obj.slots):
                    if (k % obj.slots == 0):
                        counter2 = counter2 + 1
                    if (time_table[6 * obj.slots * counter + k] != 0):
                        continue

                    else:
                        counter3 = -1
                        flag = 0
                        for l in branch:
                            counter3 = counter3 + 1
                            if (l == branch[i]):
                                continue

                            if ((str(list_var_teachers[j])) == (str((time_table[6 * counter3 * obj.slots + j])))):
                                flag = 1
                                break
                        if flag == 1:
                            continue
                        elif flag == 0:
                            time_table[i * 6 * obj.slots + k] = list_var_teachers[j]
                            p[j] = p[j] - 1

        for j in range(6*obj.slots*i,6*obj.slots*(i+1)):

            str1=str1+str(time_table[j])+","

        print(p)
        print(str1)
        obj4=Generate()
        obj4.timetable=str1
        obj4.c_id=obj1
        obj4.save()

    return (render(request,"home.html"))