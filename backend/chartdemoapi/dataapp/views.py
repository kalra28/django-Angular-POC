from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

#Create your views here.

labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Sep']
data=[195, 240, 252, 202, 298, 305, 250, 310]
def home(request):
    output=[]
    i=0
    while i < len(labels):
        x=labels[i];
        number=data[i];
        output.append({'month':x,'num':number});
        i=i+1;  
    return JsonResponse(output,safe=False);
