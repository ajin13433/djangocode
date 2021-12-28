from django.shortcuts import render
from django.http import HttpResponse
from .models import problem
from . models import solutions
from . models import *
import subprocess
import filecmp

def home(request):
    return render(request,'app1/home.htm')

def first(request):
    context={
        'quest':problem.objects.all(),
        'solu':solutions.objects.all()
    }
    return render(request,'app1/first.htm',context)

def second(request,pk):
    if request.method=='POST':
        code = request.POST['code']
        obj=problem.objects.get(id=pk)
        obj.code=code
        obj.save()
        asp=test.objects.filter(prob=pk).count()
        print(asp)
        with open('media/code.cpp','w+') as f:
            f.write(obj.code)          
        open("media/output1.txt",'w+')
        subprocess.call(["g++","media/code.cpp"])
        l=0
        for i in range(1,asp+1):
            tst=test.objects.get(prob=pk,index=i)
            tst.save() 
            with open('media/input.txt','w+') as f:
                f.write(tst.inp) 
            with open('media/output.txt','w+') as f:
                f.write(tst.oup) 
            with open('media/output.txt', 'r+') as f:
                txt = f.read().replace('\n', '' )
                f.seek(0)
                f.write(txt)
                f.truncate() 
            subprocess.call("a.exe <media/input.txt> media/output1.txt",shell=True,text='true')
            with open('media/output1.txt', 'r+') as f:
                txt1 = f.read().replace('\n', '' )
                f.seek(0)
                f.write(txt1)
                f.truncate() 
            f2 = "media/output1.txt"
            f1 = "media/output.txt"
            result = filecmp.cmp(f1,f2,shallow="false")
            if result==True:
                l=l+1
                print("accepted")
            else:
                print("wrong")    
            sol=solutions.objects.get(prob=pk)
            if l==asp:
                sol.verdict=1
            else:
                sol.verdict=0
            sol.save() 
    context={
        'quest':problem.objects.get(id=pk),
        'solu':solutions.objects.get(prob=pk)
    }              
    return render(request,'app1/second.htm',context)    

def third(request):
    return render(request,'app1/third.htm') 
