from django.shortcuts import render
from django.http import HttpResponse
from .models import Institute_Details,Login,Branches,Teachers
# Create your views here.

def home(request):
    return (render(request,"home.html"))

def register(request):
    return (render(request,"register.html"))

def register1(request):
    if(request.method=="POST"):
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        branches = request.POST["branches"]

        obj=Login()
        obj.username=username
        obj.password=password
        obj.email=email
        obj.branches_no = (int)(branches)
        obj.save()
        return (render(request,"home.html"))

def login(request):
    return (render(request,"login.html"))

def login1(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        obj=Login.objects.all()
        flag=0
        obj1 = Institute_Details.objects.all()
        slots = []
        obj5=Branches.objects.all()
        counter1=0
        collegeopen=""
        collegeclose=""
        for i in obj:
            if((i.username==username) or (i.email==username)):
                if(i.password==password):

                    for j in obj1:
                        if((j.c_id.id==i.id) and (j.details=="True")):

                            flag=1
                            if(j.tdetails=="True"):
                                return(render(request,"home1.html",{"id":j.id}))
                            else:
                                collegeopen=j.college_open
                                collegeclose=j.college_close
                                ostatus = str(collegeopen[len(collegeopen) - 2]) + str(
                                    collegeopen[len(collegeopen) - 1])
                                cstatus = str(collegeclose[len(collegeclose) - 2]) + str(
                                    collegeclose[len(collegeclose) - 1])
                                flag = 0
                                ohr = ""
                                omin = ""
                                chr = ""
                                cmin = ""

                                var = 60

                                ohr = str(collegeopen[0]) + str(collegeopen[1])
                                omin = str(collegeopen[3]) + str(collegeopen[4])
                                if (ostatus == "PM"):
                                    ohr = (int)(ohr) + 12
                                    omin = (int)(omin)
                                else:
                                    ohr = (int)(ohr)
                                    omin = (int)(omin)

                                chr = str(collegeclose[0]) + str(collegeclose[1])
                                cmin = str(collegeclose[3]) + str(collegeclose[4])

                                if (cstatus == "PM"):
                                    chr = (int)(chr) + 12
                                    cmin = (int)(cmin)
                                else:
                                    chr = (int)(chr)
                                    cmin = (int)(cmin)

                                counter = 0
                                slots1 = []
                                while (ohr <= (chr)):
                                    if (ohr == chr):
                                        if (omin < cmin):
                                            if (((var - ((omin + var) % 60)) < cmin) and ((((omin + var) / 60) + ohr) < chr)):
                                                omin = var - ((omin + var) % var)
                                                ohr = ohr + ((omin + var) / var)
                                                if (omin == 0):
                                                    if ((ohr == 12) and (omin == 0)):
                                                        slots1.append(str((int)(ohr)) + ":00 NOON")
                                                        slots1.append(str(counter))
                                                        counter = counter + 1
                                                        slots.append(slots1)
                                                        slots1 = []

                                                    elif (ohr >= 12):

                                                        if(omin==0):

                                                            slots1.append("0"+str((int)(ohr) % 12) +":"+ str(omin) + "0 PM")
                                                            slots1.append(str(counter))
                                                            counter = counter + 1
                                                            slots.append(slots1)
                                                            slots1 = []
                                                        else:
                                                            slots1.append("0"+str((int)(ohr) % 12) +":"+ str(omin) + "PM")
                                                            slots1.append(str(counter))
                                                            counter = counter + 1
                                                            slots.append(slots1)
                                                            slots1 = []


                                                    else:
                                                        if (ohr < 10):
                                                            if(omin==0):
                                                                slots1.append("0" + str((int)(ohr) % 12) +":"+ str(omin) + "0 AM")
                                                                slots1.append(str(counter))
                                                                counter = counter + 1
                                                                slots.append(slots1)
                                                                slots1 = []
                                                            else:
                                                                slots1.append( "0" + str((int)(ohr) % 12) +":"+ str(omin) + "AM")
                                                                slots1.append(str(counter))
                                                                counter = counter + 1
                                                                slots.append(slots1)
                                                                slots1 = []


                                                        else:

                                                            slots1.append("0"+str((int)(ohr) % 12) +":"+ str(omin) + "AM")
                                                            slots1.append(str(counter))
                                                            counter = counter + 1
                                                            slots.append(slots1)
                                                            slots1 = []
                                        else:
                                            break
                                    else:
                                        ohr = ohr + ((omin + var) / 60)
                                        omin = omin + ((omin + var) % 60)
                                        if (omin == 0):
                                            if ((ohr == 12) and (omin == 0)):
                                                slots1.append(str((int)(ohr)) + ":00 NOON")
                                                slots1.append(str(counter))
                                                counter = counter + 1
                                                slots.append(slots1)
                                                slots1 = []

                                            elif (ohr >= 12):
                                                if (ohr > 10):
                                                    if(omin==0):
                                                        slots1.append("0" + str((int)(ohr) % 12) +":"+ str(omin) + "0 PM")
                                                        slots1.append(str(counter))
                                                        counter = counter + 1
                                                        slots.append(slots1)
                                                        slots1 = []
                                                    else:
                                                        slots1.append("0"+str((int)(ohr) % 12) ++ ":"+ str(omin)  + " PM")
                                                        slots1.append(str(counter))
                                                        counter = counter + 1
                                                        slots.append(slots1)
                                                        slots1 = []

                                                elif(omin==0):
                                                    slots1.append("0"+str((int)(ohr) % 12) +":"+ str(omin) + "0 PM")
                                                    slots1.append(str(counter))
                                                    counter = counter + 1
                                                    slots.append(slots1)
                                                    slots1 = []
                                                else:
                                                    slots1.append(str((int)(ohr) % 12) +":"+ str(omin) + " PM")
                                                    slots1.append(str(counter))
                                                    counter = counter + 1
                                                    slots.append(slots1)
                                                    slots1 = []
                                            else:
                                                if (ohr < 10):
                                                    if(omin==0):
                                                        slots1.append("0" + str((int)(ohr) % 12) +":"+ str(omin) + "0 AM")
                                                        slots1.append(str(counter))
                                                        counter = counter + 1
                                                        slots.append(slots1)
                                                        slots1 = []
                                                    else:
                                                        slots1.append("0" + str((int)(ohr) % 12) +":"+ str(omin) + "AM")
                                                        slots1.append(str(counter))
                                                        counter = counter + 1
                                                        slots.append(slots1)
                                                        slots1 = []

                                                elif(omin==0):
                                                    slots1.append(str((int)(ohr) % 12) +":"+ str(omin) + "0 AM")
                                                    slots1.append(str(counter))
                                                    counter = counter + 1
                                                    slots.append(slots1)
                                                    slots1 = []
                                                else:
                                                    slots1.append(str((int)(ohr) % 12) +":"+ str(omin) + "AM")
                                                    slots1.append(str(counter))
                                                    counter = counter + 1
                                                    slots.append(slots1)
                                                    slots1 = []

                                slot3 = []
                                slot4=[]
                                for m in obj5:
                                    if(i.id==m.c_id.id):
                                        slot3=[]
                                        slot3.append(m.b_name)
                                        slot3.append(str(counter1))
                                        slot3.append(str(m.id))
                                        counter1=counter1+1
                                        slot4.append(slot3)
                                slot5=[]
                                for m in range(j.teachers_no):
                                    slot5.append(str(m))

                                print(i.id)
                                print(slots)
                                print(len(slots))
                                print(j.teachers_no)
                                print(slot4)
                                print(slot5)
                                print(len(slot5))

                                return (render(request,"teacher_detail.html",{"id":i.id,"slots":slots,"len_slots":len(slots),"len_teacher":j.teachers_no,"slot4":slot4,"len_slots4":len(slot4),"slot5":slot5}))
                    if(flag==0):
                        var=i.branches_no
                        slots=[]
                        for m in range(var):
                            slots.append(m)

                        return(render(request,"college_details.html",{"id":i.id,"slots":slots,"len":len(slots)}))
        else:
            return (render(request,"register.html"))


def college_details(request):
    if request.method=="POST":
        name = request.POST["name"]
        teachers = request.POST["teachers"]
        collegeopen = request.POST["collegeopen"]
        collegeclose = request.POST["collegeclose"]
        id=request.POST["id"]
        id=(int)(id)
        length=request.POST["len"]
        length=(int)(length)
        branch=""
        slot3=[]
        slot4=[]

        for i in range(length):
            obj = Branches()
            branch=request.POST["branch"+str(i)]
            obj1=Login.objects.get(id=id)
            obj.b_name=branch
            obj.c_id=obj1
            obj.save()

        obj1=Login.objects.get(id=id)
        obj = Institute_Details()

        obj.name = name
        obj.teachers_no = (int)(teachers)
        obj.college_open =collegeopen
        obj.college_close =collegeclose
        obj.details=True
        obj.tdetails=False
        obj.c_id=obj1

        slots = []
        obj5 = Branches.objects.all()
        ostatus = str(collegeopen[len(collegeopen) - 2]) + str(
            collegeopen[len(collegeopen) - 1])
        cstatus = str(collegeclose[len(collegeclose) - 2]) + str(
            collegeclose[len(collegeclose) - 1])
        flag = 0
        ohr = ""
        omin = ""
        chr = ""
        cmin = ""

        var = 60

        ohr = str(collegeopen[0]) + str(collegeopen[1])
        omin = str(collegeopen[3]) + str(collegeopen[4])
        if (ostatus == "PM"):
            ohr = (int)(ohr) + 12
            omin = (int)(omin)
        else:
            ohr = (int)(ohr)
            omin = (int)(omin)

        chr = str(collegeclose[0]) + str(collegeclose[1])
        cmin = str(collegeclose[3]) + str(collegeclose[4])

        if (cstatus == "PM"):
            chr = (int)(chr) + 12
            cmin = (int)(cmin)
        else:
            chr = (int)(chr)
            cmin = (int)(cmin)

        counter = 0
        slots1 = []
        while (ohr <= (chr)):
            if (ohr == chr):
                if (omin < cmin):
                    if (((var - ((omin + var) % 60)) < cmin) and ((((omin + var) / 60) + ohr) < chr)):
                        omin = var - ((omin + var) % var)
                        ohr = ohr + ((omin + var) / var)
                        if (omin == 0):
                            if ((ohr == 12) and (omin == 0)):
                                slots1.append(str((int)(ohr)) + ":00 NOON")
                                slots1.append(counter)
                                counter = counter + 1
                                slots.append(slots1)
                                slots1 = []

                            elif (ohr >= 12):

                                if (omin == 0):

                                    slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "0 PM")
                                    slots1.append(counter)
                                    counter = counter + 1
                                    slots.append(slots1)
                                    slots1 = []
                                else:
                                    slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "PM")
                                    slots1.append(counter)
                                    counter = counter + 1
                                    slots.append(slots1)
                                    slots1 = []


                            else:
                                if (ohr < 10):
                                    if (omin == 0):
                                        slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "0 AM")
                                        slots1.append(counter)
                                        counter = counter + 1
                                        slots.append(slots1)
                                        slots1 = []
                                    else:
                                        slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "AM")
                                        slots1.append(counter)
                                        counter = counter + 1
                                        slots.append(slots1)
                                        slots1 = []


                                else:

                                    slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "AM")
                                    slots1.append(counter)
                                    counter = counter + 1
                                    slots.append(slots1)
                                    slots1 = []
                else:
                    break
            else:
                ohr = ohr + ((omin + var) / 60)
                omin = omin + ((omin + var) % 60)
                if (omin == 0):
                    if ((ohr == 12) and (omin == 0)):
                        slots1.append(str((int)(ohr)) + ":00 NOON")
                        slots1.append(counter)
                        counter = counter + 1
                        slots.append(slots1)
                        slots1 = []

                    elif (ohr >= 12):
                        if (ohr > 10):
                            if (omin == 0):
                                slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "0 PM")
                                slots1.append(counter)
                                counter = counter + 1
                                slots.append(slots1)
                                slots1 = []
                            else:
                                slots1.append("0" + str((int)(ohr) % 12) + + ":" + str(omin) + " PM")
                                slots1.append(counter)
                                counter = counter + 1
                                slots.append(slots1)
                                slots1 = []

                        elif (omin == 0):
                            slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "0 PM")
                            slots1.append(counter)
                            counter = counter + 1
                            slots.append(slots1)
                            slots1 = []
                        else:
                            slots1.append(str((int)(ohr) % 12) + ":" + str(omin) + " PM")
                            slots1.append(counter)
                            counter = counter + 1
                            slots.append(slots1)
                            slots1 = []
                    else:
                        if (ohr < 10):
                            if (omin == 0):
                                slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "0 AM")
                                slots1.append(counter)
                                counter = counter + 1
                                slots.append(slots1)
                                slots1 = []
                            else:
                                slots1.append("0" + str((int)(ohr) % 12) + ":" + str(omin) + "AM")
                                slots1.append(counter)
                                counter = counter + 1
                                slots.append(slots1)
                                slots1 = []

                        elif (omin == 0):
                            slots1.append(str((int)(ohr) % 12) + ":" + str(omin) + "0 AM")
                            slots1.append(counter)
                            counter = counter + 1
                            slots.append(slots1)
                            slots1 = []
                        else:
                            slots1.append(str((int)(ohr) % 12) + ":" + str(omin) + "AM")
                            slots1.append(counter)
                            counter = counter + 1
                            slots.append(slots1)
                            slots1 = []
        obj.slots=len(slots)
        obj.save()

        slot3 = []
        slot4 = []
        counter1=0
        for m in obj5:
            if (id == m.c_id.id):
                slot3 = []
                slot3.append(m.b_name)
                slot3.append(counter1)
                slot3.append(m.id)
                counter1 = counter1 + 1
                slot4.append(slot3)
        obj7=Institute_Details.objects.all()
        var6=0
        slot5 = []
        for l in obj7:
            if(id==l.c_id.id):
                var6=l.teachers_no

                for n in range(l.teachers_no):
                    slot5.append(n)
        print(id)
        print(slots)
        print(len(slots))
        print(var6)
        print(slot4)
        print(slot5)
        print(len(slot5))
        return (render(request,"teacher_detail.html",{"id": id, "slots": slots, "len_slots": len(slots), "len_teacher": var6,"slot4": slot4, "len_slots4": len(slot4), "slot5": slot5}))

def success(request):
    if(request.method=="POST"):
        len_slots=request.POST["len_slots"]
        len_slots4=request.POST["len_slots4"]
        len_teacher=request.POST["len_teacher"]
        len_slots=(int)(len_slots)
        len_slots4=(int)(len_slots4)
        len_teacher=(int)(len_teacher)
        id=request.POST["id"]
        print(len_slots)
        print(len_slots4)
        print(len_teacher)
        id=(int)(id)
        obj1=Institute_Details.objects.all()
        obj7=Login.objects.get(id=id)
        for i in obj1:
            if(i.c_id.id==id):
                obj2=Institute_Details.objects.get(id=i.id)
                obj2.tdetails=True
                var_1=i.id
                obj2.save()


        for i in range(len_teacher):
            var2 = ""
            var5=""
            print(i)
            obj6 = Teachers()
            var="time"+str(i)+"[]"
            var3=request.POST.getlist(var)

            for j in var3:
                var2=var2+j+","

            var="value"+str(i)+"[]"
            var4=request.POST.getlist(var)

            for j in var4:
                var6="checkbox"+str(j)
                var7=request.POST[var6]
                var5=var5+str(var7)+","

            t_name=request.POST["name"+str(i)]
            classes=request.POST["class"+str(i)]

            obj6.teacher_name=t_name
            obj6.no_lectures=(int)(classes)
            obj6.problem=var2
            obj6.classes=var5
            obj6.c_id=obj7
            obj6.save()

        return (render(request,"home1.html",{"id":var_1}))

