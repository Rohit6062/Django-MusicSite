from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    Name=request.POST.get('name','None')
    Email=request.POST.get('email','None')
    Query=request.POST.get('??','None')
    param={
        'Name':Name,
        'Email':Email,
        'Query':Query
    }
    with open('static/DATA/data.txt','a') as f:
        f.write(str(param))
        f.write('\n')
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
print('rohit')