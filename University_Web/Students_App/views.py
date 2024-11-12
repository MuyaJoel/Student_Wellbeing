from django.shortcuts import render

# Create your views here.
from .models import StudentRecords

def dashboard(request):
    students=StudentRecords.objects.filter(needs_assistance=True)
    print(students.values())
    
    return render(request, 'Students_App/index.html',{'students':students})