from django.shortcuts import render
from .models import *

def home(request):
    
    grades = Grade.objects.all()
    grades_all = Grade.everything.all()
    print("Grades_all: ", grades_all)
    grades_all[0].soft_delete()
    print("Grades: ", grades)
    students_all = Student.everything.all()
    students = Student.objects.all()
    print("\n")
    print("Student_all: ", students_all)
    print("Students: ", students)

    grades_all[0].restore()
    students_all = Student.everything.all()
    students = Student.objects.all()
    print("after\n")
    print("Student_all: ", students_all)
    print("Students: ", students)
    return render(request, 'home.html')