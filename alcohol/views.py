import email
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect  #ye bhi page redirect k kaam aata hh
from first.models import first            #yha se model ko call kiya
from news.models import news
from .forms import userform
from database.models import enquiry
from django.core.mail import send_mail

def homepage(request): 
    firstdata=first.objects.all()      #yha se sara data call kiya through all key  #model ka data laya jaa rha hh
    seconddata=first.objects.all().order_by('id')                                       #order key ka use kr k assending and decending kre ge
                                                                                           #icon k according assending m hoga
                                                                                            #decending k liye bs .order_by('-icon')
    thirddata=first.objects.all()[:3]                                      #limit function show krne k liye
    
    newsdata=news.objects.all()
    
    data={'title':'nirmal',
    'firstdata':firstdata,'seconddata':seconddata,'thirddata':thirddata,'newsdata':newsdata}              #data ki dictnoray  bna kr   usme first data k through add kiya
    return render(request,"index.html",data)                                            #yha pe html page pe send kiya


def about(request):
    return render(request,"aboutus.html")
def designregister(request):
    return render(request,"design form.html")
def career(request):

    if request.method=="GET":      #ye get method lga
        output=request.GET.get('output')  #yha se output post method k output ka use kiya 
    return render(request,"career.html",{'output':output})     #yha niche se function ko call karya gaya dynamic url k liye #yha pe form ka data show  hua output k through
def python(request,python):
    return HttpResponse("webpage developer, data science, artificial intelligance")
def service(request):
    return HttpResponse("""service provided by us:
    1. filling a case file
    2. consultant facilitys
    3.not ggo
    """)
    
def userformget(request):
    finalans=0                                                             #????not getting value of finalans 
    try:
        # n1=int(request.GET['NUM1'])                   #get method url pe data send krta hh default
        # # n1=int(request.GET['NUM1'])         #1 ist method of get
        n1=int(request.GET.get('num1'))        # 2nd menthod of get krne k liye vlaue
        n2=int(request.GET.get('num2'))
        finalans=n1+n2
    except:
        pass
    
    return render(request,"userformget.html",{'output':finalans})

def userformpostredirect(request):
    d=0
    delta={}                                                              #????not getting value of finalans 
    try:
        # n1=int(request.GET['NUM1'])                   #get method url pe data send krta hh default
        # # n1=int(request.GET['NUM1'])         #1 ist method of get
        if request.method=="POST": 
            n1=int(request.POST.get('num1'))        # 2nd menthod of get krne k liye vlaue
            n2=int(request.POST.get('num2'))
        d=n1+n2
        delta={
            'n1':n1,
            'n2':n2,
            'output':d
        }
                    
        url="/career/?output={}".format(d)
        #return HttpResponseRedirect(url)   # 1st url m dekhane k liye agar page k ander dekhna hh to carrer method pe jana hoga
        return redirect(url)   #1st/1 same function like 1st on https and /1 is on shortcut look on top.
        #return HttpResponseRedirect('/career/')   # 2nd methodess se direct hmm carrer or thanku page pr jaa skte hh

    except:
        pass
    return render(request,"userformpostredirect.html",delta)




def submitform(request):
    try:
        # n1=int(request.GET['NUM1'])                   #get method url pe data send krta hh default
        # # n1=int(request.GET['NUM1'])         #1 ist method of get
        if request.method=="POST": 
            n3=int(request.POST.get('num1'))        # 2nd menthod of get krne k liye vlaue
            n4=int(request.POST.get('num2'))
        d=n3+n4
        e=n3-n4
        delta={
            'n3':n3,
            'n4':n4,
            'output':d,
            'test':e
        }
                    
        
        #return HttpResponse(d) 
        #return HttpResponse(e)               #htttpresponse show only 1 variable either e or d or any string
        #return HttpResponse("welcome to submit form")
        return render(request,"submitform.html",delta) 
        
    except:
        pass

   

def userformpostaction(request):
    d=0
    delta={}                                                              #????not getting value of finalans 
    try:
            # n1=int(request.GET['NUM1'])                   #get method url pe data send krta hh default
         # n1=int(request.GET['NUM1'])         #1 ist method of get
        if request.method=="POST": 
            n3=int(request.POST.get('num1'))        # 2nd menthod of get krne k liye vlaue
            n4=int(request.POST.get('num2'))
        d=n3+n4
        e=n3-n4
        delta={
            'n3':n3,
            'n4':n4,
            'output':d,
            'test':e
        }
                    
        url="/career/?output={}".format(d)
        #return HttpResponseRedirect(url)   # 1st url m dekhane k liye agar page k ander dekhna hh to carrer method pe jana hoga
        return redirect(url)   #1st/1 same function like 1st on https and /1 is on shortcut look on top.
        #return HttpResponseRedirect('/career/')   # 2nd methodess se direct hmm carrer or thanku page pr jaa skte hh

    except:
        pass
    return render(request,"userformpostaction.html",delta)




#  form  through django application start-----create a foam.py file in alcohol folder
                                           #class to import kiya from about said file---from .forms import userfor
def submitform1(request):
    dj=userform()          #yha pe django form ko call kiya
    dj2=dj.data    
    delta={'dj1':dj,'dj2':dj2
    }
    
    


    #return render(request,"submitform1.html",delta)--
    #alpha={}
    try:
        if request.method=="POST": 
            fm=userform(request.POST)
            if fm.is_valid():
                print('Form validated')
                print('Name:',fm.cleaned_data['num1'])
                print('roll no:',fm.cleaned_data['num2'])
                print('class:',fm.cleaned_data['num3'])
                print('email:',fm.cleaned_data['email'])
                print('message:',fm.cleaned_data['message'])
        else:
            fm=userform()

            



        
                    
        
        #return HttpResponse(d) 
        #return HttpResponse(e)               #htttpresponse show only 1 variable either e or d or any string
        #return HttpResponse("welcome to submit form")
        return render(request,"submitform1.html",{'form':fm}) 
        
    except:
        pass
def djangoform(request):
    dj=userform()          #yha pe django form ko call kiya
    delta={'dj1':dj
    }
                                                                

    return render(request,"djangoform.html",delta)







def formfordatabase(request):
    return render(request,"formdatabaseenquirymodel.html")

def saveenquiry(request):  #yha database me data jana ki query hh
    if request.method=="POST":
        name=request.POST.get('num1')
        email=request.POST.get('num2')
        phoneno=request.POST.get('num3')
        website=request.POST.get('num4')
        message=request.POST.get('num5')
        en=enquiry(name=name,email=email,phoneno=phoneno,website=website,message=message)  #ye get krne k liye        
        en.save()               #ye save krne k liye
    return render(request,"formdatabaseenquirymodel.html")






def calculator(request): 
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="invalid opr"
    return render(request,"calculator.html",{'c':c})

def newsdetails(request,newsid):
    return render(request,"newsdetails.html")

#gmail connection to # formfordatabase form se next use hoga
 #send_mail(
         #   'testing mail',
          #  'here is the message',
         #   'nirmal98741@gmail.com',
         #   ['nirmalsingh000153@gmail.com'],
         #   fail_silently=False,
        # )
