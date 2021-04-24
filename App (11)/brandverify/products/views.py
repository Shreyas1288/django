from django.shortcuts import render,redirect,HttpResponseRedirect
import random
from django.http import HttpResponse
from . models import Register
import hashlib
import datetime
import json

class Blockchain():

    def __init__(self):
        self.curr_hash=0x0
        self.max_nonce=pow(2,32)
        self.chain=[]
        self.index =len(self.chain)+1
        self.prevhash="00000000000000000000"
        self.transactions=[]
        self.timestamp = datetime.datetime.now()
        self.nonce=0
        self.create_block(self.nonce,self.prevhash,self.timestamp)

    def create_block(self,nonce,previous,timestamp):
        self.index=len(self.chain)+1
        block={
                "index":self.index,
                "nonce":nonce,
                "prev_hash":previous,
                "timestamp":str(timestamp),
                "transactions":self.transactions

        }
        self.curr_hash=self.calc_hash(block)
        self.chain.append(block)
        self.transactions=[]

    def add_transactions(self,sender,reciever,amount,time):

        self.transactions.append({"sender":sender,"reciever":reciever,"amount":amount,"time":str(time)})

    def get_last_block(self):

        return (self.chain[-1])


    def calc_hash(self,block):

        str1=json.dumps(block,sort_keys=True)
        hash=hashlib.sha3_256(str1.encode()).hexdigest()
        return hash

    def mine(self,sender,reciever,amount):


        self.timestamp=datetime.datetime.now()
        self.index=len(self.chain)+1
        self.add_transactions(sender,reciever,amount,self.timestamp)
        time=self.timestamp
        self.nonce=self.proof_of_work(0,time)
        prevblock=self.get_last_block()
        self.prevhash=self.calc_hash(prevblock)
        self.create_block(self.nonce,self.prevhash,time)


    def proof_of_work(self,nonce,time):

        check_nonce=False
        prev_block=self.get_last_block()
        prev_hash=self.calc_hash(prev_block)

        while((check_nonce is False) and (nonce<self.max_nonce)):
            block = {
                "index": self.index,
                "nonce": nonce,
                "prev_hash": prev_hash,
                "timestamp": str(time),
                "transactions": self.transactions

            }
            str1 = json.dumps(block,sort_keys=True)
            hash_operation=hashlib.sha3_256(str1.encode()).hexdigest()
            if(hash_operation[:4]=="0000"):
                check_nonce=True
            else:
                nonce=nonce+1

        return nonce

    def is_chain_valid(self):

        if(self.curr_hash!= self.calc_hash(self.get_last_block())):
            return -1

        for i in range(1,len(self.chain)):
            prev_block=self.chain[i]
            if(self.calc_hash(self.chain[i-1]) != prev_block["prev_hash"]):
                return -1

        return 1

    def get_chain(self):

        return self.chain

blockchain=Blockchain()

def home(request):
    return (render(request,"home.html"))


def main(request):

    return (render(request,"main.html"))


def register_cust(request):

    request.session["old_post"] =False
    return (render(request,"register_cust.html"))


def register_cust1(request):
    if(request.method=="POST"):
        var=request.session.get("old_post")

        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm=request.POST["confirm"]
        obj=Register()
        obj.name=name
        obj.email=email
        obj.password=password
        obj.category="customer"
        obj.details=False
        if (var is False):
            obj.save()
        request.session["old_post"] = True
        return (render(request,"main.html"))



def register_sales(request):

    request.session["old_post"] = False
    return (render(request,"register_sales.html"))

def register_sales1(request):
    if (request.method == "POST"):
        var = request.session.get("old_post")

        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        obj = Register()
        obj.name = name
        obj.email = email
        obj.password = password
        obj.category = "salesman"
        obj.details = False
        if (var is False):
            obj.save()
        request.session["old_post"] = True
        return (render(request, "main.html"))


def login(request):
    return (render(request,"login.html"))

def login1(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        content = Register.objects.all()
        for i in content:
            if ((i.email == email) and (i.password == password) and (i.category == "customer")):
                return (render(request,"main.html"))

            elif((i.email == email) and (i.password == password) and (i.category == "salesman")):
                if(i.details is False):
                    print("Sethi")
                    request.session["old_post"]=False
                    return (render(request,"Fill_Details.html"))
                else:
                    print("Sethi1")
                    return (render(request,"main.html"))
        return (render(request,"login.html"))







