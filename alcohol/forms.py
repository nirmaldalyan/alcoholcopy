from email import message

from urllib import request
from django import forms
class userform(forms.Form):
    #num1=forms.CharField(labell="value1",required=False,widget=forms.TextInput)
    #num2=forms.CharField(label2="value2",widget=forms.TextInput)
    num1=forms.CharField(label="value1") #,widget=forms.TextInput(attrs={'class': "form-control"}),max_length=100)
    num2=forms.CharField(label="value2")
    num3=forms.CharField(label="value3",required="false") #required hh yha nhi hh to use kr skte hh
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea) 

    #differnt type of filed already in forms read from online
    #data={'a':num1,'b':num2,'c':num3,'d':email,'e':message}

    #def data(self):
        #print(self.num1)
        #print(self.num2)
        #print(self.num3)
        






    
    




        